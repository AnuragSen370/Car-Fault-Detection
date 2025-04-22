from flask import Flask, render_template, request, jsonify, session
import pickle
import numpy as np

app = Flask(__name__)
app.secret_key = 'abcde'

# Load model and label encoder
model = pickle.load(open('car_fault_model.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))

# Symptoms used in the model
symptoms = ['engine_noise', 'smoke', 'vibration', 'oil_leak',
            'warning_light', 'slow_acceleration', 'overheating', 'brake_issues']

# Home page
@app.route('/')
def home():
    return render_template('index.html', symptoms=symptoms)

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    input_features = [int(request.form.get(symptom, 0)) for symptom in symptoms]
    prediction = model.predict([input_features])[0]
    predicted_fault = label_encoder.inverse_transform([prediction])[0]

    # Store predicted fault in session
    session['predicted_fault'] = predicted_fault

    return render_template('index.html', symptoms=symptoms, result=f"Predicted fault: {predicted_fault}")

# Chatbot response route
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    predicted_fault = session.get('predicted_fault', 'car fault')  # Use stored fault or default

    message_lower = user_message.lower()

    if 'cause' in message_lower or 'reason' in message_lower:
        response = f"🤖 The cause of the {predicted_fault} could be due to malfunctioning components, poor maintenance, or wear and tear."
    elif 'solution' in message_lower or 'fix' in message_lower or 'solve' in message_lower:
        response = f"🤖 To solve the {predicted_fault}, consider replacing faulty components, performing regular maintenance, or visiting a mechanic."
    elif 'how' in message_lower and predicted_fault in message_lower:
        response = f"🤖 The {predicted_fault} might be caused by prolonged use, overheating, or component failure."
    elif 'how' in message_lower:
        response = f"🤖 Please ask about the predicted car fault only."
    else:
        response = f"🤖 Please ask about the predicted car fault only."

    return jsonify({'response': response})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
