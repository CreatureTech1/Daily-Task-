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
api_key = "V7ALVmIbm9ROBWUg4a1vXSXJA"
api_key_secret = "HAcYjXNlR2n3abvrdyLU1hMbr3zs75k5Ng0K679H326ZuiZJkZ"
access_token = "1295683057-E1XREj7QF6ahpidrod53wAqImIfDPJtm4RnngTz"
access_token_secret = "HclHAjws9i5os673quYfWlXKrtayOEiRJoVpKke7U6jHi"

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

put_your_user_id = "869660137"
user1 = api.get_user(user_id = put_your_user_id)
print(user1.name)