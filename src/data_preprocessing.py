import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess_data(data):
    data = data.dropna(subset=['Text Response'])
    data['Text Response'] = data['Text Response'].str.lower()
    data = data.drop_duplicates(subset=['Text Response'])
    return data