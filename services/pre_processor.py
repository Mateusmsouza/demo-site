import joblib
import re
import nltk
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

class PreProcessor:
  
  def __init__(self):
    nltk.download('rslp')
    self.stemmer = nltk.stem.RSLPStemmer()
  
  def process(self, text: str) -> str:
    """ execute part of pre processing manually as it's not native supported by
    CountVetorizer """
    text = re.sub(r'\d+', '', text)
    text = ' '.join([self.stemmer.stem(word) for word in text.split()])
    return text

  def create_tokenized_matrix(self, filename_list: list) -> pd.DataFrame:
    countVectorizer = joblib.load("resources/vectorizer.pkl")

    tokenizedMatrix = countVectorizer.transform(filename_list)
    
    data = np.array(tokenizedMatrix.todense())
    labels = np.array(countVectorizer.get_feature_names())

    return pd.DataFrame(data, columns=labels)
