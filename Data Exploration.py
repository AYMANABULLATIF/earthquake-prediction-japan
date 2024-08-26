import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Load the merged data
data = pd.read_csv(r'C:\Users\aeman\OneDrive\Desktop\earthquake-prediction-japan\merged_data\merged_data.csv')

# Ensure 'Timestamp' is parsed as a datetime object
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Create 'Latitude' and 'Longitude' if not already present
if 'Latitude' not in data.columns or 'Longitude' not in data.columns:
    data['Latitude'] = data['Latitude Degrees'] + data['Latitude Minutes'] / 60
    data['Longitude'] = data['Longitude Degrees'] + data['Longitude Minutes'] / 60

# Plot the number of earthquakes over time
data['Year'] = data['Timestamp'].dt.year
yearly_counts = data['Year'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
plt.plot(yearly_counts.index, yearly_counts.values)
plt.title('Number of Earthquakes Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Earthquakes')
plt.show()

# Create a map centered around Japan
m = folium.Map(location=[36.2048, 138.2529], zoom_start=5)

# Add earthquake locations as a heatmap
heat_data = [[row['Latitude'], row['Longitude']] for index, row in data.iterrows()]

HeatMap(heat_data).add_to(m)

# Save the map as an HTML file
m.save('earthquake_heatmap.html')

# Display basic information
print(data.info())
print(data.describe())

# Display the first few rows
print(data.head())

# Only select numeric columns for correlation
numeric_data = data.select_dtypes(include=['float64', 'int64'])

# Example: Histogram of Magnitude/Intensity
plt.figure(figsize=(10, 6))
sns.histplot(data['Magnitude/Intensity'].dropna(), bins=30, kde=True)
plt.title('Distribution of Earthquake Magnitude/Intensity')
plt.xlabel('Magnitude/Intensity')
plt.ylabel('Frequency')

# Correlation Matrix of numeric columns
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
