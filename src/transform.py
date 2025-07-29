import pandas as pd

def transform_data():
    df = pd.read_csv('data/processed/extracted.csv')
    # Simple transformation: Drop rows with missing PatientID
    df = df.dropna(subset=['PatientID'])
    df.to_csv('data/processed/transformed.csv', index=False)
    print("Transformation complete.")