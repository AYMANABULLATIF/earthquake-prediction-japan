import requests

# URL of the map image
map_url = "https://www.j-shis.bosai.go.jp/map/wms/jmw?map=Z-V4-JAPAN&REQUEST=GetMap&SERVICE=WMS&VERSION=1.1.1&LAYERS=Z-V4-JAPAN-AMP-VS400_M250-JCODE&FORMAT=image/png&SRS=EPSG:4326&BBOX=120,24,153,47&WIDTH=1024&HEIGHT=1024"

# Send a GET request to download the image
response = requests.get(map_url)

# Save the image to a file
with open("seismic_map.png", "wb") as file:
    file.write(response.content)

print("Map image downloaded successfully.")