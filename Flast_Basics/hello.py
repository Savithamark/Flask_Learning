from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__) # Flask creates an object which refer to the entire app


@app.route('/')
def hello():
    return "Hello World!"
if __name__ == '__main__':
   app.run(debug = True)
   
'''when we configure the variable app, we’re configuring the way our
 entire application works. For example, setting app = Flask() can accept a few attributes:'''
 
# app = Flask(__name__,
#             instance_relative_config=False,
#             template_folder="templates",
#             static_folder="static")

''' the commented code shows an example of creating a Flask app with a few specifics: 
the location of our config file, the folder in which we'll store pages templates,
 and the folder in which we'll
 store frontend assets (JS, CSS, images, etc.).'''