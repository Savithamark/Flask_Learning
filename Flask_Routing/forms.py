from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<fname>')
def success(name):
   return 'welcome %s' % fname 

@app.route('/form',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      userfirstname = request.form['fname']
      userlastname = request.form['fname']
      return redirect(url_for('success',name = userfirstname))
   else:
      userlastname = request.args.get('fname')
      return redirect(url_for('success',name = userfirstname))

if __name__ == '__main__':
   app.run(debug = True)