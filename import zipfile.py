import zipfile
import os

# Path to the directory containing the ZIP files (update this to your actual directory)
zip_directory = r'C:\Users\aeman\OneDrive\Desktop\earthquake-prediction-japan\data'
extraction_base_dir = r'C:\Users\aeman\OneDrive\Desktop\earthquake-prediction-japan\extracted_files'

# Create a directory to hold the extracted files if it doesn't exist
os.makedirs(extraction_base_dir, exist_ok=True)

# Loop through all files in the directory
for filename in os.listdir(zip_directory):
    if filename.endswith('.zip'):
        # Define the path to the current ZIP file
        zip_file_path = os.path.join(zip_directory, filename)
        
        # Define the extraction directory for this ZIP file
        extraction_dir = os.path.join(extraction_base_dir, os.path.splitext(filename)[0])
        os.makedirs(extraction_dir, exist_ok=True)
        
        # Extract the ZIP file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extraction_dir)
        
        print(f"Extracted {filename} to {extraction_dir}")

print("All ZIP files have been extracted.")
