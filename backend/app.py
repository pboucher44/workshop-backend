#from word_prediction import get_prediction
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_word():
    return "hello - word"


@app.route('/api/create/', methods=['POST'])
def create():
    nbMot = request.args.get('nbMot', None)
    text = request.args.get('text', None)
    #get_prediction(nbMot, text)
    print (text)
    return 'success', 200

app.run()
