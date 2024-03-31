import pandas as pd
import zipfile
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the relative paths to the zip file and output CSV file
zip_file_path = os.path.join(script_dir, 'csv_data_2023.zip')
output_csv_path = os.path.join(script_dir, 'merged_file.csv')

# Create an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Open the zip file and extract CSV files
with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
    for file_name in zip_file.namelist():
        if file_name.endswith('.csv'):
            with zip_file.open(file_name) as csv_file:
                # Read each CSV file and append it to the merged_data DataFrame
                csv_data = pd.read_csv(csv_file)
                merged_data = pd.concat([merged_data, csv_data], ignore_index=True)

# Save the merged data to a new CSV file
merged_data.to_csv(output_csv_path, index=False)
