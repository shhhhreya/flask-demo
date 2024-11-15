from flask import Flask

#create an instance of class Flask
#The first argument is the name of the application’s module or package (i.e. __name__ here)
app = Flask(__name__)  #so that Flask knows where to look for resources such as templates and static files

@app.route('/')  
def hello():
    return "Hello World!" # can render html as well inside quotes

if __name__ == "__main__":
    app.run(debug=True)