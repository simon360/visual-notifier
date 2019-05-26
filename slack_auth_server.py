import json
import os
import slack
import sys
import urllib.parse

from flask import Flask, request

config_dir_loc = os.path.join(
    os.path.dirname(__file__), 'services_config/slack')
creds_loc = os.path.join(config_dir_loc, 'credentials.json')

if not os.path.exists(creds_loc):
    raise RuntimeError("No Slack credentials file exists.")

with open(creds_loc) as creds_file:
    creds = json.load(creds_file)
    client_id = creds["client_id"]
    client_secret = creds["client_secret"]
    client_scopes = creds["client_scopes"]

app = Flask(__name__)


@app.route("/begin_auth", methods=["GET"])
def pre_install():
    params = {
        'scope': client_scopes,
        'client_id': client_id,
        'redirect_uri': 'http://localhost:5172/finish_auth'
    }
    params_str = urllib.parse.urlencode(params)
    return f'<a href="https://slack.com/oauth/authorize?{ params_str }">Add to Slack</a>'


@app.route("/finish_auth", methods=["GET", "POST"])
def post_install():
    # Retrieve the auth code from the request params
    auth_code = request.args['code']

    # An empty string is a valid token for this request
    client = slack.WebClient(token="")

    # Request the auth tokens from Slack
    response = client.oauth_access(
        client_id=client_id,
        client_secret=client_secret,
        code=auth_code
    )

    with open(os.path.join(config_dir_loc, 'tokens.json'), 'w') as tokens_file:
        json.dump({
            'access_token': response['access_token']
        }, tokens_file)

    print("Authentication complete. Quit with ctrl+c.")
    return 'Authentication complete. You can now use Slack visual notifications.'


print("Authenticate by visiting http://localhost:5172/begin_auth")
