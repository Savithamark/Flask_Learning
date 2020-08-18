from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")

@app.route("/")
def info():
    return render_template("info.html") #return_template will return an HTML page by finding the page in our /templates folder:

from flask import Flask, render_template

if __name__ == '__main__':
   app.run(debug = True)