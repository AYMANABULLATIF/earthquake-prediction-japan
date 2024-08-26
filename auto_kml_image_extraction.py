import os
import requests
from xml.etree import ElementTree as ET

def extract_kml_info(kml_file):
    # Parse the KML file
    tree = ET.parse(kml_file)
    root = tree.getroot()
    namespace = {"ns0": "http://www.opengis.net/kml/2.2"}

    # Find the GroundOverlay section and extract the image URL
    ground_overlay = root.find(".//ns0:GroundOverlay", namespace)
    if ground_overlay is not None:
        href = ground_overlay.find(".//ns0:href", namespace).text
        lat_lon_box = ground_overlay.find(".//ns0:LatLonBox", namespace)
        north = lat_lon_box.find("ns0:north", namespace).text
        south = lat_lon_box.find("ns0:south", namespace).text
        east = lat_lon_box.find("ns0:east", namespace).text
        west = lat_lon_box.find("ns0:west", namespace).text

        return href, north, south, east, west
    else:
        return None, None, None, None, None

def download_image(url, output_file):
    # Download the image and save it to the output file
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_file, "wb") as file:
            file.write(response.content)
        print(f"Image saved to {output_file}")
    else:
        print(f"Failed to download image from {url}")

def process_kml_files(kml_path, image_directory):
    # Check if the provided path is a directory or a single file
    if os.path.isdir(kml_path):
        for filename in os.listdir(kml_path):
            if filename.endswith(".kml"):
                kml_file = os.path.join(kml_path, filename)
                process_single_kml(kml_file, image_directory)
    else:
        # Handle the single file case
        process_single_kml(kml_path, image_directory)

def process_single_kml(kml_file, image_directory):
    print(f"Processing {kml_file}")
    href, north, south, east, west = extract_kml_info(kml_file)
    if href:
        image_filename = os.path.join(image_directory, os.path.basename(kml_file).replace('.kml', '.png'))
        download_image(href, image_filename)
    else:
        print(f"No valid GroundOverlay found in {kml_file}")

# Set your KML directory or file path
kml_path = r'C:\Users\aeman\OneDrive\Desktop\earthquake-prediction-japan\data\datav1\I-Y2024-MAP-AVR-T30_I45_CA-WMS_EN.kml'
# Set the directory where you want to save images
image_directory = r'C:\Users\aeman\OneDrive\Desktop\earthquake-prediction-japan\images'

# Ensure the image directory exists
os.makedirs(image_directory, exist_ok=True)

# Process the KML files
process_kml_files(kml_path, image_directory)

