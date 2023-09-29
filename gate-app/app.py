
from flask import Flask, request, render_template



app = Flask(__name__)


# view function
# @ indicates a python decorator 
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/access')
def access():
    return render_template('access.html')

# to access query strings we need to import request.
# query strings stored in request object in request.args(dictionary like object)
