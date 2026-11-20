import requests
# from pprint import pprint

# metodos disponibles : GET, POST, PUT, DELETE
response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()

# for user in data:
#     print(f"Usuario: {user['id']} - {user['name']}")

# pprint(response.json())

