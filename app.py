from flask import Flask, url_for
from markupsafe import escape

#create an instance of class Flask
#The first argument is the name of the application’s module or package (i.e. __name__ here)
app = Flask(__name__)  #so that Flask knows where to look for resources such as templates and static files

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

#URL Building
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))