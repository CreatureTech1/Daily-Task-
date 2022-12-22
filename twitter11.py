#6. Getting Tweets with user information, for each Tweet
import tweepy

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAEcMkgEAAAAAt%2BLoyM6eb0YHqWvumcnZ0MQXJ2Q%3D5uYlldfYAJwXSwW8926ZQChLDY5emZBSG8X0ZtQEnkklQjxEZl')

# Replace with your own search query
query = 'covid -is:retweet'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                     user_fields=['profile_image_url'], expansions='author_id', max_results=15)

# Get users list from the includes object
users = {u["id"]: u for u in tweets.includes['users']}

for tweet in tweets.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        print(user.profile_image_url)
        print(tweet.author_id)