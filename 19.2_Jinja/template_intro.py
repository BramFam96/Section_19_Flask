from source import *

# NOTE this is stil a routes file;
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

# Dynamic HTML:
    # call render_template(html file)
# Templating info

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/hello')
def hello_page():
  return render_template('hello.html')
    
@app.route('/maths')
def random_add():
  # Flask does not simply serve a file 
  # It also reads over the file for python code;
  # Define dynamic variables
  a = randint(1,5)
  b =randint(1,5)
  # Pass variables into render func:
  return render_template('maths.html', a = a, b = b)
  
@app.route('/spell/<word>')
def spell_word(word):
  return render_template('spell_word.html', word=word)
  