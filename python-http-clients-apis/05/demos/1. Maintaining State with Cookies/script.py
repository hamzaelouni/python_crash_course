import requests

# Set a custom cookie
custom_cookies = {"user_id": "2"}

response = requests.get(
    "http://127.0.0.1:8000/api/cookies",
    cookies=custom_cookies # use the cookies argument
)

# Print the cookiejar from the response as a dictionary
print(response.cookies.get_dict())
# Print the value of the user_id cookie
print(response.cookies["user_id"])

# Proof that cookies are managed with headers
print("=== Request Headers ===")
print(response.request.headers)

print("\n=== Response Headers ===")
print(response.headers)