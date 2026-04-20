import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib

from preprocess import clean_data, encode_data
from features import create_features


def train_model():
    df = pd.read_csv('../data/Churn_Modelling.csv')

    df = clean_data(df)
    df = encode_data(df)
    df = create_features(df)

    X = df.drop('Exited', axis=1)
    y = df['Exited']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = XGBClassifier()
    model.fit(X_train, y_train)

    joblib.dump(model, '../models/churn_model.pkl')


if __name__ == "__main__":
    train_model()