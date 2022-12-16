import requests
response = requests.get("https://api.thedogapi.com/v1/breeds")
print(response.text)
print(response)
print(response.request)
request =response.request
print(request.url)
print(request.path_url)
print(request.headers)
print(request.method)
print(response.status_code)
print(response.headers)
print(response.reason)

#falling request
response = requests.get("https://api.thedogapi.com/v1/breedz")
print(response)
print(response.status_code)
print(response.reason)