from fastapi import FastAPI
import joblib
import pandas as pd
import os

app = FastAPI()

# ===== Load paths safely =====
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, 'models', 'churn_model_v2.pkl')
scaler_path = os.path.join(BASE_DIR, 'models', 'scaler.pkl')
features_path = os.path.join(BASE_DIR, 'models', 'features.pkl')

# ===== Load model files =====
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)
features = joblib.load(features_path)

# ===== Home route =====
@app.get("/")
def home():
    return {"message": "Churn Prediction API Running 🚀"}

# ===== Prediction route =====
@app.post("/predict")
def predict(data: dict):
    try:
        df = pd.DataFrame([data])

        # Ensure correct feature order
        df = df[features]

        # Scale
        df_scaled = scaler.transform(df)

        # Predict probability
        prob = model.predict_proba(df_scaled)[0][1]

        # Risk segmentation
        if prob > 0.7:
            risk = "High Risk 🔴"
        elif prob > 0.4:
            risk = "Medium Risk 🟡"
        else:
            risk = "Low Risk 🟢"

        return {
            "churn_probability": float(prob),
            "risk": risk
        }

    except Exception as e:
        return {"error": str(e)}