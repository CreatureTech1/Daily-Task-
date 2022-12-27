import tweepy

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAEcMkgEAAAAAt%2BLoyM6eb0YHqWvumcnZ0MQXJ2Q%3D5uYlldfYAJwXSwW8926ZQChLDY5emZBSG8X0ZtQEnkklQjxEZl')

# Replace user ID
id = '2244994945'
users = client.get_users_followers(id=id, user_fields=['profile_image_url'])

for user in users.data:
    print(user.id)