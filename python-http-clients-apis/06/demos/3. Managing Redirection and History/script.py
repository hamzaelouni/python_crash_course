import requests

# This will redirect to the new route
# response = requests.get("http://127.0.0.1:8000/old-route")

# HEAD HTTP method does not allow redirects by default
# This will return a 307 redirectstatus code
# response = requests.head("http://127.0.0.1:8000/old-route")

# You can set the allow_redirects parameter to True to allow redirects
# response = requests.head("http://127.0.0.1:8000/old-route", allow_redirects=True)

# You can also disable redirection for the GET request
# response = requests.get("http://127.0.0.1:8000/old-route", allow_redirects=False)

response = requests.get("http://127.0.0.1:8000/old-route")

# Print the history of redirects
print(response.history)

print(response.url)
print(response.status_code)
print(response.text)