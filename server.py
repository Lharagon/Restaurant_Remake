from flask import Flask, render_template, request, flash, session
from flask_mail import Mail, Message
import re

mail = Mail()
app = Flask(__name__)

app.config.update(dict(
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'projects4port',
    MAIL_PASSWORD = 'systems11'
))

mail.init_app(app)
app.secret_key = '7d441f27d441f27567d441f2b6176aYes'

email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
first_re = re.compile(r'^[a-zA-Z]+$')
last_re = re.compile(r'^[a-zA-Z]+$')

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/blog')
def blog():
	return render_template("blog.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route('/process_contact', methods=["POST"])
def process():

	first = request.form['first_name']
	last = request.form['last_name']
	email_ti = request.form['email']
	subject = request.form['subject']
	message = request.form['message']

	good = True
	if len(first) < 1:
		flash("First Name cannot be blank!")
		good = False
	elif not first_re.match(first):
		flash("Invalid first Name")
		good = False
	
	if len(last) < 1:
		flash("Last Name cannot be blank!")
		good = False
	elif not last_re.match(last):
		flash("Invalid last Name")
		good = False

	if len(email_ti) < 1:
		flash("Email cannot be blank!")
		good = False
	elif not email_re.match(email_ti):
		flash("Not Valid Email")
		good = False

	if len(subject) < 1:
		flash("Please input something for the subject")
		good = False

	if len(message) < 1:
		flash("Please input something for the message")
		good = False

	if good:
		msg = Message( subject, sender=(first + " " + last, email_ti), recipients = ['projects4port@gmail.com'])
		msg.body = message 
		mail.send(msg)
		flash("Thank you for your Message")
		return render_template('contact.html')
	else:

		return render_template('contact.html')

app.run(debug=True)
