# Imports:

from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def ask_questions():
    """Generate and show word form."""

    prompts = story.prompts

    return render_template("home.html", prompts=prompts)


@app.route("/madlib")
def show_story():
    """Show story result."""
    
    text = story.generate(request.args);

    return render_template("madlib.html", text=text)
