# HTML Templating:
# Instead of returning HTML strings in line
# We can use Jinja to serve template files -> HTML, CSS, JS; 

# Templates:

    # Can produce HTML responses
    # Can dynamically create the structure of these responses;

        # can use variables passed from the view
        # can use conditional logic
        # can inherit other templates

# Jinja
    # Popular templating library included with flask;
    # Requires a templates folder in our current direct;
from flask import Flask, request, render_template
app = Flask(__name__);

@app.route('/hello')
def hello_page():
    return render_template('hello.html')