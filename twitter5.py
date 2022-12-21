import requests

# Replace these with your own API keys and access tokens
api_key = "b8H0AinqH3wGbVkmpKsldJfKz"
api_secret_key = "5Wyj0ay8Elo5gXdidY6sXcC6ByDrHilVnnXWtY4wWNRJeRhqPS"
access_token = "1295683057-gfcfWdaP3bEp87hus8oMg5GaZDUtTuxM8vCjFF9"
access_token_secret = "yylD20FDA2FloPwoc2WOTh4L2iUSuwUfCJsZ451URB2DB"

# Set up the request header with the necessary authentication information
headers = {
    "Authorization": "Bearer " + access_token
}

# Set the text of the Tweet you want to post
tweet_text = "This is a test Tweet"

# Make the POST request to the API
response = requests.post(
    "https://api.twitter.com/1.1/statuses/update.json",
    params={"status": tweet_text},
    headers=headers
)

# Check the status code of the response to make sure the request was successful
if response.status_code == 200:
    print("Tweet posted successfully!")
else:
    # If the request was not successful, print an error message
    print("Failed to post Tweet. Error code:", response.status_code)