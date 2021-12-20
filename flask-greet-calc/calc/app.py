# Put your app in here.

from flask import Flask, request;
from operations import *

# Instantiate a new application object:
app = Flask(__name__);

@app.route('/add')
def add_nums():
    
    a= int(request.args.get('a'))
    b= int(request.args.get('b'))

    return str(add(a,b))
    
@app.route('/sub')
def sub_nums():
    
    a= int(request.args.get('a'))
    b= int(request.args.get('b'))

    return str(sub(a,b))
    
@app.route('/mult')
def mult_nums():
    
    a= int(request.args.get('a'))
    b= int(request.args.get('b'))

    return str(mult(a,b))
    
@app.route('/div')
def div_nums():
    
    a= int(request.args.get('a'))
    b= int(request.args.get('b'))

    return str(div(a,b))
    

@app.route('/math/<operation>')
def do_maths(operation):
    '''Handle GET request like: 
    /search?a=num&b=num'''
   
    OPERATIONS = {
        'add':add,
        'sub':sub,
        'mult':mult,
        'div':div
    }
    
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))


    return str(OPERATIONS[operation](a,b));
