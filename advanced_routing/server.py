# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
    first = request.form['first_name']
    last = request.form['last_name']
    password = request.form['pass']
    pass_confirm = request.form['pass_confirm']
    if not first.isalpha():
        flash('Only letters!', 'first_req')
    if not last.isalpha():
        flash('Only letters!', 'last_req')
    if len(request.form['pass']) < 9:
        flash("More than 8 characters!", "pass")
    if password != pass_confirm:
        flash('Passwords must match', 'match')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", "email")
    else:
        flash("Success!")
    return redirect('/')
app.run(debug=True)
