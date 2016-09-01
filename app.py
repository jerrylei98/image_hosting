from flask import Flask, render_template, session, request, redirect
from utils import *

app = Flask(__name__)
app.secret_key = 'thequickbrownfoxjumpsoverthetwolazydogs'

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        button = request.form['button']
        if button == "Log In":
            #print "LOGINHERE"
            uname = request.form.get('usernameLogin')
            pword = request.form.get('passwordLogin')
            if check_user(uname,pword): #if authentication works, user is directed to browse
                session['username'] = uname
                return redirect('/browse')
        if button == "Sign Up":
            print "HERE"
            uname = request.form.get('usernameSignup')
            pword = request.form.get('passwordSignup')
            email = request.form.get('emailSignup')
            if create_user(uname,pword,email):
                session['username'] = uname
                return redirect('/browse')
        return redirect('/')

@app.route("/browse")
def browse():
    return "hello"

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
