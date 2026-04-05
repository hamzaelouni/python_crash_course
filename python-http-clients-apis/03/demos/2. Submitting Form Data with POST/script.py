import requests

# Submit form data through the body of the request
response = requests.post(
    "http://127.0.0.1:8000/items/new",
    data={"name": "Another item", "price": 44},
    allow_redirects=False, # We don't want to get redirected to the new item page
)

# Request content type is x-www-form-urlencoded and the body is the form data
# You can use response.request to access the prepared request
print(response.request.headers["content-type"])
print(response.request.body)