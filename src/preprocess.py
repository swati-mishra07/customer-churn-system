import pandas as pd

def clean_data(df):
    df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1, errors='ignore')
    return df


def encode_data(df):
    df = pd.get_dummies(df, drop_first=True)
    return df