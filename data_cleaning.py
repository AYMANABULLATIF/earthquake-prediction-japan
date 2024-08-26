import pandas as pd
import os

# Load the merged data
data = pd.read_csv(r'C:\Users\aeman\OneDrive\Desktop\earthquake-prediction-japan\merged_data\merged_data.csv')

# Clean the data by dropping missing values for Magnitude/Intensity
data_cleaned = data.dropna(subset=['Magnitude/Intensity']).copy()

# Handle missing values in 'Depth' by filling them with the mean value
data_cleaned['Depth'] = data_cleaned['Depth'].fillna(data_cleaned['Depth'].mean())

# Convert 'Timestamp' to datetime format
data_cleaned['Timestamp'] = pd.to_datetime(data_cleaned['Timestamp'], errors='coerce')

# Create Latitude and Longitude columns by combining degrees and minutes
data_cleaned['Latitude'] = data_cleaned['Latitude Degrees'] + data_cleaned['Latitude Minutes'] / 60
data_cleaned['Longitude'] = data_cleaned['Longitude Degrees'] + data_cleaned['Longitude Minutes'] / 60

# Ensure the save directory exists
save_directory = r'C:\Users\aeman\OneDrive\Desktop\earthquake-prediction-japan\cleaned_data'
os.makedirs(save_directory, exist_ok=True)

# Save the cleaned data to a new CSV file
data_cleaned.to_csv(os.path.join(save_directory, 'cleaned_data.csv'), index=False)

# Preview cleaned data
print(data_cleaned.head())
