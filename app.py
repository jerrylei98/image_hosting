from flask import Flask, render_template, session, request, redirect
from utils import *

app = Flask(__name__)
app.secret_key = 'thequickbrownfoxjumpsoverthetwolazydogs'

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
