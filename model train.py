import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

df = pd.read_csv('car_symptom_data.csv')

# Encode labels
le = LabelEncoder()
df['fault'] = le.fit_transform(df['fault'])

# Save label encoder
with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

# Split and train
X = df.drop('fault', axis=1)
y = df['fault']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Save model
with open('car_fault_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to car_fault_model.pkl")
