from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    dbconfig = { 'host': '127.0.0.1',
                 'user': 'vsearch',
                 'password': 'vsearchpasswd',
                 'database': 'vsearchlogDB', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log
           (phrase, letters, ip, browser_string, results)
            values
            (%s, %s, %s, %s, %s)"""
   
    cursor.execute(_SQL, (req.form['phrase'],
                   req.form['letters'],
                   req.remote_addr,
                   req.user_agent.browser,
                   res, ))
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/search4', methods = ["POST","GET"])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results =str(set(phrase).intersection(set(letters)))
    log_request(request,results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html',
                            the_title='Welcome to search4letters on the web!')
app.run(debug=True)
