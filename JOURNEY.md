🗺️ User Journey & System Documentation: Telco Intel
This document provides a visual walkthrough of the Telco Intel platform, demonstrating how raw data from the IBM Telco Dataset is transformed into actionable AI insights.

1. System Health & Dashboard Overview
Upon landing on the dashboard, the system performs an automated handshake with the FastAPI backend hosted on Render.

Status: A green indicator confirms "Neural Network Active," signifying the ML model is loaded and ready for inference.

Metrics: The overview cards track the total volume of analyzed customers stored in the Supabase cloud database.

<img width="950" height="388" alt="telco" src="https://github.com/user-attachments/assets/38f0d2f7-77b4-4839-a9cc-6d0b44bf5825" />


2. Individual Churn Prediction
The core functionality allows users to input specific customer data to receive a real-time risk score.

Input: User enters demographics (tenure) and contract details into the Predictor.

AI Inference: The backend processes these features through the churn_model.pkl.

Output: Results are displayed with a risk label (e.g., "High Risk") and a percentage (e.g., 95%).

<img width="937" height="398" alt="image" src="https://github.com/user-attachments/assets/cdb4ff63-384b-4525-b1ff-a793e9283f9c" />


3. Batch Data Processing
To handle enterprise-level data, the platform supports CSV uploads.

Upload: A CSV file (e.g., CHURN 1.csv) is uploaded through the interface.

Batch Analysis: The system iterates through the records, providing an Average Risk for the entire batch.

Automation: This mirrors a real-world scenario where a company analyzes its entire monthly subscriber base at once.

<img width="953" height="415" alt="image" src="https://github.com/user-attachments/assets/993494c1-f65c-417d-ba4c-14e50e1a61e2" />

4. Cloud Data Persistence (Supabase)
Every analysis is permanent. This project uses Supabase to ensure that data is not lost when the session ends.

Data Log: Users can navigate to the "Data Log" to audit all previous predictions.

Database Sync: The "Welcome Back" message and history tables verify that the frontend is successfully pulling historical data from the cloud.

<img width="947" height="271" alt="image" src="https://github.com/user-attachments/assets/2b0dbc1f-c2e5-4e5c-9e54-10359861632c" />


🛠️ Technical Summary
Source Data: IBM Telco Customer Churn.

Model: Scikit-Learn Pipeline (.pkl).

Backend: FastAPI.

Database: PostgreSQL via Supabase.
