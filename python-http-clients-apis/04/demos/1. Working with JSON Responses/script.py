import requests

response = requests.get("http://127.0.0.1:8000/api/items")

# Try to parse the response as JSON
try:
    data = response.json()
except ValueError:
    print("Response is not valid JSON")

# Pretty print the data
import json

print(json.dumps(data, indent=4))