# NOTE routing is importing the config file
from routing import *

# Query Strings:

 # POST requests are typically generated from form responses;
 # Form responses are converted to query strings in our route
 # Writing POSTs thus reqs that we know how to access query strings
 # from our GET routes;

# query routes look like:

 # /route?q=value&param1=value&*etc;
 # /videos?q=soccer&sort=most_viewed 

#Our server will want something like:  
      #q: soccer sort:most_viewed 
# To get this flask provides a request object:
# from flask import Flask, request; 
@app.route('/search')
def search():
    '''Handle GET request like: 
    /search?q=value&sort=new&filter=recommended'''
#The request obj the url string; 
# request.args is a dict like obj of query params:
    print(request.args);
# Access individual values like any other dict:
    q = request.args['q'];
    sort = request.args['sort']
    filter = request.args['filter']
    return f'''
    <h1>Querying for:{q}</h1>
    <p>Sorting by: {sort}</p>
    <p>Filtering by: {filter}</p>
    '''
# NOTE these params must be passed, extras will be ignored;