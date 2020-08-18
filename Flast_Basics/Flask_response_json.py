from flask import Flask, make_response
'''make_response has a number of uses, the most notable of which is to serve a response 
in the form of a JSON object. 
If our application is an API, we'd return a response objects instead of pages:'''


app = Flask(__name__)

@app.route("/")
def json_object():
    headers = {"Content-Type": "application/json"}
    return make_response('it worked!', 200, headers)

if __name__ == '__main__':
   app.run(debug = True)