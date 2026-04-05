import requests

# PUT request typically replaces the entire resource with new data
response = requests.put(
    "http://127.0.0.1:8000/api/items/1",
    json={"name": "Updated PUT Name", "price": 100}
)

# PATCH request typically updates specific fields of a resource
response = requests.patch(
    "http://127.0.0.1:8000/api/items/1",
    json={"name": "Updated PATCH Name"}
)

# DELETE request typically deletes a resource
response = requests.delete(
    "http://127.0.0.1:8000/api/items/1",
)


print(response.json())