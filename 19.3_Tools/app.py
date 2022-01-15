from source import *
from flask import redirect, flash, jsonify

################ Redirecting #####################

# Import redirect from flask, and pass it a page;

@app.route('/old-landing-page')
def sample_redirect():
  return redirect('/');
  
# By default the debugger will intercept this -> helpful for debugs;
# to stop debug toolbar from intercepting we can add:
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False;

# NOTE pretend this a database
MOVIES = ['Amadeus', 'Troy', 'Karate Kid']


@app.route('/movies')
def show_all_movies():
  '''Show list of all movies in fake db'''
  return render_template('get_movies.html', movies=MOVIES)

@app.route('/movies/new', methods=["POST"])
def add_movie():
  # remember request is provided by flask
  title = request.form['title']
  #Add to pretend DB
  if title in MOVIES:
    # WE can customize flash msgs by passing in catagories:
    flash('Movie already exists!', 'err')
      # We then pass with_categories=true to get_flashed_messages();
      # check base.html line 17
  else:
    MOVIES.append(title)
    # WE can customize flash msgs by passing in catagories:
    flash(f'''{title} added to movie list!''', 'success');
  
  # We COULD just rerender the template at this point:

    # return render_template('movies.html', movies=MOVIES)
  
  # The problem is, each time we refresh, we will resubmit the movie; 
  # Instead of returning the same template at movies, we should return the route to moves:
  return redirect('/movies')
  
@app.route('/movies/json')
def show_movie_json():
  # Problem: response header often mislabels json content-type as text/html
  # NOTE we need to pass a header to label our JSON as such;
  # Flask has a built in func jsonify() which will set this header for us;
  # Does not work on sets
  json_res = jsonify(MOVIES)
  return json_res

