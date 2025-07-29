import pandas as pd
from src.transform import transform_data

def test_transform_data(tmp_path):
    # Create a dummy extracted.csv
    df = pd.DataFrame({'PatientID': [1, None, 3], 'Value': [10, 20, 30]})
    df.to_csv(tmp_path / "extracted.csv", index=False)
    # Run transformation
    transform_data()
    # Check result
    result = pd.read_csv(tmp_path / "transformed.csv")
    assert result['PatientID'].isnull().sum() == 0