# README #

### Developing Secure Software Coursework ###

* Quick summary

Repository for Developing Secure Software Coursework at University of East Anglia. 
Students working on this project are : 
    
    Danny Booty
    Justin Nuttall
    Jack Hilsdon
    Sophie Rollo

## How do I get set up? ##

Notes on running
* When creating a new user or updating your password, you will need to verify via an email link so please don't use a 
dummy email to create an account. 
* As the website is ran locally, you will need to click the email links on the same machine that the website is 
running on. It will not work on a separate device.
#### Development Settings ####
    
  The program was developed in PyCharm and these directions for installation will be written with the intention of 
  the PyCharm development environment being used to run them.
  
  
  Please ensure you have Python3.8 installed to run this project. 
  You can find that here: https://www.python.org/downloads/release/python-380/
  
  You must also ensure that your project interpreter is correctly set up to Python if using PyCharm. 
  This may require you to delete the virtual environment and recreate it. 
  Steps on how to do this are under the `Virtual Environment` section.

#### Requirements ####
Run requirements.txt to install all necessary requirements, PyCharm should prompt you to do this.
* Flask
* SQLAlchemy
* WTForms 
* pyopenssl
* Flask-Mail
    
If PyCharm does not provide this prompt, or if you are using a different IDE, 
the following commands will install the dependencies also.
    
Navigate to the command line by searching for `GitBash` or any other command line terminal program. 
(`Terminal` should be pre-installed if on MacOS).
Within the command line, navigate into the base folder of the project. 

You should be able to run the command `pip install requirements.txt` command and force the IDE to install all the 
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
 
## Optional Steps ##
After completing the above steps, you should be able to run the program using the existing database. 
However, if you want to start with a fresh database, follow the steps under Database Configuration. 
There are also steps for setting up a virtual environment if that is required.
If you have any issues please contact one of the creators of the project or the module organiser `Oliver Buckley`.
    
### Database ###

   * The Database is an sqlite database
   * Database location is blogsite/blogsiteDatabase.db
   * You can view the database file online: https://inloop.github.io/sqlite-viewer/
        * Click the big box on the page and navigate to blogsite/blogsiteDatabase.db to open it.
   
#### How to Set-up ####
To configure the database, first run create_database.py. (In PyCharm press the play button next to the method name). 
This will create an empty database.

To then populate the database with dummy users, run populate_database.py. 
This populates the database with some test data, it is recommended to run this after create_database.py

If an error occurs when creating or populating the database, delete the database and retry 

### Virtual Environment ###
The code you have been sent will have a virtual environment in it, however you may have to delete this 
and create your own if there are issues in running it.

To do this, right click the `venv` folder in the project file structure, then select delete. 

Now, navigate to File ---> Settings, open the  `Project` tab on the left hand menu and select `Project Interpreter`.
It should say `<No intrepreter>` at the top of that section. Click the cog next to the project interpreter selection 
box and select `Add`. You will now have a window titled `Add Project Interpreter` pop up. 

On this window you want to select `Virtualenv Environment` on the left hand side, click the `New environment` radial
button, select the location you wish to store the virtual environment (We recommend you store it where you deleted the 
original venv folder from), select a base interpreter (Python 3.8 is our recommendation) then select OK.

If you try to save the virutal environment where one already exists, it will give you an error message and fail to 
create.

Press apply and OK, then your virtual environment should be set up.
### I still need help! Who can I talk to? ###

Any member of the development team.
    * Sophie jxy13mmu@uea.ac.uk
    * Jack zkv15bwu@uea.ac.uk
    * Danny d.booty@uea.ac.uk
    * Justin abe17tju@uea.ac.uk
    
Module organiser, Oliver Buckley.

### Bitbucket Project Location ###

You can find the project here: https://bitbucket.org/sophieR123/developing-secure-software/src/master/
It is currently set to private.