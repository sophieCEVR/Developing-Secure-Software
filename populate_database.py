# File to populate database with initial data - recommended to run create_database.py beforehand
# Database can be viewed here: https://inloop.github.io/sqlite-viewer/

from blogsite import db  # import the db object from the blogsite package
from blogsite import models  # import the models used by the database

if __name__ == '__main__':
    # Add test users
    db.session.add(models.User(username='username1', password='password'))
    db.session.add(models.User(username='username2', password='password'))
    db.session.add(models.User(username='username3', password='password'))
    db.session.add(models.User(username='username4', password='password'))
    db.session.add(models.User(username='username5', password='password'))
    db.session.commit()
    # Add test posts
    allUsers = models.User.query.all()
    for usr in allUsers:
        for i in range(1, 4, 1):
            db.session.add(models.Post(title=('Test Post ' + str(i)), body='This is a generated post', author=usr))
    db.session.commit()
