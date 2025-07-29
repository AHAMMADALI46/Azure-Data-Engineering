import pandas as pd
from azure.storage.blob import BlobServiceClient

def extract_data(blob_conn_str, container, blob_name, output_path):
    blob_service_client = BlobServiceClient.from_connection_string(blob_conn_str)
    blob_client = blob_service_client.get_container_client(container).get_blob_client(blob_name)
    with open(output_path, "wb") as f:
        f.write(blob_client.download_blob().readall())
    print(f"Extracted {blob_name} to {output_path}")

# Example usage:
# extract_data('<conn_str>', 'raw-data', 'patients.csv', 'data/raw/patients.csv')