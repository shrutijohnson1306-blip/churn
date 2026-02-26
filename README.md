📊 Telco Intel: End-to-End Churn Prediction
Telco Intel is a full-stack predictive analytics platform that identifies at-risk telecommunications customers using Machine Learning. This project bridges the gap between raw data science research (Kaggle) and a live, functional web application.

🚀 Live Links
Dashboard: [https://telco-dashboard-v3.onrender.com/]

API Backend: Powered by FastAPI & Hosted on Render

🧠 Project Evolution: From Kaggle to Cloud
This project follows the complete data science lifecycle:

Research & Training: Exploratory Data Analysis (EDA) and Model Training were performed on Kaggle using the IBM Telco Customer Churn dataset.

Model Export: The best-performing model was exported as churn_model.pkl.

Production API: Built a FastAPI backend to serve the model predictions in real-time.

Frontend Dashboard: Created a responsive UI to visualize risk scores and manage customer data.

📊 The Dataset
The model was trained on the Telco Customer Churn (IBM Sample Data Sets) from Kaggle.

Context: Predict behavior to retain customers by analyzing all relevant customer data.

Features Used:

Demographics: Gender, Senior Citizen status, Partner, Dependents.

Services: Tenure, Phone Service, Multiple Lines, Internet Service, Online Security, Tech Support, Streaming TV/Movies.

Account Info: Contract type, Paperless Billing, Payment Method, Monthly Charges, Total Charges.

🛠️ Tech Stack
Frontend: HTML5, JavaScript (ES6+), Tailwind CSS.

Backend: FastAPI (Python), Uvicorn.

Database: Supabase (PostgreSQL) for cloud data persistence.

Machine Learning: Scikit-Learn (Random Forest/Logistic Regression).

Deployment: Render (Static Site & Web Service).

📂 Repository Structure
telco-backend/: Live API source code, dependencies, and the trained .pkl model.

index.html: The main dashboard user interface.

research_analysis.pdf: Full documentation of the Kaggle data science process.

kaggle_script.py: The original Python code used to train and validate the model.

💻 How to Run Locally
Clone the Repo:

Bash
git clone https://github.com/shrutijohnson1306-blip/churn.git
Setup Backend:

Navigate to telco-backend/.

Install dependencies: pip install -r requirements.txt.

Add .env file with SUPABASE_URL and SUPABASE_KEY.

Start server: uvicorn main:app --reload.

Launch Dashboard:

Open index.html in your browser.

Developed by Shruti Johnson — Transforming data into actionable business intelligence.
