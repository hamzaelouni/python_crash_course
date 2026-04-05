import requests

# Hardcoded query parameters in the URL string
# response = requests.get(
#     "http://127.0.0.1:8000/api/items?offset=2&limit=2&max_price=40"
# )

query_params = {
    "offset": 2,
    "limit": 2,
    "max_price": 40
}

# Use the params keyword argument to pass the query parameters
response = requests.get(
    "http://127.0.0.1:8000/api/items",
    params=query_params,
)


print(response.json())