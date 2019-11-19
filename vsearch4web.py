from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'
@app.route('/search4')
def do_search() -> str:
    return str(set('life, the universe, and everything').intersection(set('eiru,!')))
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                            the_title='Welcome to search4letters on the web!')
app.run(debug=True)
