from flask import Flask, render_template, session, request

app = Flask(__name__)

@app.route("/")
def index():
    # Some sort of thing that sends you to the login route if you 
    if not session["username"]:
        #Something that sends you to the login page
    if request.method == "GET":
        # Something that gets information from database and sends it to the calendar
        return render_template("todo.html")
    if request.method == "POST":
        # Something that adds an item to the database
        return render_template("todo.html") # Probably will send some sort of "complete!" message
    

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

@app.route("/new-user", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("new-user.html")
    if request.method == "POST":
        # Check username doesn't already exist
        # Check password is long enough
        # Check passoword and conformation are right
        # Email confirmation send
        session["username"] = "username" # Replace with real username
        return render_template("index.html")
        # If invalid
        return render_template("login.html", warning = "Invalid username or password")

@app.route("/calander")
def index():
    # Some sort of thing that sends you to the login route if you
    if not session["username"]:
        #Something that sends you to the login page
    else:
    # Some sort of thing that sends you to week view
        return render_template("calendar.html")
