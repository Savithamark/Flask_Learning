from flask import Flask, make_response, request, jsonify
app = Flask(__name__)
@app.route("/test", methods=['GET'])
def hello():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    my_dict = {'key': 'dictionary value'}
    headers = {"Content-Type": "application/json"}
    res = make_response(jsonify(my_dict), 200, headers)
    res.mimetype = 'application/json'
    return res

if __name__ == '__main__':
   app.run(debug = True)