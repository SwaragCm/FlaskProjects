from flask import Flask,redirect,request,render_template
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

# @app.route('/path/<path:subpath>/home')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

@app.route('/')
def index():
    return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))


@app.route('/logger')
def index():
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return 'loggs'



@app.post("/login")
def do_the_login():
    if request.method == 'POST':
        usr = request.form['user']
        pwd = request.form['pwd']
        return ("congrats")
    return render_template('index.html')

@app.get('/log')
def login_get():
    return render_template('index.html')

# @app.post('/log')
# def login_post():
#     return do_the_login()




