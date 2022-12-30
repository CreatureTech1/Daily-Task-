import requests

# Enter your Facebook access token and the ID of the page
access_token = 'EAAJyAsDAEwkBANJ6n3ve8ZCEyulZAfd2oZC4pRMjEBlcif2dS9T1CmiZBZB7zaLwXbDs4vSdPK8HEHyPkmi4JOeLMGbBZAJO2BIm9KG1quqZB33QxY3MCmi7qhlP2ytwyzZByMRdx2NQvTLzZAtkCJsJWZC6fstKHArMkXIGKiEo39ZCVeHRZAwKPfh282PmbUm9TUsRwhEBkb9ZAO4MVpeW5NjnC'
page_id = '111215835173665'

# Set the message and other parameters for the post
data = {
    'message': 'Hello, World!',
    'source': ('image.jpeg', open('image.jpeg','rb')),
    'access_token': access_token
}

# Make a request to the /{page-id}/feed endpoint to create a new post
response = requests.post(
    f'https://graph.facebook.com/v8.0/{page_id}/feed',
    data=data
)

status_code = response.status_code
print(status_code)
error = response.json()['error']
print(error)
'''
# Get the ID of the new post from the response
post_id = response.json()['id']

# Print the ID of the new post
print(post_id)
'''


