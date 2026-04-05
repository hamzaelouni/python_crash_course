# Examples of how to use TLS certificates for HTTPS protected communication

import requests

# Using TLS by default. If the verification failed, it will raise SSLError
response = requests.get("https://www.weather.com/my-town")

# Disable verification if needed (not recommended for production)
response = requests.get("https://www.weather.com/my-town", verify=False)

# Provide a custom CA bundle
response = requests.get("https://www.weather.com/my-town", verify="/bundle_path")

# Some servers require client certificates
response = requests.get("https://www.weather.com/my-town", cert=("/cert_path", "/key_path"))