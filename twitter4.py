import requests

# Replace these with your own API keys and access tokens
api_key = "V7ALVmIbm9ROBWUg4a1vXSXJA"
api_secret_key = "HAcYjXNlR2n3abvrdyLU1hMbr3zs75k5Ng0K679H326ZuiZJkZ"
access_token = "1295683057-E1XREj7QF6ahpidrod53wAqImIfDPJtm4RnngTz"
access_token_secret = "HclHAjws9i5os673quYfWlXKrtayOEiRJoVpKke7U6jHi"

# Specify the ID of the Tweet you want to retrieve
tweet_id = "1604692545178849280"

# Set up the request header with the necessary authentication information
headers = {
    "Authorization": "Bearer " + access_token
}

# Make the GET request to the API
response = requests.get(
    "https://api.twitter.com/1.1/statuses/show.json",
    params={"id": tweet_id},
    headers=headers
)

# Check the status code of the response to make sure the request was successful
if response.status_code == 200:
    # If the request was successful, parse the JSON data to access the Tweet
    tweet = response.json()
    print(tweet["text"])
else:
    # If the request was not successful, print an error message
    print("Failed to retrieve Tweet. Error code:", response.status_code)