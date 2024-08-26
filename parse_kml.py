import xml.etree.ElementTree as ET

kml_file = r'C:\Users\aeman\OneDrive\Desktop\earthquake-prediction-japan\data\datav1\Z-V4-JAPAN-AMP-VS400_M250-JCODE-WMS_EN.kml'

# Parse the KML file
tree = ET.parse(kml_file)
root = tree.getroot()

# Define the namespaces
namespaces = {
    'kml': 'http://www.opengis.net/kml/2.2',
    'gx': 'http://www.google.com/kml/ext/2.2',
    'atom': 'http://www.w3.org/2005/Atom'
}

# Print the root to check if it's parsed correctly
print(ET.tostring(root, encoding='utf8').decode('utf8'))
