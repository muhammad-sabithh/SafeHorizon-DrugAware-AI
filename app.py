from flask import Flask, render_template, request
import pickle
import numpy as np
import random

app = Flask(__name__)

# Load the model and scaler
model = pickle.load(open("random_forest_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

FEATURES = [
    'Painkiller_Use_Recency',
    'Mental_Health_Think',
    'Dependent_On_Prescription_Pills',
    'Age_Group',
    'Education_Highest_Category',
    'Pain_Relievers_Non_Medical_Lifetime_Use',
    'health.1',
    'Gender',
    'Currently_Using_Drugs',
    'total_drug_use_days'
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        values = [float(request.form.get(f)) for f in FEATURES]
        values_scaled = scaler.transform([values])
        prediction = model.predict(values_scaled)[0]

        if prediction == 1:
            risk = "🔴 High Risk"
            high_risk_messages = [
                "You're not alone. It's brave to seek help — and help is always available. 💙",
                "Every step you take toward healing matters. Reach out, talk to someone. You are valued.",
                "This isn’t the end — it’s the beginning of your comeback. 💪 Stay strong!",
                "Asking for help shows strength, not weakness. You matter, and support is out there.",
                "Healing takes time, but you don’t have to do it alone. We believe in you. 🙌",
                "It's okay to not be okay. You deserve care, compassion, and peace."
            ]
            message = random.choice(high_risk_messages) + " — Need help? Call 1-800-662-HELP"
        else:
            risk = "🟢 Low Risk"
            low_risk_messages = [
                "Great job! Keep focusing on your well-being — mind and body.",
                "You're doing well! Stay strong, stay aware, and support others when you can. 💚",
                "Health is a journey. Keep going, one positive step at a time!",
                "Your choices today shape a brighter tomorrow. Stay inspired. ✨",
                "Celebrate your wins, no matter how small. You’ve got this!",
                "Stay informed, stay mindful, and never hesitate to ask for help if needed."
            ]
            message = random.choice(low_risk_messages)

        return render_template('index.html', prediction_text=f"Risk Level: {risk}", supportive_message=message)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
