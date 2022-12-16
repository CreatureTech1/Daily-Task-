'''
import requests
response = requests.get("https://api.thedogapi.com/")
print(response.text)
'''

#endpoints
'''
import requests
response = requests.get("https://api.thedogapi.com/v1/breeds")
print(response.text)
'''

import requests
response = requests.get("https://api.thecatapi.com/v1/breeds")
print(response.text)