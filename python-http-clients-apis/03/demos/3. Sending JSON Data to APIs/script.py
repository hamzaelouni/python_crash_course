import requests

# Message body to be sent in the request
message_body = {"name": "Some item", "price": 22}

# Submit JSON data through the body of the request
response = requests.post(
    "http://127.0.0.1:8000/api/items",
    json=message_body # use json keyword argument to send JSON data
)

# The content type is application/json and the body is the JSON data
print(response.request.headers["content-type"])
print(response.request.body)
