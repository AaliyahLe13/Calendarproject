from flask import Flask, render_template, session, request, redirect
import smtplib, ssl
from email.mime.text import MIMEText
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

#Configs database
PASSWORD ="Hello123"
PUBLIC_IP_ADDRESS = "34.71.116.70"
DBNAME = "trial.db"
PROJECT_ID = "Hack-K-State"
INSTANCE_NAME = "teamrocks"
app.config["SECRET_KEY"] = "something something something something"
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
 
#db = SQLAlchemy(app)

# The main route, which is the To Do list
@app.route("/")
def index():
    # Checks if the user is logged in 
    if "username" not in session:
        return redirect("/login")
    if request.method == "GET":
        # TODO: Query database, send info to todo page
        return render_template("calendar.html")
    if request.method == "POST":
        # Something
        return 404
    
# The login page route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        session.clear()
        return render_template("login.html")
    if request.method == "POST":
        # TODO: Check username and password
        username = request.form.get("usename")
        password = request.form.get("password")
        if username and password:
            session["username"] = username
            return redirect("/")
        else:
            return render_template("login.html", warning = "Please provide a username and password!")

# The route for creating a new user
@app.route("/register", methods=["GET", "POST"])
def new_user():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        password = request.form.get("password")
        confirmation = request.form.get("password")
        # Check username doesn't already exist
        # Check password is long enough
        if len(password) < 9:
            return render_template("login.html", warning = "Password must be 8 characters long.")
         # Check password and conformation are right
        if password != confirmation:
            return render_template("login.html", warning = "Password and confirmation do not match.")
        # Sends an email confirmation message formatted with HTML
        message = MIMEMultipart("alternative")
        message["Subject"] = "Calender - Password Confirmation"
        message["From"] = "Some email address" # Some sort of email address for our website - make google account
        message["To"] = request.form("email")
        # Alternate text in case the HTML won't go through
        text = """\\Here is your email confirmation link - link."""
        # HTML email content
        html = """\\
        <html>
          <body>
            <p>Hi,<br>
               Here's your email confirmation link<br>
               <a href="#">Confirm email</a> 
            </p>
          </body>
        </html>
        """
        plaintext = MIMEText(text, "plain")
        html = MIMEText(html, "html")
        # Adds message to email message that will be sent. Will try to render HTML first, then plaintext if unsuccessful
        message.attach(plaintext)
        message.attach(html)
        
        # Sends email over secure connection
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
            server.login()#Our email, #The password)
            server.sendmail()#Our email, message.email, message.as_string())
                
        return render_template("login.html", success="Thanks for registering!")

# The route for the weekly calender
@app.route("/calander")
def calendar():
    # Redirects you to the login if you are not logged in 
    if "username" not in session:
        return redirect("/login")        
    else:
    # Some sort of thing that sends you to week view
        return render_template("calendar.html")

# The route for if the user is logging out
@app.route("/logout")
def logout():
    # Clears the session and redirects you to the login
    session.clear()
    return redirect("/login")

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
