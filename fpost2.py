import requests

# Replace with your own access token and page ID
access_token = 'EAAJyAsDAEwkBAMEq9I5uOUfl5pZBJEZAs54za22E5anFETUh7TY6hsKQ5GB6SYqYMFCeBW3SfebrWtwhfSsdZB5ZAe7TjZAvCEZBx1ZC2eeokZCU0vYtwljyDLOsrEZAiyMLffcgTbqotgVHGYCioZBXshueXSsZBh0Xt2socELA8tI7iio0n9FP71CiZBNntPpchJgvEmV9NrKFyBK1pN8ZB9pP983sMRpQVpWMZD'
page_id = '111215835173665'

# Set the endpoint URL and version of the API
endpoint_url = f'https://graph.facebook.com/v7.0/{page_id}/feed'

# Set the request headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f'Bearer {access_token}',
}

# Set the request parameters
params = {
    'message': 'This is a test post',
    'media': [{'type': 'image', 'src': ('imgees.jpeg', open('imgees.jpeg', 'rb'))}],
}

# Make the POST request to create the new post
response = requests.post(endpoint_url, headers=headers, params=params)

# Check the status code of the response
status_code = response.status_code
if status_code == 200:
    # The request was successful
    print('Post created successfully!')
else:
    # There was an error
    print('Error creating post:')
    print(response.json())