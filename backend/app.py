#from word_prediction import get_prediction
from flask import Flask, request
from flask import json

app = Flask(__name__)

@app.route('/')
def hello_word():
    return "hello - word"


@app.route('/api/create/', methods=['POST'])
def createWithPost():
    nbMot = request.args.get('nb', None)
    text = request.args.get('text', None)
    data = []
    for i in range(int(nbMot)):
        data.append(text)

    response = app.response_class(
        response= json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    #return  get_prediction(nbMot, text)
    return response

@app.route('/api/create/', methods=['GET'])
def createWithGet():
    nbMot = request.args.get('nb', None)
    text = request.args.get('text', None)
    print (nbMot)
    #return  get_prediction(nbMot, text)
    return 'success', 200

#app.run()
