import requests

# Enter your Facebook access token and the ID of the post
access_token = 'EAAJyAsDAEwkBAJEdHeDFVFCE2g8APACR5ecS7k2ZCVOmloYoZCvRU61ZAIdh2j1ZAwhTqpCUjHUFA3ZBmH2AaKslidfmZCjqnmZClTF2PQG7ZA2FUijIcTngysLT28tYxZCuSdGqNmqoZCQRGxiUoXlR7huZBUjqGiEVy71NEme6VHRT61Ade2awQvDVKNGj4605G4d7pfHxvxsKT3oGnKo6cwa'
post_id = '111244105170838'

# Make a request to the /{post-id}/comments endpoint
response = requests.get(
    f'https://graph.facebook.com/v8.0/{post_id}/likes',
    params={'access_token': access_token}
)

# Get the comments from the response
likes = response.json()['data']

# Print the comments
print(likes)