#from word_prediction import get_prediction
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_word():
    return "hello - word"


@app.route('/api/create/', methods=['POST'])
def createWithPost():
    nbMot = request.args.get('nb', None)
    text = request.args.get('text', None)
    print (text)
    #return  get_prediction(nbMot, text)
    return 'success', 200

@app.route('/api/create/', methods=['GET'])
def createWithGet():
    nbMot = request.args.get('nb', None)
    text = request.args.get('text', None)
    print (nbMot)
    #return  get_prediction(nbMot, text)
    return 'success', 200

#app.run()
