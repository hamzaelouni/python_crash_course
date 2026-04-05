import requests

with requests.Session() as session:
    credentials = {"username": "some_name", "password": "pass"}

    session.post("http://127.0.0.1:8000/api/login", data=credentials)

    response = session.get("http://127.0.0.1:8000/protected")

    print("Protected route:")
    print(response.status_code)
    print(response.text)