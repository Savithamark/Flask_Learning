from flask import Flask, Markup
app = Flask(__name__)

@app.route("/")

def hello():
    return Markup("<h1>Hello Python!</h1>") # Markup allows us to return an HTML page by rendering a string as HTML:

if __name__ == '__main__':
   app.run(debug = True)