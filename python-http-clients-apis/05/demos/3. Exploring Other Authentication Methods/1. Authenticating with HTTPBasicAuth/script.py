import requests
from requests.auth import HTTPBasicAuth

username = "username"
password = "pass"

response = requests.get(
    "http://127.0.0.1:8000/protected-endpoint",
    auth=HTTPBasicAuth(username, password)
) # you can leave out HTTPBasicAuth, it will be used by default

print(response.text)