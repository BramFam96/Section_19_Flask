# Getting started:

# Import flask like any other installed lib:

from flask import Flask;

# Instantiate a new application object:
app = Flask(__name__);
# Does NOT execute like a normal py file.
# NOTE in command line:
    # flask run -> not python3 or %run;
    # Console logs server params:

    #* Enivornment:production
    #* Running on ....
    #* Debug mode :off;


# NOTE flask run defaults to app.py in our current directory;
    
    # Change this behavior with FLASK_APP
    
    # FLASK_APP=filename.py flask run
    
        #FLASK_APP is an env variable 

# NOTE Enivornment and Debug mode are also env vars we should adjust;
# FLASK_ENV=development flask run
    
    # * Environment: development
    # * Debug mode: on
    # * Running on ...
    # * Restarting with stat
    # * Debugger is active!
    # * Debugger PIN: ...

# Now we have debugging and auto reload!

# Setting FLASK_ENV each time can be tedious.
# Instead we can set our default environment to development;
# To do this run export FLASK_ENV=development; 

# NOTE this is not permanent! It will revert when the window closes;

# The best solution for permanately changing our default env
# is to configure it in our bash profile.
# cd $ -> ls -a -> code .profile -> add export FLASK_ENV...