import zipfile
import os

# Path to the directory containing the ZIP files
zip_directory = r'C:\Users\aeman\OneDrive\Desktop\earthquake-prediction-japan\data'
extraction_base_dir = r'C:\Users\aeman\OneDrive\Desktop\earthquake-prediction-japan\extracted1_files'

# Create the directory for extracted files if it doesn't exist
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
        
        # Now, check the encoding and read the files properly
        for extracted_file in os.listdir(extraction_dir):
            if extracted_file.endswith('.dat'):
                dat_file_path = os.path.join(extraction_dir, extracted_file)
                
                # Detect and confirm encoding (Shift-JIS in this case)
                try:
                    with open(dat_file_path, 'r', encoding='shift_jis') as f:
                        content = f.read()
                        print(f"Successfully read {extracted_file} with Shift-JIS encoding")
                        print(f"Content sample from {extracted_file}:\n{content[:500]}")  # Print first 500 characters
                except Exception as e:
                    print(f"Failed to read {extracted_file} with Shift-JIS encoding: {e}")

print("All ZIP files have been extracted and read with the correct encoding.")
