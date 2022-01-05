# Jinja can dynamically render variables in our templates;

# This can be any text wrapped in double curly brackets: {{}}
# It works almost exactly like f strings;

# NOTE These examples involve editing template files, and routingh in template_intro;
# The following is integrated into other files, but paths and code are included here
    # Routing for first example: 
# Template found at templates/maths.html;
# @app.route('/maths')
# def random_add():

   # Flask does not simply serve a file 
   # It also reads over the file for python code;
   # Define dynamic variables here in the view

#   a = randint(1,100)
#   b =randint(1,100)

#  Pass variables into render func:

  #  return render_template('maths.html', a = a, b = b);
  

# templates/random_maths.html
