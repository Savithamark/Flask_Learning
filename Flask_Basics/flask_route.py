from flask import Flask
from calc import square, addition, multiplication, subtraction, division
app = Flask(__name__)

@app.route("/add")
def add():
    add = addition(5,6) # passing parameter to addtion function written in calc.py which already imported
    return add

@app.route("/sub")
def sub():
    sub = subtraction(8,10)
    return sub

@app.route("/mul")
def mul():
    mult =  multiplication(4,7)
    return mult

@app.route("/div")
def div():
    d = division(4,7)
    return d

@app.route("/square")
def squ():
    s = square(7)
    return s

if __name__ == '__main__':
   app.run(debug = True)