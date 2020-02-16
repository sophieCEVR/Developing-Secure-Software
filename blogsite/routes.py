# File containing the routes for blogsite

from . import app  # import the app object from the current package

from . import forms  # import forms
from . import models

from flask import render_template, redirect, url_for, session, flash


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# Route for about page
@app.route('/posts')
def posts():
    allPosts = models.Post.query.all()
    return render_template('posts.html', title='Posts', posts=allPosts)

# Route for about page
@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        flash('Attempted Login')
        return redirect(url_for('home'))
    return render_template('login.html', form=form)
