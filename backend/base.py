from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
api = Flask(__name__)
cors = CORS(api)
api.config['CORS_HEADERS'] = 'Content-Type'

@api.route('/')
@cross_origin()
def home():
    return "home page"

@api.route('/response', methods=['GET'])
def response():
    if request.method == 'GET':

        #if request.args.get('userInput') == 'Hello':
        return jsonify({'response': 'Hello yo yo yo yo '})

    return "response page"
