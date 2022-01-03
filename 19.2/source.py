# Import flask
# Include render_template to serve files:
from flask import Flask, request, render_template
# Import debug toolbar:
from flask_debugtoolbar import DebugToolbarExtension;
from random import randint, choice, sample;

app = Flask(__name__);

# Config and init toolbar:
app.config['SECRET_KEY'] = 'something';
# TODO Env variables
debug = DebugToolbarExtension(app);
