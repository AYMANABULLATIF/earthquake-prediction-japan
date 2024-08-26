# Earthquake Prediction in Japan

## Project Overview

This project focuses on analyzing and predicting earthquake patterns in Japan using historical data. The aim is to detect patterns that could help in forecasting future seismic activities. The project involves several stages, from data extraction and cleaning to visualization and pattern analysis.

## Technologies Used

- **Python**: The core programming language used for data processing, analysis, and visualization.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib & Seaborn**: For data visualization, including plots and heatmaps.
- **Folium**: For creating interactive maps to visualize earthquake data.
- **FPDF**: Used for generating PDFs, if applicable.
- **Git**: Version control system to track changes in the project.

## Project Structure

- **Data Extraction**: Extracted data from multiple ZIP and KML files, focusing on earthquake-related datasets.
- **Data Cleaning**: Handled missing values, converted timestamps, and computed latitude and longitude from degrees and minutes.
- **Feature Engineering**: Added new features like the year of occurrence for better analysis.
- **Visualization**: Created visualizations such as time series plots of earthquake frequency, distribution histograms, and interactive heatmaps of earthquake locations.
- **Pattern Analysis**: Conducted correlation analysis and explored potential patterns in the earthquake data.

## Key Steps

1. **Extracted Data**: Data was extracted from multiple sources, including ZIP and KML files.
2. **Merged Datasets**: Combined multiple CSV files to form a comprehensive dataset.
3. **Data Cleaning**: Addressed missing values, converted formats, and ensured data consistency.
4. **Data Visualization**: Created plots to understand the distribution and frequency of earthquakes.
5. **Heatmap Creation**: Used Folium to create a heatmap of earthquake locations across Japan.
6. **Pattern Analysis**: Analyzed correlations and trends to detect patterns in earthquake occurrences.

## How to Run

**1. Clone the repository:**
   git clone https://github.com/AYMANABULLATIF/earthquake-prediction-japan.git

**2.Navigate to the project directory:**
cd earthquake-prediction-japan 

**3.Install the required Python packages:**
pip install -r requirements.txt

**4.Run the data cleaning script:**
python data_cleaning.py
**5.Generate visualizations and analysis:**
python Data\ Exploration.py

**6.View the generated heatmap:**
Open earthquake_heatmap.html in your browser.


# Future Work
**Implement more advanced predictive models using machine learning.**
**Integrate real-time data sources for ongoing earthquake monitoring.**
**Improve the data visualization with more interactive elements.**



