from flask import Flask, render_template, url_for
from SSD_A1 import app

posts = [
    {
    'author' : 'Jack Hilsdon',
    'title' : 'My first post!',
    'content' : 'Me me big boy don\'t hack me :( ',
    'date_posted' : '02/02/2020'
    },
    {
    'author' : 'Jeffffffff',
    'title' : 'HELLO',
    'content' : 'qweq ',
    'date_posted' : '06/02/2020'
    }
]

# Route for home page 
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

# Route for about page
@app.route('/posts')
def posts_page():
    return render_template('posts.html', title='Posts', posts=posts)

# Route for about page
@app.route('/about')
def about_page():
    return render_template('about.html', title='About')


