from flask import Flask, make_response, request, jsonify
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    if request.method != 'GET':
        return make_response('Information request', 400)
    my_dict = {'fruit': 'apple'}
    headers = {"Content-Type": "application/json"}
    return make_response(jsonify(my_dict), 200, headers)

if __name__ == '__main__':
   app.run(debug = True)