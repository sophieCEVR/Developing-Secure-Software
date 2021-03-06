# File containing the routes for blogsite

from . import app, sanitise  # import the app object from the current package
from . import db  # import the db object from the current package

from . import forms  # import forms
from . import models  # import models

from flask import render_template, redirect, url_for, session, flash, request, escape

from datetime import datetime
import time

account_enumeration_times = {'posts_user_username': dict()}


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
        cleanpuserid = sanitise.all(p.user_id)
        raw_sql = 'SELECT username FROM user WHERE id="{}"'.format(cleanpuserid)
        p_user = db.session.execute(raw_sql).first()
        if p_user:
            post_usernames[p.id] = p_user.username
    return render_template('posts.html', posts=all_posts, post_usernames=post_usernames, title='Posts')


@app.route('/posts/view/<post_id>')
def posts_post_id(post_id=None):
    all_posts = []
    post_usernames = {}
    cleanpostid = sanitise.all(post_id)  # remove html chars, see sanitise.py
    raw_sql = 'SELECT * FROM post WHERE id="{}"'.format(cleanpostid)
    # flash(raw_sql)  # Flash the SQL for testing and debugging
    the_post = db.session.execute(raw_sql).first()
    if the_post:
        all_posts.append(the_post)
        cleanthepostuserid = sanitise.all(the_post.user_id)
        raw_sql = 'SELECT username FROM user WHERE id="{}"'.format(cleanthepostuserid)
        the_user = db.session.execute(raw_sql).first()
        if the_user:
            post_usernames[the_post.id] = the_user.username
    return render_template('posts.html', posts=all_posts, post_usernames=post_usernames, title='Posts')


@app.route('/posts/account/<user_username>')
def posts_user_username(user_username=None):
    wait_time = 0  # Initial time to wait
    start_time = time.time()  # Begin timing the process
    all_posts = []
    post_usernames = {}
    cleanusername = sanitise.all(user_username)
    raw_sql = 'SELECT id, username FROM user WHERE username="{}"'.format(cleanusername)
    # flash(raw_sql)  # Flash the SQL for testing and debugging
    the_user = db.session.execute(raw_sql).first()
    if the_user:
        cleantheuserid = sanitise.all(the_user.id)
        raw_sql = 'SELECT * FROM post WHERE user_id="{}" ORDER BY update_time DESC'.format(cleantheuserid)
        all_posts = db.session.execute(raw_sql).fetchall()
        for p in all_posts:
            post_usernames[p.id] = the_user.username
        try:  # Update average time of query (case = data present)
            account_enumeration_times['posts_user_username']['success'] += time.time() - start_time
            account_enumeration_times['posts_user_username']['success'] *= 0.5
        except KeyError:
            account_enumeration_times['posts_user_username']['success'] = time.time() - start_time
        if account_enumeration_times['posts_user_username'].get('failure'):  # Get the difference between average times
            wait_time = (account_enumeration_times['posts_user_username']['failure']
                         - account_enumeration_times['posts_user_username']['success'])
    else:
        try:  # Update average time of query (case = data NOT present)
            account_enumeration_times['posts_user_username']['failure'] += time.time() - start_time
            account_enumeration_times['posts_user_username']['failure'] *= 0.5
        except KeyError:
            account_enumeration_times['posts_user_username']['failure'] = time.time() - start_time
        if account_enumeration_times['posts_user_username'].get('success'):  # Get the difference between average times
            wait_time = (account_enumeration_times['posts_user_username']['success']
                         - account_enumeration_times['posts_user_username']['failure'])
    if wait_time > 0:
        time.sleep(wait_time)
    #flash(account_enumeration_times.get('posts_user_username'))  # Flash data for testing and debugging
    #flash('Wait Time = ' + str(wait_time))  # Flash wait time for testing and debugging
    return render_template('posts.html', posts=all_posts, post_usernames=post_usernames, title='Posts')


@app.route('/posts/create', methods=['GET', 'POST'])
def create_post():
    if not session.get('user_id'):
        flash('You must log in to create a post!')
        return redirect(url_for('login'))
    else:
        form = forms.CreatePostForm()

        if request.method == 'POST' and form.validate():
            cleansessionid = sanitise.all(session['user_id'])
            raw_sql = 'SELECT id FROM user WHERE id="{}"'.format(cleansessionid)
            # flash(raw_sql)  # Flash the SQL for testing and debugging
            the_user = db.session.execute(raw_sql).first()
            if the_user:  # Only create a post if the user exists
                cleanformtitle = sanitise.all(form.title.data)
                cleanformbody = sanitise.all(form.body.data)
                values = [cleansessionid, cleanformtitle, cleanformbody, datetime.utcnow(), datetime.utcnow()]
                raw_sql = 'INSERT INTO post (user_id, title, body, create_time, update_time) VALUES ({})'.format(
                    ', '.join('"{}"'.format(str(v)) for v in values)
                )
                # flash(raw_sql)  # Flash the SQL for testing and debugging
                db.session.execute(raw_sql)
                db.session.commit()
                flash('Your post has been created')
                return redirect(url_for('posts'))
            else:  # If the user does not exist, redirect to logout
                flash('An error occurred whilst processing your request')
                return redirect(url_for('logout'))
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
        cleanpostid = sanitise.all(request.form['post_id'])

        raw_sql = 'SELECT * FROM post WHERE id="{}"'.format(cleanpostid)
        # flash(raw_sql)  # Flash the SQL for testing and debugging
        the_post = db.session.execute(raw_sql).first()
        if not the_post or the_post.user_id != session['user_id']:  # only delete posts that exist and are owned by user
            flash('You cannot delete that')
            return redirect(url_for('posts_post_id', post_id=session['user_id']))
        else:
            cleanthepost = sanitise.all(the_post.id)
            raw_sql = 'DELETE FROM post WHERE id="{}"'.format(cleanthepost)
            # flash(raw_sql)  # Flash the SQL for testing and debugging
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
        if request.method == 'POST' and form.validate():
            cleanusername = sanitise.all(form.username.data)
            cleanpassword = sanitise.all(form.password.data)
            raw_sql = 'SELECT * FROM user WHERE username="{}" AND password="{}"'.format(
                cleanusername, cleanpassword
            )
            # flash(raw_sql)  # Flash the SQL for testing and debugging
            the_user = db.session.execute(raw_sql).first()
            if not the_user:
                values = [cleanusername, cleanpassword]
                raw_sql = 'INSERT INTO user (username, password) VALUES ({})'.format(
                    ', '.join('"{}"'.format(str(v)) for v in values)
                )
                # flash(raw_sql)  # Flash the SQL for testing and debugging
                db.session.execute(raw_sql)
                db.session.commit()
            flash('If this account did not already exist, you have created an account')
            return redirect(url_for('login'))
        return render_template('register.html', form=form, title='Create Account')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user_id'):  # redirect to home if logged in
        flash('You are already logged in!')
        return redirect(url_for('posts'))
    else:
        form = forms.LoginForm()
        if request.method == 'POST' and form.validate():
            cleanusername = sanitise.all(form.username.data)
            cleanpassword = sanitise.all(form.password.data)
            raw_sql = 'SELECT * FROM user WHERE username="{}" AND password="{}"'.format(
                cleanusername, cleanpassword
            )
            # flash(raw_sql)  # Flash the SQL for testing and debugging
            the_user = db.session.execute(raw_sql).first()
            if not session.get('login_attempts'):
                session['login_attempts'] = 1
            x = max(0, session['login_attempts'] - 2)  # Only stall login process after 2 unsuccessful login attempts
            wait_time = (5 * x) / (x + 1)
            # flash("Login Attempt " + str(session['login_attempts']))  # Flash login attempts for testing and debugging
            # flash("Wait Time = " + str(wait_time))  # Flash wait time for testing and debugging
            if wait_time > 0:
                time.sleep(wait_time)
            if the_user:
                session.pop('login_attempts', None)  # Successful login, forget login attempts
                session['user_id'] = the_user.id  # Log the user in (account operations depend on user_id)
                session['user_username'] = the_user.username
                flash('You have logged in as ' + str(the_user.username))
                return redirect(url_for('posts'))
            else:  # Unsuccessful login, increment login attempts
                session['login_attempts'] = min(32, session['login_attempts'] + 1)
                flash('Invalid username and/or password')
        # flash(form.errors)  # Flash form errors for testing and debugging
        return render_template('login.html', form=form, title='Login')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_username', None)
    flash('You have been logged out')
    return redirect(url_for('posts'))
