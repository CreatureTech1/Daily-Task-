import tweepy

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAEcMkgEAAAAAt%2BLoyM6eb0YHqWvumcnZ0MQXJ2Q%3D5uYlldfYAJwXSwW8926ZQChLDY5emZBSG8X0ZtQEnkklQjxEZl')

# Replace with your own search query
query = 'covid -is:retweet has:media'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                     media_fields=['preview_image_url'], expansions='attachments.media_keys',
                                     max_results=15)

# Get list of media from the includes object
media = {m["media_key"]: m for m in tweets.includes['media']}

for tweet in tweets.data:
    attachments = tweet.data['attachments']
    media_keys = attachments['media_keys']
    print(tweet.text)
    if media[media_keys[0]].preview_image_url:
        print(media[media_keys[0]].preview_image_url)