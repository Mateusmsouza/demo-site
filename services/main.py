import joblib
import re
import nltk
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from services.pre_processor import PreProcessor

file_list = ['0-true.json']

def validate_news(news):
    with open('temp/news.json', 'w') as writer:
        writer.write(news.__str__())

    tokenized_matrix = PreProcessor().create_tokenized_matrix(
        filename_list=['temp/news.json']
    )
    
    model = joblib.load("resources/model.sav")
    prediction = model.predict(tokenized_matrix)

    return prediction
