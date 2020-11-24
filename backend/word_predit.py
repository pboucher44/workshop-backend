# Importing the Libraries

from tensorflow.keras.models import load_model
import numpy as np
import pickle

model = load_model('/content/drive/My Drive/Colab Notebooks/nextword1.h5')
tokenizer = pickle.load(open('/Users/Marwane/Desktop/EPSI I2/Workshop/workshop-backend/tokenizer1.pkl', 'rb'))


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
        #         print(preds)
        predicted_word = ""

        for key, value in tokenizer.word_index.items():
            if value == preds:
                predicted_word = key
                break

        # print(predicted_word)
        return predicted_word


"""
    We are testing our model and we will run the model
    until the user decides to stop the script.
    While the script is running we try and check if 
    the prediction can be made on the text. If no
    prediction can be made we just continue.

"""

# text1 = "at the dull"
# text2 = "collection of textile"
# text3 = "what a strenuous"
# text4 = "stop the script"

def launch(text, nbOfWords):
    #nbOfWords = input("Nb mots: ")
    #text = input("Enter your line: ")
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
                textFinal = textFinal + ' ' + predicted
            except:
                continue
    print(textFinal)