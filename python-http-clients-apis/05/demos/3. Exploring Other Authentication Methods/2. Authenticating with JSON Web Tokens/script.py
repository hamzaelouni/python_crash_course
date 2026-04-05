import requests
from requests.auth import AuthBase

# Authorization: Bearer <token>

class JWTAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    # The auth class must have a __call__ method that takes a request object and returns a request object
    def __call__(self, request):
        request.headers["Authorization"] = f"Bearer {self.token}"
        return request

token = "abcde123"
response = requests.get(
    "http://127.0.0.1:8000/jwt-protected-route",
    auth=JWTAuth(token)
)

print(response.text)