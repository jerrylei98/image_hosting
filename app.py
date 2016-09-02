from flask import Flask, render_template, session, request, redirect
from utils import *

app = Flask(__name__)
app.secret_key = 'thequickbrownfoxjumpsoverthetwolazydogs'

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        if session.get('username') != None: #if already logged in, go straight to browsing
            return redirect('/browse')
        else:
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
            #print "HERE"
            uname = request.form.get('usernameSignup')
            pword = request.form.get('passwordSignup')
            email = request.form.get('emailSignup')
            if create_user(uname,pword,email):
                session['username'] = uname
                return redirect('/browse')
        if button == "Browse Anonymously":
            session['username'] = None
            return redirect('/browse')
        return redirect('/')

@app.route("/profile")
@app.route("/profile/<profile_user>", methods=["GET", "POST"])
def profile(profile_user = ''):
    if request.method == "GET":
        if len(profile_user) == 0: #if trying '/profile'
            return redirect('/browse')
        else:
            if check_user_exists(profile_user):
                if session.get('username') == profile_user: #logged in and accessing own profile
                    return render_template("profile.html", username=session.get("username"), allow_profile=True, profile_exists=True)
                else: #not logged in accessing another profile
                    return render_template("profile.html", username=session.get("username"), allow_profile=False, profile_exists=True)
            else: #throw error to show profile does not exist
                return render_template("profile.html", username=session.get("username"), allow_profile=False, profile_exists=False)

@app.route("/browse")
def browse():
    return render_template("browse.html", username=session.get("username"))

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html", username=session.get("username"))

@app.route("/logout")
def logout():
    session['username'] = None
    return redirect('/')


if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
