import pandas as pd

def load_data():
    df = pd.read_csv('data/processed/transformed.csv')
    # Simulate loading to database (here, just save as CSV)
    df.to_csv('data/processed/final_output.csv', index=False)
    print("Load complete.")