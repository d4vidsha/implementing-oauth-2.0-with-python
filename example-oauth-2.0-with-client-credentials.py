from requests import request
import json
from datetime import datetime

# constants
SPACE = " "
CLIENT_ID = "some id here"
CLIENT_SECRET = "some secret here"
EVENT_ID = "some event id from lup here"

# obtain access token
url = "https://security.lup.com.au/connect/token"
data = {
    "grant_type": "client_credentials",
    "scope": "oapi"
}
response = request("POST", url, auth=(CLIENT_ID, CLIENT_SECRET), data=data)
print(json.dumps(response.json(), indent=4))
access_token = response.json()["access_token"]
token_type = response.json()["token_type"]

# make the request
now = datetime.now().isoformat()
url = f"https://oapi.lup.com.au/api/v1/events/{EVENT_ID}/visitors"
headers = {
    "Authorization": token_type + SPACE + access_token, 
    "Content-Type": "application/json"
}

response = request("GET", url, headers=headers)
print(response.text)