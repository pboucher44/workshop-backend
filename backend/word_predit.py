# Importing the Libraries

import tensorflow as tf
from tensorflow.python.keras.models import load_model
import numpy as np
import pickle
import random

# Load the model and tokenizer

model = load_model('model/nextword1.h5')
tokenizer = pickle.load(open('tokens/tokenizer1.pkl', 'rb'))

def Predict_Next_Words(model, tokenizer, text):
    """
        In this function we are using the tokenizer and models trained
        and we are creating the sequence of the text entered and then
        using our model to predict and return the the predicted word.
    """
    for i in range(3):
        sequence = tokenizer.texts_to_sequences([text])[0]
        sequence = np.array(sequence)
        
        preds = model.predict_classes(sequence)
        predicted_word = ""
        
        for key, value in tokenizer.word_index.items():
            if value == preds:
                predicted_word = key
                break
        
        return predicted_word
def GenerateRandomWord():
    """
       Pick random word from dictionary
    """
    return random.choice(list(tokenizer.word_index.keys()))
 
"""
    We are testing our model and we will run the model
    until the user decides to stop the script.
    While the script is running we try and check if 
    the prediction can be made on the text. If no
    prediction can be made we just continue.
"""

nbOfWords = input("Nb mots: ")
text = input("Enter your line: ")
textFinal = text
for x in range(int(nbOfWords)): 
    if text == "stop the script":
        print("Ending The Program.....")
        break
    
    else:
        try:
            text = text.split(" ")
            text = text[-1]

            text = ''.join(text)
            predicted = (Predict_Next_Words(model, tokenizer, text))
            text = predicted
           
        except:
            predicted = ''
        if ' '+predicted+' ' in textFinal or predicted == '':

            text = text + ' ' + GenerateRandomWord()
      
        textFinal = textFinal + ' ' + text
textFinal = textFinal.split(" ")
count = 0;
textFinalEnForme = ""
for leText in textFinal:
  if count == 0:
    textFinalEnForme += ' '+'\n'+ (leText.capitalize())
    count = 8
  else :  
    textFinalEnForme += " "+leText
  count -= 1
print(textFinalEnForme)
