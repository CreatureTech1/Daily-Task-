import tweepy

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAEcMkgEAAAAAt%2BLoyM6eb0YHqWvumcnZ0MQXJ2Q%3D5uYlldfYAJwXSwW8926ZQChLDY5emZBSG8X0ZtQEnkklQjxEZl')

# Replace Tweet ID
id = '1604682463284178949'

users = client.get_retweeters(id=id, user_fields=['profile_image_url'])

for user in users.data:
    print(user)