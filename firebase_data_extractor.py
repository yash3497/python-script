
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# Initialize Firebase with your service account key
cred = credentials.Certificate("/Users/yashguptamac/Downloads/Python/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Create a Firestore client
db = firestore.client()

# Define the Firestore collections you want to extract data from
collections = ["studentregistration"]

# Create an empty list to store DataFrames
dfs = []

# Loop through collections and retrieve data
for collection_name in collections:
    collection_ref = db.collection(collection_name)
    docs = collection_ref.stream()

    data = []
    for doc in docs:
        data.append(doc.to_dict())

    # Create a DataFrame for each collection
    df = pd.DataFrame(data)
    dfs.append(df)

# Concatenate DataFrames from different collections
result_df = pd.concat(dfs, ignore_index=True)

# Specify the Excel file path where you want to save the data
excel_file_path = "data.xlsx"

# Save the DataFrame to an Excel file
result_df.to_excel(excel_file_path, index=False, engine="openpyxl")

print(f"Data saved to {excel_file_path}")
