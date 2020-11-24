#from word_prediction import launch
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_word():
    return "hello - word"

@app.route('/test')
def test():
    return 'launch()'

@app.route('/api/create/', methods=['POST'])
def foo():
    nbMot = request.args.get('nbMot', None)
    text = request.args.get('text', None)
    #bar = request.args.to_dict()
    #launch(nbMot, text)
    print (text)
    return 'success', 200

app.run()
