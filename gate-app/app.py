from flask import Flask, request, render_template, redirect
app = Flask(__name__)
from modules.authorize import authenticate
from modules.open_gate import open

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == "POST":
        if authenticate(request.form['user'],request.form['pw']):
            return redirect('access')
        else:
            return redirect('/')
    else:
        return render_template('login.html')

    
@app.route('/access')
def access():
    return render_template('access.html')


@app.route('/open_gate')
def open_gate():
    res = open()
    if res == 1:
        result = 'succses'
    else:
        result = 'fail'

    return {'result': result};


# what are the pssible states the user can be in.
'''
state machinee concept
not logged in
logged in
token exprired
tokec authorized

'''
