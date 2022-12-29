import requests

# Enter your Facebook access token
access_token = 'EAAJyAsDAEwkBAIgLQMFZBt1CGEnZAvyPZAZAslHYtJBCXcTaRZBUTpKL1nuyZCbJSeu2Cu5wjHgeHqHklaQM7wmPAg2ltZBwkFja2v45tmvEwZCgWd1qSZCkNyZCDEi0ojQgz8tQZB469RViJtl8w2ChIpzyvs1vyd2OJTZAYRffZBrEAJ08A7ERX5hmXu2wEqRcWpwtBb2qOURW1hoxB6VIZANZCyweqPiYVBgdrgZD'

# Make a request to the /{post-id}/likes endpoint
response = requests.get(
    f'https://graph.facebook.com/v8.0/111244105170838/likes',#100088434655036
    params={'access_token': access_token}
)

# Get the likes from the response
likes = response.json()['data']

# Print the likes
print(likes)