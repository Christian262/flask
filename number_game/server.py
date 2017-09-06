from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
# our index route will handle rendering our form
def winning_number():
    session['number'] = int(random.randrange(0,101))

@app.route('/')
def index():
    winning_number()
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess_number():
    guess = int(request.form['guess'])
    if guess < session['number']:
        print "Too low"
        return render_template('low.html')
    elif guess > session['number']:
        print "Too high"
        return render_template('high.html')
    else:
        print "You win!"
        return render_template('win.html')

app.run(debug=True)
