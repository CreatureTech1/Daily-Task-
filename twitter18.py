import tweepy



# Replace the text with whatever you want to Tweet about
#response = client.create_tweet(text='hello')

#print(response)





def return_twitterid():
    consumer_key="ZJ3PnSmzbylNkwsZpxOoNBLhs"
    consumer_secret="brYNDraZClBPcjPNBfBUQTQ1q7LgHuP1tQhrWEJtC4vvqqmVG1"
    access_token="1295683057-aQhETUVya0Rcs630cOYW4bAWHb4JnmVUvxtimsz"
    access_token_secret="CTzjEV5EQjc00ezpz4Ws9uTSf29FGIRQB2TieIeXIvJFu"
    # authorization of consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # set access to user's access key and access secret
    auth.set_access_token(access_token, access_token_secret)

    # calling the api
    api = tweepy.API(auth)
    # the screen name of the user
    screen_name = "arunkum77152360"
    print("The screen name is: " + screen_name)
    twitterid = api.get_user(username=screen_name)
    print(type(twitterid)) #to confirm the type of object
    print(f"The Twitter ID is {twitterid.data.id}.")


return_twitterid()
'''
# fetching the user
user = api.get_user(username=screen_name)

# fetching the ID
ID = user.id_str

print("The ID of the user is : " + ID)
'''