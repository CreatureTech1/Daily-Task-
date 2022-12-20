'''
API key
V7ALVmIbm9ROBWUg4a1vXSXJA

API key Secret
HAcYjXNlR2n3abvrdyLU1hMbr3zs75k5Ng0K679H326ZuiZJkZ

Bearer token
AAAAAAAAAAAAAAAAAAAAAEcMkgEAAAAAvD%2Bsi4g8KxqpD6M0mzEIhQ9vJ7o%3Dh9TrpynrhrvQMJCh2ABsm4ys9yQtrKwA4EmRJliIaT00FMPBhn

Access Token
1295683057-E1XREj7QF6ahpidrod53wAqImIfDPJtm4RnngTz

Access Token Secret
HclHAjws9i5os673quYfWlXKrtayOEiRJoVpKke7U6jHi
'''

import tweepy

# Set up your Twitter API credentials
consumer_key = "V7ALVmIbm9ROBWUg4a1vXSXJA"
consumer_secret = "HAcYjXNlR2n3abvrdyLU1hMbr3zs75k5Ng0K679H326ZuiZJkZ"
access_token = "1295683057-E1XREj7QF6ahpidrod53wAqImIfDPJtm4RnngTz"
access_token_secret = "HclHAjws9i5os673quYfWlXKrtayOEiRJoVpKke7U6jHi"

# Authenticate with the Twitter API
endpoints = "https://api.twitter.com/2/tweets/search/recent"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets
query = "python"
date_since = "2022-12-16"
tweets = tweepy.Cursor(api.search_tweets,q=query,lang="en",since=date_since).items(5)

# Print the tweets
for tweet in tweets:
    print(tweet.text)
