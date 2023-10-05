
from flask import Flask, request, render_template, redirect

app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def login():
    if request.method == "POST":
        if request.form['user'] == 'ari' and request.form['pw'] == 'ari':
                return redirect('/access')
        else:
            return redirect('/')
    else:
        return render_template('login.html')

    
@app.route('/access')
def access():
    return render_template('access.html')
