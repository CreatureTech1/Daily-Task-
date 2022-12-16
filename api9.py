#Pagination
import requests
response = requests.get("https://api.github.com/events?per_page=1&page=0")
print(response.json()[0]["id"])
#'14345572615'
response = requests.get("https://api.github.com/events?per_page=1&page=1")
print(response.json()[0]["id"])
#'14345572808'
response = requests.get("https://api.github.com/events?per_page=1&page=2")
print(response.json()[0]["id"])
#'14345572100'