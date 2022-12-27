import tweepy

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAEcMkgEAAAAAt%2BLoyM6eb0YHqWvumcnZ0MQXJ2Q%3D5uYlldfYAJwXSwW8926ZQChLDY5emZBSG8X0ZtQEnkklQjxEZl')

# Replace user ID
id = '2244994945'
tweets = client.get_users_mentions(id=id, tweet_fields=['context_annotations','created_at','geo'])

for tweet in tweets.data:
    print(tweet)