# File containing the routes for blogsite

from . import app  # import the app object from the current package
from . import db  # import the db object from the current package

from . import forms  # import forms
from . import models  # import models

from flask import render_template, redirect, url_for, session, flash, request


@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/posts')
@app.route('/posts/<view_argument>')
def posts(view_argument=None):
    all_posts = []
    if view_argument:
        if view_argument.isdigit():  # if argument is digit e.g. /post/2 (digit means post id)
            all_posts = db.session.query(models.Post).filter_by(id=view_argument)
        else:  # argument is not digit e.g. /post/_2 (not digit means account username)
            user = db.session.query(models.User).filter_by(username=view_argument).first()
            if user:
                all_posts = db.session.query(models.Post).filter_by(
                    user_id=user.id
                ).order_by(models.Post.update_time.desc())
    else:
        all_posts = db.session.query(models.Post).order_by(models.Post.update_time.desc())
    return render_template('posts.html', posts=all_posts, title='Posts')


@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if not session.get('user_id'):
        flash('You must log in to create a post!')
        return redirect(url_for('login'))
    else:
        form = forms.CreatePostForm()
        if form.validate_on_submit():
            db.session.add(models.Post(title=form.title.data, body=form.body.data, user_id=session['user_id']))
            db.session.commit()
            flash('Your post has been created')
            return redirect(url_for('posts'))
        return render_template('create_post.html', form=form, title='Create Post')


@app.route('/delete_post', methods=['POST'])
def delete_post(post_id=None):
    if not session.get('user_id'):
        flash('You must log in to delete a post!')
        return redirect(url_for('login'))
    else:
        the_post = db.session.query(models.Post).filter_by(id=request.form['post_id']).first()
        if not the_post or the_post.user_id != session['user_id']:  # only delete posts that exist and are owned by user
            flash('You cannot delete that')
            return redirect(url_for('posts', view_argument=request.form['post_id']))
        else:
            db.session.delete(the_post)
            db.session.commit()
            flash('Your post has been deleted')
            return redirect(url_for('posts'))


@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if session.get('user_id'):
        flash('Please logout before creating a new account!')
        return redirect(url_for('posts'))
    else:
        form = forms.CreateAccountForm()
        if form.validate_on_submit():
            existing_user = db.session.query(models.User).filter_by(username=form.username.data).first()
            if not existing_user:
                db.session.add(models.User(username=form.username.data, password=form.password.data))
                db.session.commit()
            flash('Your account has been created')
            return redirect(url_for('login'))
        return render_template('create_account.html', form=form, title='Create Account')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user_id'):  # redirect to home if logged in
        flash('You are already logged in!')
        return redirect(url_for('posts'))
    else:
        form = forms.LoginForm()
        if form.validate_on_submit():
            query_result = db.session.query(models.User).filter_by(
                username=form.username.data,
                password=form.password.data
            ).first()
            if query_result:
                session['user_id'] = query_result.id
                session['user_username'] = query_result.username
                flash('You have logged in as ' + str(query_result.username))
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
