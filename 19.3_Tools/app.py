from source import *
from flask import redirect
# Redirecting
# Import redirect from flask, and pass it a page;
@app.route('/old-landing-page')
def sample_redirect():
  return redirect('/');