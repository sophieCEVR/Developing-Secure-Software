# File to populate database with initial data - recommended to run create_database.py beforehand
# Database can be viewed here: https://inloop.github.io/sqlite-viewer/

from blogsite import app  # import the app object from the blogsite package
from blogsite import db  # import the db object from the blogsite package
from blogsite import models  # import the models used by the database

from blogsite import hashing  # import hashing

if __name__ == '__main__':
    # Add test users
    for i in range(0, 20, 1):
        username_string = 'username' + str(i)
        password_string = 'password' + str(i)
        email_string = 'usr' + str(i) + '@email.com'
        salt = hashing.generate_salt()
        password_hash = hashing.generate_hash(password_string, salt=salt, pepper=app.config.get('SECRET_KEY', 'no_secret_key'))
        db.session.add(models.User(username=username_string, password=password_hash, salt=salt, email=email_string))
        db.session.commit()
    # Add test posts
    allUsers = db.session.query(models.User)
    for i in range(0, 20, 1):
        for usr in allUsers:
            title_string = 'Test Post ' + str(i)
            body_string = 'This is a generated post'
            db.session.add(models.Post(title=title_string, body=body_string, author=usr))
        db.session.commit()
