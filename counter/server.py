from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSOOSecret'

def session_counter():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1

@app.route('/')
def index():
    session_counter()
    return render_template("index.html", session=session)
app.run(debug=True)
