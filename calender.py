from flask import Flask, render_template, session, request
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# The main route, which is the To Do list
@app.route("/")
def index():
    # Some sort of thing that sends you to the login route if you 
    if not session["username"]:
        #Something that sends you to the login page
    if request.method == "GET":
        # Something that gets information from database and sends it to the calendar
        return render_template("index.html")
    if request.method == "POST":
        # Something that adds an item to the database
        return render_template("index.html") # Probably will send some sort of "complete!" message
    
# The login page route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        # Check username and password
        # If valid and email confirmed
        session["username"] = "username" # Replace with real username
        return render_template("index.html")
        # If invalid (also send some sort of "resend link" message if email not confirmed
        return render_template("login.html", warning = "Invalid username or password")

# The route for creating a new user
@app.route("/new-user", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("new-user.html")
    if request.method == "POST":
        # Check username doesn't already exist
        # Check password is long enough
        # Check passoword and conformation are right
        # Sends an email confirmation message formatted with HTML
        message = MIMEMultipart("alternative")
        message["Subject"] = "Calender - Password Confirmation"
        message["From"] = # Some sort of email address for our website
        message["To"] = request.form(email)
        # Alternate text in case the HTML won't go through
        text = """\Here is your email confirmation link - link."""
        # HTML email content
        html = """\
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
            server.login(#Our email, #The password)
            server.sendmail(#Our email, message.email, message.as_string())
                
        return render_template("login.html") # Some sort of success message

# The route for the weekly calender
@app.route("/calander")
def index():
    # Some sort of thing that sends you to the login route if you
    if not session["username"]:
        #Something that sends you to the login page
    else:
    # Some sort of thing that sends you to week view
        return render_template("calendar.html")
