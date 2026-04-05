import requests

query_params = {
    "offset": 0,
    "limit": 2,
    "max_price": 40
}

response = requests.get("http://127.0.0.1:8000/api/items")
print(response)
print(response.status_code)
print("\nthe content is bytes : ")
print(response.content)
print("\nHex method show what this payload actually looks like : ")
print(response.content.hex())
print("\nshow the context as text : ")
print(response.text)
print("\nlist headers : ")
print(response.headers)
print("\nShow content-type headers : ")
print(response.headers["content-type"])
print("\n")
print(response.json()[1]["name"])

if response.status_code == 200:
    print("\nSuccess!")
elif response.status_code == 404:
    print("\nPage Not Found")
elif response.status_code == 500:
    print("\nServer Error")

print("\npass query params: ")
response = requests.get("http://127.0.0.1:8000/api/items", params=query_params)
print(response.json())
