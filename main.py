import joblib
import re
import nltk
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from services.pre_processor import PreProcessor

file_list = ['temp/news.json']

if __name__ == '__main__':
    tokenized_matrix = PreProcessor().create_tokenized_matrix(
        filename_list=file_list
    )

    model = joblib.load("resources/model.sav")
    prediction = model.predict(tokenized_matrix)
    
    result = 0

    if prediction[0] == 1:
        result = 1

    with open('temp/result.json', 'w') as writer:
        writer.write(result.__str__())

    
