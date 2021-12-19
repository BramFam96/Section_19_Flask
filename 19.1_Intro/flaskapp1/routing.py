from config import *
# NOTE Routing Section 

# Begin routes with @decorator -> like class methods
@app.route('/')
# Py looks for initial func called a view:
def home_view():
# view is automatically called at this route
# return creates the response -> a string of dynamic HTML
    '''routes '/' to welcome page'''
    #We could simply return some text: 
    # return 'Welcome!'
    # We can also respond with a basic HTML template:
    html = '''
    <html>
        <body>
            <h1>Home</h1>
            <p>Welcome, welcome!</p>
            <a href = '/about'>Check out the about page!</a>
        </body>
    </html>'''
    return html;


@app.route('/about')
def about_view():
    return '''
        <html>
        <body>
            <h1>About</h1>
            <p>Blah, blah</p>
            <a href = '/'>Back to the home page!</a>
        </body>
    </html>
    '''
# NOTE routes above are all GET requests
