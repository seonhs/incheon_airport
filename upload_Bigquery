from google.colab import files
from google.oauth2 import service_account
from google.cloud import bigquery

#How to upload an imported DataFrame (df) to Bigquery

#Importing BigQuery's authentication key JSON file
uploaded = files.upload()

# Set the service account key file path
key_path = list(uploaded.keys())[0]  # Uploaded key file path
credentials = service_account.Credentials.from_service_account_file(key_path)
from google.cloud import bigquery

# Setting up dataset and table information to upload
project_id = "incheon-airport-shs" # BigQuery Project ID
dataset_id = "incheon_airport" # BigQuery Dataset ID

# Create a BigQuery client
client = bigquery.Client(credentials=credentials, project='incheon-airport-shs')

# Upload a dataframe
table_id= "incheon_airport" # BigQuery table name to generate
job = client.load_table_from_dataframe(df, f"{dataset_id}.{table_id}")

#Waiting for a task to complete
job.result()

# Check the results
print(f"Uploaded {job.output_rows} rows to {dataset_id}.{table_id}.")
