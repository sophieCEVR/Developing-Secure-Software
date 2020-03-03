# File to populate database with initial data - recommended to run create_database.py beforehand
# Database can be viewed here: https://inloop.github.io/sqlite-viewer/

from blogsite import db  # import the db object from the blogsite package
from blogsite import models  # import the models used by the database

if __name__ == '__main__':
    # Add test users
    for i in range(0, 20, 1):
        username_string = 'username' + str(i)
        password_string = 'password' + str(i)
        db.session.add(models.User(username=username_string, password=password_string))
    db.session.commit()
    # Add test posts
    allUsers = db.session.query(models.User)
    for usr in allUsers:
        for i in range(0, 20, 1):
            title_string = 'Test Post ' + str(i)
            body_string = 'This is a generated post'
            db.session.add(models.Post(title=title_string, body=body_string, author=usr))
    db.session.commit()
