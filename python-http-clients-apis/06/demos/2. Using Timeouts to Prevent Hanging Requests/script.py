import requests

try:
    # The timeout is a tuple of (connect timeout, read timeout)
    # The connect timeout is the time to connect to the server
    # The read timeout is the time to read the response from the server
    response = requests.get("http://127.0.0.1:8000/slow-response", timeout=(5, 3))
    print(response.json())

    # This will raise a ConnectTimeout error
    # response = requests.get("http://10.255.255.1", timeout=(5, 6))
except requests.exceptions.ConnectTimeout:
    print("The request failed to connect in the allotted time.")
except requests.exceptions.ReadTimeout:
    print("The server did not send any data in the allotted amount of time.")
except requests.exceptions.Timeout:
    print("A timeout error occurred.")