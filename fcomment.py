import requests

# Enter your Facebook access token and the ID of the page
access_token = 'EAAJyAsDAEwkBAJEdHeDFVFCE2g8APACR5ecS7k2ZCVOmloYoZCvRU61ZAIdh2j1ZAwhTqpCUjHUFA3ZBmH2AaKslidfmZCjqnmZClTF2PQG7ZA2FUijIcTngysLT28tYxZCuSdGqNmqoZCQRGxiUoXlR7huZBUjqGiEVy71NEme6VHRT61Ade2awQvDVKNGj4605G4d7pfHxvxsKT3oGnKo6cwa'
page_id = '111215835173665'

# Make a request to the /{page-id}/feed endpoint
response = requests.get(
    f'https://graph.facebook.com/v8.0/111215835173665/feed',
    params={'access_token': access_token}
)

# Get the posts from the response
posts = response.json()['data']

# Iterate through the posts and print the comments
for post in posts:
    if 'comments' in post:
        comments = post['comments']['data']
        for comment in comments:
            print(comment)
