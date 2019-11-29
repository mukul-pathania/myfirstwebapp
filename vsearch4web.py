from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello world from Flask!'
@app.route('/search4', methods = ["POST","GET"])
def do_search():
    return str(set(request.form["phrase"]).intersection(set(request.form["letters"])))
@app.route('/entry')
def entry_page():
    return render_template('entry.html',
                            the_title='Welcome to search4letters on the web!')
app.run(debug=True)
