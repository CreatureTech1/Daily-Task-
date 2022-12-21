import tweepy

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAEcMkgEAAAAAt%2BLoyM6eb0YHqWvumcnZ0MQXJ2Q%3D5uYlldfYAJwXSwW8926ZQChLDY5emZBSG8X0ZtQEnkklQjxEZl')

# Replace with your own search query
query = 'covid -is:retweet'

# Name and path of the file where you want the Tweets written to
file_name = 'tweets.txt'

with open(file_name, 'a+') as filehandle:
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                                  tweet_fields=['context_annotations', 'created_at'], max_results=10).flatten(
            limit=20):
        filehandle.write('%s\n' % tweet.id)