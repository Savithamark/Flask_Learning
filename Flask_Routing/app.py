from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      user2 = request.form['ss']
      return redirect(url_for('success',name = str(user+" "+user2)))
   else:
      return redirect(url_for('success',name = "shawn"))

if __name__ == '__main__':
   app.run(debug = True)