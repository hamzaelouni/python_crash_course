import requests
# Use the xml library to parse the response
import xml.etree.ElementTree as ET

# XML message body (which is just a string)
message_body = """
<item>
    <name>Some item</name>
    <price>300</price>
</item>
"""

response = requests.post(
    "http://127.0.0.1:8000/api/items/xml",
    data=message_body,
    headers={"Content-Type": "application/xml"} # Set the request content type to xml
)

# Print the raw response
print(response.text)

# Parse the response as XML and find the name and price
print(ET.fromstring(response.text).find("name").text)
print(ET.fromstring(response.text).find("price").text)
