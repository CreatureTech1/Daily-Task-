#Query parameter
import requests
response = requests.get("https://randomuser.me/api/")
print(response)
response = requests.get("https://randomuser.me/api/").json()
print(response)
response = requests.get("https://randomuser.me/api/?gender=female").json()
print(response)
response = requests.get("https://randomuser.me/api/?gender=female&nat=de").json()
print(response)

query_param = {"gender":"female","nat":"de"}
response = requests.get("https://randomuser.me/api/",params=query_param).json()
print(response)


query_params = {"q": "labradoodle"}
endpoint = "https://api.thedogapi.com/v1/breeds/search"
reponse =requests.get(endpoint, params=query_params).json()
print(response)
