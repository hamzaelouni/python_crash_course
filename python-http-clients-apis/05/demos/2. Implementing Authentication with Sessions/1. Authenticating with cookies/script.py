import requests

# Wrong credentials
# credentials = {"username": "name", "password": "pass"}
# Correct credentials
credentials = {"username": "some_name", "password": "pass"}

# Log in with the credentials and receive cookies
login_response = requests.post(
    "http://127.0.0.1:8000/api/login",
    data=credentials
)

# Extract cookies returned from login response
login_cookies = login_response.cookies

print("Cookies returned from login:")
print(login_cookies.get_dict())

print("Login response:")
print(login_response.text)

# Use the cookies to access a protected route
response = requests.get(
    "http://127.0.0.1:8000/protected",
    cookies=login_cookies
)

print("Protected route:")
print(response.status_code)
print(response.text)