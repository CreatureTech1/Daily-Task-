#Authentication
#API key
#NASA
import requests
endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
# Replace DEMO_KEY below with your own key if you generated one.
api_key = "MGYvSPdZbIaRTHfoSQ49q3Ovk6nqrIW1HmWfK8Ko"
query_params = {"api_key": api_key, "earth_date": "2020-07-10"}
response = requests.get(endpoint, params=query_params)
print(response)
#response = requests.get(endpoint, params=query_params).json()
response = requests.get(endpoint, params=query_params)
photos = response.json()["photos"]
print(f"Found {len(photos)} photos")
print(photos[10]["img_src"])