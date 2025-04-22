# 🚗 Car Fault Detection using Machine Learning

A web-based ML app that detects car faults based on symptoms and lets users interact with a custom AI chatbot for guidance.

## 🔧 Features
- Select symptoms and get predicted car faults
- Inbuilt AI chatbot gives cause, solution, and explanation
- Built with Flask, Python, HTML/CSS, and Bootstrap

## 🧠 Tech Stack
- Flask (Backend)
- HTML/CSS + Bootstrap (Frontend)
- Pandas, scikit-learn (ML)
- Model: Trained using Random Forest
- Chatbot: Custom rule-based logic (no API key needed)

## 💻 How to Run Locally
```bash
git clone https://github.com/AnuragSen370/Car-Fault-Detection.git
cd Car-Fault-Detection
python -m venv venv
venv\Scripts\activate     # On Windows
pip install -r requirements.txt
python app.py

## ⚠️ Disclaimer
This is for educational purposes. Always consult a certified mechanic before taking any action on car issues.

## Project Structure

├── app.py
├── templates/
│   ├── index.html
│   ├── abt.html
│   └── cont.html
├── model_train.py
├── car_fault_model.pkl
├── car_symptom_data.csv
├── car_fault_data.csv
└── static/
