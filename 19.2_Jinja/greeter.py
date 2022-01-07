from source import *;
# NOTE Greeter pt 1 NOTE #

# Create a form route for accepting usernames
@app.route('/form')
def show_form():
  return render_template('form.html')

COMPLIMENTS = ['cool', 'suave', 'tenacious', 'awesome']
IDIOMS = ['cat', 'dawg','dude']

@app.route('/greet')
def greet():
  # We want to extract the input from /form:
  # Simply grab username, and pass it into our render
  username = request.args['username']
  compliment = choice(COMPLIMENTS);
  idiom = choice(IDIOMS);
  return render_template('greetings.html', username=username, compliment=compliment, idiom= idiom);
# NOTE Greeter pt 2 NOTE #
# We want to add the option to select multiple compliments;
# Selecting multiple compliments should elicit 3 randon compliments from the list abv.

@app.route('/form-2')
def show_form2():
  return render_template('form_2.html')

@app.route('/greet-2')
def greet_2():
  # We want to extract the input from /form:
  # Simply grab username, and pass it into our render
  username = request.args['username']
  compliment = choice(COMPLIMENTS);
  idiom = choice(IDIOMS);
  
  more_compliments = request.args.get('more_compliments')
  compliments = sample(COMPLIMENTS, 3)
  return render_template('greetings_2.html', compliments= compliments, more_compliments=more_compliments, username=username, compliment=compliment, idiom= idiom);