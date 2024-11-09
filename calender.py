from flask import Flask, render_template, session, request

app = Flask(__name__)

@app.route("/")
def index():
    session['email'] = request.form['email_address']
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        # Check username and password
        # If valid
        session["username"] = "username" # Replace with real username
        return render_template("index.html")
        # If invalid
        return render_template("login.html", warning = "Invalid username or password")
