from flask import Flask, make_response, request
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    headers = {"Content-Type": "application/json"}
    return make_response('it is Wonderful', 200, headers)

if __name__ == '__main__':
   app.run(debug = True)