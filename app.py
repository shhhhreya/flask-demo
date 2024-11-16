from flask import Flask
from markupsafe import escape

#create an instance of class Flask
#The first argument is the name of the application’s module or package (i.e. __name__ here)
app = Flask(__name__)  #so that Flask knows where to look for resources such as templates and static files

@app.route('/')  
def index():
    return "Index Page!" # can render html as well inside quotes

@app.route('/hello/<username>')
def hello(username):
    return f'Hello {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post id: {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'subpath: {escape(subpath)}'


if __name__ == "__main__":
    app.run(debug=True)