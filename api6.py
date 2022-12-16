#HTTP Methods
import requests
print(requests.post("https://api.thedogapi.com/v1/breeds/1"))
print(requests.get("https://api.thedogapi.com/v1/breeds/1"))
print(requests.put("https://api.thedogapi.com/v1/breeds/1"))
print(requests.delete("https://api.thedogapi.com/v1/breeds/1"))