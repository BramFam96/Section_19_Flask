# Import flask like any other installed lib:

from flask import Flask, request;

# Instantiate a new application object:
app = Flask(__name__);

@app.route('/welcome')
# Py looks for initial func called a view:
def welcome_page():
# view is automatically called at this route
# return creates the response -> a string of dynamic HTML
    '''routes to welcome page'''
  
    html = '''
    <html>
        <body>
            <h1>Welcome</h1>
        </body>
    </html>'''
    return html;


@app.route('/welcome/<sub>')
def welcome_sub_page(sub):
    SUB = {
        'home': 'Welcome home',
        'back': 'Welcome back'
    }
    page = SUB[sub]
    return f'''
        <html>
        <body>
            <h1>{page}</h1>    
        </body>
    </html>
    '''