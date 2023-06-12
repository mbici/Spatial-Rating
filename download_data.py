import requests
import zipfile
url ="https://export.hotosm.org/downloads/6b3f8c4a-589d-4537-99e4-1518937c23a8/hotosm_ken_roads_polygons_shp.zip"

response = requests.get(url)

with open("roads.zip","wb") as file:
    file.write(response.content)

with zipfile.ZipFile("roads.zip","r") as zip:
    zip.extractall("C:/Users/mbici/Desktop/Portfolio Ptojects/Spatial peoject/data")