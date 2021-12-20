from querystring import *
# Variable Routing

    # Rather than hardcode our routes we can let flask dynamically
    # generate routes as based on variables we pass in;

# ie subreddits, users on fb, routes that are too numerous to code

# Basic Variable Route:

@app.route('/users/<user>')
# dynamic values go in <> like HTML;
# they can be anything and flask will generate the route
# we restrict this by comparing it to something like USERS abv;
# NOTE keyword args are automatically passed to the view func:
def show_profile(user):
    'Show user profile'
# Mock user storage:
    USERS = {
     'sonic': 'Sonic the Hedgehog',
     'tails': 'Tails the Fox'
    }
# NOTE view params must match keyword arg
    
# name is how we ensure our route only responds to known users;
    name = USERS.get(user, "User not found")
    return f"<h1>{name}'s Profile:</h1>"

# Variable routing with int in url:

@app.route('/posts/<int:id>')
# We've added int: to route b/c post ids are nums;
# This means posts/non-num will not even ping the route;
def show_posts(id):

    POSTS = {
        1: 'Python toimee',
        2: 'New notes on Flask',
        3: 'All that other jazz'
        }

    post = POSTS.get(id, 'Post not found')

    # NOTE this does not work!
    # Python turns nums in route to a string!
    # Must define int:id @ line 28

    return f"<h1>{post}</h1>"
