from flask import Flask, make_response, request, jsonify
'''make_response has a number of uses, the most notable of which is to serve a response 
in the form of a JSON object. 
If our application is an API, we'd return a response objects instead of pages:'''


app = Flask(__name__)

@app.route("/test", methods=['GET'])
def hello():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    my_dict = {'key': 'dictionary value'}
    headers = {"Content-Type": "application/json"}
    return make_response(jsonify(my_dict), 200, headers)

    
if __name__ == '__main__':
   app.run(debug = True)