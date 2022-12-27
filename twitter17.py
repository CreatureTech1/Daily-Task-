import tweepy

client = tweepy.Client(consumer_key='ZJ3PnSmzbylNkwsZpxOoNBLhs',
                       consumer_secret='brYNDraZClBPcjPNBfBUQTQ1q7LgHuP1tQhrWEJtC4vvqqmVG1',
                       access_token='1295683057-aQhETUVya0Rcs630cOYW4bAWHb4JnmVUvxtimsz',
                       access_token_secret='CTzjEV5EQjc00ezpz4Ws9uTSf29FGIRQB2TieIeXIvJFu')

# Replace the text with whatever you want to Tweet about
#response = client.create_tweet(text='hello')

#print(response)

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

# the screen name of the user
screen_name = "geeksforgeeks"

# fetching the user
user = api.get_user(screen_name)

# fetching the ID
ID = user.id_str

print("The ID of the user is : " + ID)