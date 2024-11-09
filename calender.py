from flask import Flask, render_template, session, request

app = Flask(__name__)

@app.route("/")
def index():
    # Some sort of thing that sends you to the login route if you 
    if not session["username"]:
        #Something that sends you to the login page
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
