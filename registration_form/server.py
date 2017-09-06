from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/users', methods=['Post'])
def process():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    text = request.form['text']
    if len(request.form['name']) < 1:
        flash("Must contain between 1 and 120 characters")
        return redirect('/')
    elif len(request.form['text']) > 120:
        flash("Must contain between 1 and 120 characters")
        return redirect('/')
    else:
        # flash("Success!") # display success message
        return render_template('result.html', name=name, location=location, language=language, text=text)

app.run(debug=True)
