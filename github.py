import requests
# REPLACE the following variables with your Client ID and Client Secret
CLIENT_ID = "0ee7e248caba7abd292c"
CLIENT_SECRET = "31920ad1b11873a04e214f6ffb03621713f60f30"

# REPLACE the following variable with what you added in the
# "Authorization callback URL" field
REDIRECT_URI = "https://httpbin.org/anything"

def create_oauth_link():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "user",
        "response_type": "code",
    }

    endpoint = "https://github.com/login/oauth/authorize"
    response = requests.get(endpoint, params=params)
    url = response.url
    return url


def exchange_code_for_access_token(code=None):
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code,
    }

    headers = {"Accept": "application/json"}
    endpoint = "https://github.com/login/oauth/access_token"
    response = requests.post(endpoint, params=params, headers=headers).json()
    return response["access_token"]

def print_user_info(access_token=None):
    headers = {"Authorization": f"token {access_token}"}
    endpoint = "https://api.github.com/user"
    response = requests.get(endpoint, headers=headers).json()
    name = response["name"]
    username = response["login"]
    private_repos_count = response["total_private_repos"]
    print(
        f"{name} ({username}) | private repositories: {private_repos_count}"
    )    

link = create_oauth_link()
print(f"Follow the link to start the authentication with GitHub: {link}")
code = input("GitHub code: ")
access_token = exchange_code_for_access_token(code)
print(f"Exchanged code {code} with access token: {access_token}")
#print_user_info(access_token)
print_user_info(access_token=access_token)
'''
arun@arun-Lenovo-B490:~/Desktop/arun/api$ python3 github.py
Follow the link to start the authentication with GitHub: https://github.com/login?client_id=0ee7e248caba7abd292c&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D0ee7e248caba7abd292c%26redirect_uri%3Dhttps%253A%252F%252Fhttpbin.org%252Fanything%26response_type%3Dcode%26scope%3Duser
GitHub code: c515b3a2743510fd75ba
Exchanged code c515b3a2743510fd75ba with access token: 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
'''




