# SafeHorizon - Drug Risk Prediction with Machine Learning

**SafeHorizon** is a machine learning-powered web application that predicts an individual's drug risk level (High or Low) based on behavioral, mental health, and demographic factors. The app is built with Flask and deployed using a trained Random Forest model.

---

## 🚀 Features
- Predicts drug use risk level based on user inputs
- Collects 10 behavioral and demographic factors
- Trained using multiple ML models (Random Forest, SVM, Logistic Regression, XGBoost)
- Final model selected based on F1 score and test performance
- Clean, user-friendly web interface with motivational feedback

---

## 📁 Project Structure
```
SafeHorizon-DrugRisk-Prediction/
├── app.py                    # Flask backend
├── scaler.pkl               # Saved StandardScaler object
├── random_forest_model.pkl  # Trained Random Forest model
├── Drug_last_updated1.csv   # Processed dataset
├── MY_UPDATED_EDA_23.ipynb  # Jupyter Notebook with full model pipeline
├── requirements.txt         # List of Python dependencies
└── templates/
    └── index.html           # Web interface (form + display)
```

---

## 🧠 Model Details
- **Data Source:** NSDUH (National Survey on Drug Use and Health)
- **Target:** `drug_risk_level` (0 = Low, 1 = High)
- **Preprocessing:**
  - Missing value handling
  - Label encoding & feature scaling
  - Undersampling for imbalance
  - 5% label noise injection
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1 Score
- **Best Model:** Random Forest

---

## 🌐 How to Run the App
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run Flask app
python app.py

# 3. Open in browser
http://127.0.0.1:5000/
```

---

## 📊 Sample Features
- Painkiller Use Recency
- Mental Health Thoughts
- Prescription Pill Dependence
- Age Group
- Education Level
- Self-Rated Health
- Gender
- Current Drug Use
- Total Use Days (30d)

---

## 💬 Motivational Messaging
- **Low Risk:** Encouraging message to stay healthy
- **High Risk:** Supportive, hopeful message for recovery

---

## 📌 Future Improvements
- Integrate mental health chatbot
- Add mobile responsiveness
- Connect to real-time helpline APIs

---


---

Made with ❤️ for awareness and early intervention.


