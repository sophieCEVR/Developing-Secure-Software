# Main file to run blogsite
# Database can be viewed here: https://inloop.github.io/sqlite-viewer/

from blogsite import app  # import the app object from blogsite package

# run the blogsite app
if __name__ == '__main__':
    print(app.config)
    app.run(ssl_context='adhoc')
