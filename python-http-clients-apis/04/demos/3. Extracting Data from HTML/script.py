import requests
from bs4 import BeautifulSoup

# Make a request to the /about route
response = requests.get("http://127.0.0.1:8000/about")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the description (paragraph text)
description = soup.find('p').get_text().strip() # use strip to remove whitespace
print("Description:")
print(description)

# Extract phone and email by using IDs
phone = soup.find('td', id='phone').get_text().strip()
email = soup.find('td', id='email').get_text().strip()

print("Phone:", phone)
print("Email:", email)