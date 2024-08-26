import os
import pandas as pd

# Directory containing the CSV files
csv_directory = r'C:\Users\aeman\OneDrive\Desktop\earthquake-prediction-japan\extracted_files'

# Directory to save the merged file
save_directory = r'C:\Users\aeman\OneDrive\Desktop\earthquake-prediction-japan\merged_data'

# Create save directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# Initialize an empty DataFrame
merged_data = pd.DataFrame()

# Function to try different encodings
def read_csv_with_encoding(file_path):
    encodings = ['utf-8', 'shift_jis', 'iso-8859-1', 'cp1252']  # List of encodings to try
    for enc in encodings:
        try:
            return pd.read_csv(file_path, encoding=enc)
        except UnicodeDecodeError:
            print(f"Encoding {enc} failed for {file_path}. Trying next encoding...")
        except Exception as e:
            print(f"An error occurred with encoding {enc}: {e}")
    return None

# Loop through all CSV files and merge them
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_directory, filename)
        print(f"Processing file: {file_path}")  # Debugging print
        data = read_csv_with_encoding(file_path)
        if data is not None:
            print(f"Data from {filename}:\n", data.head())  # Show the first few rows of the data
            merged_data = pd.concat([merged_data, data], ignore_index=True)
        else:
            print(f"Failed to read {filename} with any known encoding.")

# Print a preview of the merged data for debugging
if not merged_data.empty:
    print("Preview of merged data:")
    print(merged_data.head())
else:
    print("Merged data is empty. No data was found in the CSV files.")

# Save the merged file to the specified directory
output_path = os.path.join(save_directory, 'merged_data.csv')
merged_data.to_csv(output_path, index=False)

print(f"All files merged and saved successfully at {output_path}")
