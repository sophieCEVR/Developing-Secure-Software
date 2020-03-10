# README #

### Developing Secure Software Coursework ###

* Quick summary

Repository for Developing Secure Software Coursework at University of East Anglia. 
Students working on this project are : 
    
    Danny Booty
    Justin Nuttall
    Jack Hilsdon
    Sophie Rollo

### How do I get set up? ###

* Development Settings
    
  <p>
  The program was developed in PyCharm and these directions for installation will be written with the intention of the PyCharm development environment being used to run them.
  <br>
  Please ensure you have Python3.8 installed to run this project. 
  You can find that here: https://www.python.org/downloads/release/python-380/
  </p>
* Requirements
<br>
    Run requirements.txt to install all necessary requirements, PyCharm should prompt you to do this.
     
    * Flask
    * SQLAlchemy
    * WTForms 
    * pyopenssl
    * Flask-Mail
    <br>
    
    If PyCharm does not provide this prompt, or if you are using a different IDE, 
    the following commands will install the dependencies also.
    
    Navigate to the command line by searching for `GitBash` or any other command line terminal program. 
    (`Terminal` should be pre-installed on MacOS).
     Within the command line, navigate into the base folder of the project. 
     <br>You should be able to run the command `pip install requirements.txt` command and force the IDE to install all the 
     dependencies from requirements.txt, however if that does not work;
    write each line from the below section into the terminal, then press the enter key to run the installation.
    
    ```
        pip install Flask
        pip install sqlalchemy 
        pip install Flask-WTF
        pip install pyopenssl
        pip install Flask-Mail
    ```
    You should now have all the dependencies installed for the project. 
    If you have any issues please contact one of the creators of the project or the module organiser `Oliver Buckley`.
    
* Database configuration
    * The Database is an sqlite database
    * Database location is blogsite/blogsiteDatabase.db
    * You can view the database file online: https://inloop.github.io/sqlite-viewer/
        * Click the big box on the page and navigate to blogsite/blogsiteDatabase.db to open it.
    * To configure the database, first run create_database.py. (In PyCharm press the play button next to the method name)
        * This will create the database.
    * To then populate the database with dummy users, run populate_database.py. 
        * This populates the database with some test data, it is recommended to run this after create_database.py
    * If an error occurs when creating or populating the database, delete the database and retry 

### Who do I talk to? ###

* Any member of the development team.
* Module organiser, Oliver Buckley.
