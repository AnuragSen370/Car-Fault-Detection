from sklearn.preprocessing import LabelEncoder
import pickle

# List of all possible car faults
faults = ['engine_issue', 'transmission_issue', 'brake_issue', 'battery_issue', 'exhaust_issue']

# Initialize label encoder and fit it on the list of faults
label_encoder = LabelEncoder()
label_encoder.fit(faults)

# Save the label encoder
with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

print("Label encoder saved to label_encoder.pkl")
