# File containing the routes for blogsite

from . import app  # import the app object from the current package
from . import db  # import the db object from the current package

from . import forms  # import forms
from . import models  # import models

from flask import render_template, redirect, url_for, session, flash, request
from datetime import datetime


@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/posts')
def posts():
    all_posts = []
    post_usernames = {}
    raw_sql = 'SELECT * FROM post ORDER BY update_time DESC'
    all_posts = db.session.execute(raw_sql).fetchall()
    for p in all_posts:
        raw_sql = 'SELECT username FROM user WHERE id="{}"'.format(p.user_id)
        p_user = db.session.execute(raw_sql).first()
        if p_user:
            post_usernames[p.id] = p_user.username
    return render_template('posts.html', posts=all_posts, post_usernames=post_usernames, title='Posts')


@app.route('/posts/view/<post_id>')
def posts_post_id(post_id=None):
    all_posts = []
    post_usernames = {}
    raw_sql = 'SELECT * FROM post WHERE id="{}"'.format(post_id)
    flash(raw_sql)
    the_post = db.session.execute(raw_sql).first()
    if the_post:
        all_posts.append(the_post)
        raw_sql = 'SELECT username FROM user WHERE id="{}"'.format(the_post.user_id)
        the_user = db.session.execute(raw_sql).first()
        if the_user:
            post_usernames[the_post.id] = the_user.username
    return render_template('posts.html', posts=all_posts, post_usernames=post_usernames, title='Posts')


@app.route('/posts/account/<user_username>')
def posts_user_username(user_username=None):
    all_posts = []
    post_usernames = {}
    raw_sql = 'SELECT id, username FROM user WHERE username="{}"'.format(user_username)
    flash(raw_sql)
    the_user = db.session.execute(raw_sql).first()
    if the_user:
        raw_sql = 'SELECT * FROM post WHERE user_id="{}" ORDER BY update_time DESC'.format(the_user.id)
        all_posts = db.session.execute(raw_sql).fetchall()
        for p in all_posts:
            post_usernames[p.id] = the_user.username
    return render_template('posts.html', posts=all_posts, post_usernames=post_usernames, title='Posts')


@app.route('/posts/create', methods=['GET', 'POST'])
def create_post():
    if not session.get('user_id'):
        flash('You must log in to create a post!')
        return redirect(url_for('login'))
    else:
        form = forms.CreatePostForm()
        if form.validate_on_submit():
            values = [session['user_id'], form.title.data, form.body.data, datetime.utcnow(), datetime.utcnow()]
            raw_sql = 'INSERT INTO post (user_id, title, body, create_time, update_time) VALUES ({})'.format(
                ', '.join('"{}"'.format(str(v)) for v in values)
            )
            flash(raw_sql)
            db.session.execute(raw_sql)
            db.session.commit()
            flash('Your post has been created')
            return redirect(url_for('posts'))
        return render_template('create_post.html', form=form, title='Create Post')


@app.route('/posts/delete', methods=['POST'])
def delete_post(post_id=None):
    if not session.get('user_id'):
        flash('You must log in to delete a post!')
        return redirect(url_for('login'))
    elif not request.form.get('post_id'):
        flash('You must provide an id to delete a post!')
        return redirect(url_for('posts'))
    else:
        raw_sql = 'SELECT * FROM post WHERE id="{}"'.format(request.form['post_id'])
        flash(raw_sql)
        the_post = db.session.execute(raw_sql).first()
        if not the_post or the_post.user_id != session['user_id']:  # only delete posts that exist and are owned by user
            flash('You cannot delete that')
            return redirect(url_for('posts_post_id', post_id=request.form['post_id']))
        else:
            raw_sql = 'DELETE FROM post WHERE id="{}"'.format(the_post.id)
            flash(raw_sql)
            db.session.execute(raw_sql)
            db.session.commit()
            flash('Your post has been deleted')
            return redirect(url_for('posts'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('user_id'):
        flash('Please logout before creating a new account!')
        return redirect(url_for('posts'))
    else:
        form = forms.CreateAccountForm()
        if form.validate_on_submit():
            raw_sql = 'SELECT * FROM user WHERE username="{}" AND password="{}"'.format(
                form.username.data, form.password.data
            )
            flash(raw_sql)
            the_user = db.session.execute(raw_sql).first()
            if not the_user:
                values = [form.username.data, form.password.data]
                raw_sql = 'INSERT INTO user (username, password) VALUES ({})'.format(
                    ', '.join('"{}"'.format(str(v)) for v in values)
                )
                flash(raw_sql)
                db.session.execute(raw_sql)
                db.session.commit()
            flash('Your account has been created')
            return redirect(url_for('login'))
        return render_template('register.html', form=form, title='Create Account')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user_id'):  # redirect to home if logged in
        flash('You are already logged in!')
        return redirect(url_for('posts'))
    else:
        form = forms.LoginForm()
        if form.validate_on_submit():
            raw_sql = 'SELECT * FROM user WHERE username="{}" AND password="{}"'.format(
                form.username.data, form.password.data
            )
            flash(raw_sql)
            the_user = db.session.execute(raw_sql).first()
            if the_user:
                session['user_id'] = the_user.id
                session['user_username'] = the_user.username
                flash('You have logged in as ' + str(the_user.username))
                return redirect(url_for('posts'))
            else:
                flash('Invalid username and/or password')
        print(form.errors)  # Display form errors to console (e.g. 'username', 'csrf_token', etc) for testing/debugging
        return render_template('login.html', form=form, title='Login')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_username', None)
    flash('You have been logged out')
    return redirect(url_for('posts'))
