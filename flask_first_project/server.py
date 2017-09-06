from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/boats')
def boats():
    return "<h1>I guess I like boats</h1>"

app.run(debug=True)
