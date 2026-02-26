import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Load environmental variables from .env
load_dotenv()

app = FastAPI()

# Enable CORS for frontend connectivity
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration from .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("CRITICAL ERROR: Supabase credentials not found in .env file")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class ChurnRequest(BaseModel):
    customer_name: str
    tenure: int
    monthly_charges: float
    contract: str

@app.get("/")
def read_root():
    return {"status": "AI Backend Online", "database": "Connected"}

@app.post("/analyze")
async def analyze_churn(data: ChurnRequest):
    # --- Simple AI Prediction Logic ---
    score = 0
    
    # Contract Risk
    if data.contract == "Month-to-month": 
        score += 45
    elif data.contract == "One year": 
        score += 20
    
    # Tenure Risk (Newer customers churn more)
    if data.tenure < 12: 
        score += 30
    elif data.tenure < 24: 
        score += 15
    
    # Charges Risk
    if data.monthly_charges > 80: 
        score += 20
    
    # Final Calculation
    risk_score = min(score, 99)
    label = "High Risk" if risk_score > 70 else ("Moderate Risk" if risk_score > 40 else "Low Risk")

    # --- Save to Supabase Cloud ---
    try:
        db_entry = {
            "customer_name": data.customer_name,
            "risk_score": float(risk_score),
            "risk_label": label
        }
        
        # Insert into Supabase
        supabase.table("churn_history").insert(db_entry).execute()
        
        # RETURN KEYS: We provide both underscore and standard names to be safe
        return {
            "customer_name": data.customer_name, 
            "name": data.customer_name, 
            "risk_score": float(risk_score),
            "score": float(risk_score), 
            "risk_label": label,
            "label": label
        }
    except Exception as e:
        print(f"Database Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history")
async def get_history():
    try:
        # Fetches the last 50 entries
        response = supabase.table("churn_history").select("*").order("created_at", desc=True).limit(50).execute()
        return response.data
    except Exception as e:
        print(f"History Fetch Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)