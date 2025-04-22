import pandas as pd
import random

symptoms = ['engine_noise', 'smoke', 'vibration', 'oil_leak',
            'warning_light', 'slow_acceleration', 'overheating', 'brake_issues']
faults = ['engine_issue', 'transmission_issue', 'brake_issue', 'battery_issue', 'exhaust_issue']

data = []

for _ in range(200):
    entry = {symptom: random.randint(0, 1) for symptom in symptoms}

    if entry['engine_noise'] and entry['smoke']:
        fault = 'engine_issue'
    elif entry['slow_acceleration'] and entry['vibration']:
        fault = 'transmission_issue'
    elif entry['brake_issues']:
        fault = 'brake_issue'
    elif entry['warning_light'] and entry['oil_leak']:
        fault = 'battery_issue'
    elif entry['smoke'] and entry['oil_leak'] and not entry['engine_noise']:
        fault = 'exhaust_issue'
    else:
        fault = random.choice(faults)

    entry['fault'] = fault
    data.append(entry)

df = pd.DataFrame(data)
df.to_csv('car_symptom_data.csv', index=False)
print("✅ Dataset generated: car_symptom_data.csv")
