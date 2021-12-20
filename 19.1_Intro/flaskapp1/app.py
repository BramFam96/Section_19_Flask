from querystring import *

#  POST Requests:

    # By defualt routes only respond to GET requests;
    # To accept POST reqs, we must pass:
        #   methods=['POST']
    # To our app.route decorator;
@app.route('/test')
# # methods is a list and can accept multiple HTTP verbs:
#     # methods=['POST','GET'];
#     # Including GET will cause the view to render in both scenarios
#     # Typically we do not want this and will seperate POST from GET;
def post_demo():
    return "You've sent a post request!";
# Going to this page returns an invalid method response;
# How to actually send the post req?
# We can use something like curl:
    # curl -X POST localurl/test;

# Typically POSTs are made by form submission:
# Start with a GET route and serve a form with method="POST"
# Make a new POST route like we did above:
@app.route('/add-comment')
def add_comment_page():
    return '''
    <form method="POST">
        <input type='text' name='comment' placeholder='comment'>
        <input type='text' name = 'user' placeholder='username'> 
        <button>Add</button>
    </form>
    '''
# NOTE on submit forms run a get req and refresh the page;
# method='POST' changes this to a post req and refresh;
@app.route('/add-comment', methods=['POST'])
def show_comment():
    # on form submission request.form is populated:
    # print(request.form)
    # Access the input value by its name: 'comment'
    comment = request.form['comment']
    user = request.form['user']
    # comment = request.form['comment'];
    return f'''
    <h1>New comment received from {user}!</h1>
    <p>{user}:{comment}</p>'''
# TODO save this data in a database;


