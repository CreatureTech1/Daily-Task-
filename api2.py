'''
import requests
response = requests.get("https://randomuser.me/api/")
print(response.text)
'''
import requests
response = requests.get("https://randomuser.me/api/")
print(requests["name"])