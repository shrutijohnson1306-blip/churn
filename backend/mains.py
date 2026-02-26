from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# 1. Load the "brain" and the "map" we saved from Kaggle
try:
    model = joblib.load("churn_model.pkl")
    model_columns = joblib.load("model_columns.pkl")
    print("✅ Model and Columns loaded successfully!")
except Exception as e:
    print(f"❌ Error loading files: {e}")

app = FastAPI(title="Customer Churn Prediction API")

# 2. Enable CORS so your Frontend can talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Define the Input Schema
# These are the main numeric features. 
# Categorical features will be handled by the reindex logic below.
class CustomerData(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    # If you want specific dropdowns in the API docs, add them here:
    # gender_Male: int = 0
    # InternetService_Fiber_optic: int = 0

@app.get("/")
def home():
    return {"message": "Churn Prediction API is running!"}

@app.post("/predict")
def predict(data: CustomerData):
    # Convert input data to a Dictionary, then to a DataFrame
    input_dict = data.dict()
    df = pd.DataFrame([input_dict])
    
    # 🌟 THE MAGIC STEP: Reindexing
    # This aligns the user input with the 30+ dummy columns from training.
    # Any column not provided by the user is filled with 0.
    df = df.reindex(columns=model_columns, fill_value=0)
    
    # Make prediction
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]
    
    return {
        "churn_prediction": "Yes" if int(prediction) == 1 else "No",
        "churn_probability": f"{round(float(probability) * 100, 2)}%",
        "risk_level": "High" if probability > 0.7 else "Medium" if probability > 0.4 else "Low"
    }