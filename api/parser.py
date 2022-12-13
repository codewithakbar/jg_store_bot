import requests


BASE_URL = 'https://akbar2day.pythonanywhere.com/api/'


response = requests.get(f"{BASE_URL}/products")


print(response)

