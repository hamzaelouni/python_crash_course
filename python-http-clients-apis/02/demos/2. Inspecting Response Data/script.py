import requests


response = requests.get("http://127.0.0.1:8000/something")
print(response.status_code)

# HTTP Status Codes
if response.status_code == 200: # Success!
    print("Success!")
elif response.status_code == 500: # Server error.
    print("Server error.")
elif response.status_code == 404: # Page not Found.
    print("Page not Found.")



response = requests.get("http://127.0.0.1:8000/api/items")

# Binary data but formatted by the print function
# print(response.content)

# Hexadecimal representation of the binary data
# print(response.content.hex())

# String representation of the response
# print(response.text)

# Response headers contain the metadata for the response
# print(response.headers["content-type"])

# JSON from the response converted to Python objects
print(response.json())
print(response.json()[1]["name"])