import requests

# Enter your Facebook access token and the name of the page
access_token = 'EAAJyAsDAEwkBALRRDIa2oB2upc2jrxt99S4OW2siSELLutQiIA8ccOHUHhZAVY3GFOWhEe1Y9uKYMcu2T1Ou5sJZCGtSecDtISkZCKOt6Dva0ZBZBSLxjqzVtRprz1ixZCZBDVMr4OR5Cs7ZBFFflOzufG5lX2ye38rIMo49nQZCg8jPZC2hcZA4TPR59ZC61YUbE2zpn1S8oHypTCHZBq4LvFHxy'
page_name = 'Business Standard'

# Make a request to the /{page-name} endpoint
response = requests.get(
    f'https://graph.facebook.com/v8.0/{page_name}',
    params={'access_token': access_token}
)

# Get the page object from the response
page = response.json()

# Print the ID of the page
print(page)
