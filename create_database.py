# File to create the database - run this when models.py is updated - delete database to create from scratch
# Database can be viewed here: https://inloop.github.io/sqlite-viewer/

from blogsite import db  # import the db object from the blogsite package

if __name__ == '__main__':
    db.create_all()  # create all the database components
