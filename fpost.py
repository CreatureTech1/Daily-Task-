import requests

# Enter your Facebook access token and the ID of the page
access_token = 'EAAJyAsDAEwkBALRRDIa2oB2upc2jrxt99S4OW2siSELLutQiIA8ccOHUHhZAVY3GFOWhEe1Y9uKYMcu2T1Ou5sJZCGtSecDtISkZCKOt6Dva0ZBZBSLxjqzVtRprz1ixZCZBDVMr4OR5Cs7ZBFFflOzufG5lX2ye38rIMo49nQZCg8jPZC2hcZA4TPR59ZC61YUbE2zpn1S8oHypTCHZBq4LvFHxy'
page_id = '111215835173665'

# Set the message and other parameters for the post
data = {
    'message': 'Hello, World!',
    'access_token': access_token
}

# Make a request to the /{page-id}/feed endpoint to create a new post
response = requests.post(
    f'https://graph.facebook.com/v8.0/{page_id}/feed',
    data=data
)

# Get the ID of the new post from the response
post_id = response.json()['id']

# Print the ID of the new post
print(post_id)

