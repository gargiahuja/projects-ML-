# utils/disease_model.py
import pandas as pd
import joblib
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer


def train_model(csv_path='data/dataset.csv', model_path='model/disease_model.pkl'):
    import os
    os.makedirs(os.path.dirname(model_path), exist_ok=True)

    df = pd.read_csv(csv_path)
    print("CSV loaded successfully")

    symptom_cols = [f"Symptom_{i}" for i in range(1, 18)]
    df[symptom_cols] = df[symptom_cols].fillna('')  # Replace NaNs with empty string
    df["Combined_Symptoms"] = df[symptom_cols].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)

    X = df["Combined_Symptoms"]
    y = df["Disease"]

    print("Training model...")
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(X, y)

    joblib.dump(model, model_path)
    print(f"Model saved at: {model_path}")



def predict_disease(symptoms, model_path='models/disease_model.pkl'):
    model = joblib.load(model_path)
    return model.predict([symptoms])[0]

if __name__ == "__main__":
    train_model()
    print("Model training complete and saved successfully!")

