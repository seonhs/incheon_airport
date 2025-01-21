import requests
import pandas as pd
import xml.etree.ElementTree as ET
from google.colab import userdata
from xml.dom.minidom import parseString

# Get Incheon Airport data via API in colab environment
url = 'http://apis.data.go.kr/B551177/StatusOfSrvDestinations/getServiceDestinationInfo' # API url
params ={('serviceKey', userdata.get('serviceKey')),
  ('type', 'xml') }

response = requests.get(url, params=params)
# If you successfully imported data
if response.status_code == 200: 
    print("API call successful!")
xml_data=response.text
# Formatting XML data for viewing
parsed_xml = parseString(xml_data)
pretty_xml = parsed_xml.toprettyxml(indent="  ") # Apply indentation

# Parsing XML
root = ET.fromstring(xml_data)
row_dict= {
    'airportCode': [],
    'airportName': [],
    'countryName': []
}
#get the values under the items/item hierarchy as a list and use iteration
for i in root.findall("./body/items/item"):
  #  get text from item_name and store it in a dictionary
  for j in i:
    row_dict[j.tag].append(j.text)
df = pd.DataFrame(row_dict)
df.head()
