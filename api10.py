#Giphy
#jvLqJwGxW5xW7FMlcQ6lfPh1DCMyfrVe
'''
import requests
# Replace the following with the API key generated.
API_KEY = "jvLqJwGxW5xW7FMlcQ6lfPh1DCMyfrVe"
endpoint = "https://api.giphy.com/v1/gifs/trending"
params = {"api_key": API_KEY, "limit": 3, "rating": "g"}
response = requests.get(endpoint, params=params).json()
for gif in response["data"]:

    title = gif["title"]

    trending_date = gif["trending_datetime"]

    url = gif["url"]

    print(f"{title} | {trending_date} | {url}")
'''

import requests
# Replace the following with the API key generated.
API_KEY = "jvLqJwGxW5xW7FMlcQ6lfPh1DCMyfrVe"
endpoint = "https://api.giphy.com/v1/gifs/trending"
search_term = "shrug"
params = {"api_key": API_KEY, "limit": 1, "q": search_term, "rating": "g"}
response = requests.get(endpoint, params=params).json()
for gif in response["data"]:
    title = gif["title"]
    url = gif["url"]
    print(f"{title} | {url}")

