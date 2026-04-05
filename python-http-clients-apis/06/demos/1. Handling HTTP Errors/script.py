import requests

try:
    # Make a request to the non-existent route
    response = requests.get("http://127.0.0.1:8000/something/")
    response.raise_for_status()
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(err)
else:
    print(response.status_code)