# Library imports
import pandas as pd
import numpy as np
import spacy
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import joblib
import string
from spacy.lang.en.stop_words import STOP_WORDS
from flask import Flask, request, jsonify, render_template
import nltk

# Load trained Pipeline
model = joblib.load('c2_SentimentAnalysis_Model_Pipeline.pkl')

stopwords = list(STOP_WORDS)

# Create the app object
app = Flask(__name__)


# creating a function for data cleaning



# Define predict function
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    new_comment = [str(x) for x in request.form.values()]
#     data = pd.DataFrame(new_comment)
#     data.columns = ['new_comment']

    predictions = model.predict(new_comment)[0]
    if predictions==0:
        return render_template('index.html', prediction_text='Negative')
    if predictions==1:
        return render_template('index.html', prediction_text='Neutral')
    else:
        return render_template('index.html', prediction_text='Positive')


if __name__ == "__main__":
    app.run(debug=True)
