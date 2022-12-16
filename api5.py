'''
#Headers
import requests
response = requests.get("https://api.thedogapi.com/v1/breeds/1")
print(response.headers)

import requests
response = requests.get("https://api.thedogapi.com/v1/breeds/1")
print(response.request.headers)

#custom headers
import requests
headers = {"X-Request-Id": "<my-request-id>"}
response = requests.get("https://example.org", headers=headers)
print(response.request.headers)

'''


'''
#content-type
import requests
response = requests.get("https://api.thedogapi.com/v1/breeds/1")
print(response.headers.get("Content-Type"))

import requests
response = requests.get("http://placegoat.com/200/200")
print(response)
print(response.headers.get("Content-Type"))

'''
#Response content
import requests
response = requests.get("https://api.thedogapi.com/v1/breeds/1")
print(response.headers.get("Content-Type"))
print(response.content)
print(response.text)
print(response.json())
print(response.json()['name'])

import requests
response = requests.get("http://placegoat.com/200/200")
print(response.headers.get("Content-Type"))
print(response.content)


import requests
response = requests.get("http://placegoat.com/200/200")
print(response.headers.get("Content-Type"))
file = open("goat.jpeg", "wb")
file.write(response.content)
file.close()
