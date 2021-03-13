import requests
from requests.auth import HTTPBasicAuth


def create_access_token(client_id, client_secret, region = 'eu'):
    url = "https://%s.battle.net/oauth/token" % region
    body = {"grant_type": 'client_credentials'}
    auth = HTTPBasicAuth(client_id, client_secret)

    response = requests.post(url, data=body, auth=auth)
    return response.json()