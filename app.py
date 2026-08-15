import flask, sqlite3

app = flask.Flask(__name__)

### FOR TASK 3.3 ###
@app.route('/')
def index():
    db = sqlite3.connect('sanitisers.db')

    #selecting all columns from the sanitisers table
    cursor = db.execute('''
        SELECT * FROM sanitisers
    ''')

    result = cursor.fetchall() #returns a list of tuples

    db.close()
    
    return flask.render_template('index.html', data=result)

    
### FOR TASK 3.4 ###

@app.route('/submit_form/', methods=['POST'])
def submit_form():
    data = flask.request.form #a dictionary containing all values input in the HTML form

    db = sqlite3.connect('sanitisers.db')

    #selecting all columns from the sanitisers table
    cursor = db.execute('''
        SELECT * FROM sanitisers
        WHERE active_ingredient = ?
    ''', (data['ingredient'], )) #note the single item tuple (xxx,)

    result = cursor.fetchall() #returns a list of tuples

    db.close()

    return flask.render_template('result.html', result = result)
    


### only for running on repl.it
app.run("0.0.0.0", 8080)

### for running on your local machine, use this
#app.run()

