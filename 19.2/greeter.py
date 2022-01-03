from source import *;
# Create a form route for accepting usernames
@app.route('/form')
def show_form():
  return render_template('form.html')

COMPLIMENTS = ['cool', 'suave', 'tenacious', 'awesome']
IDIOMS = ['cat', 'dawg','dude']

@app.route('/greetings')
def greet():
  # We want to extract the input from /form:
  # Simply grab username, and pass it into our render
  username = request.args['username']
  compliment = choice(COMPLIMENTS);
  idiom = choice(IDIOMS);
  return render_template('greetings.html', username=username, compliment=compliment, idiom= idiom);
