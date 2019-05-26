# Slack notification service

Derived from https://github.com/slackapi/python-slackclient/blob/master/documentation_v2/auth.md

## Usage

The `credentials.json` file should contain these keys:

- `client_id`: the client ID when the app was registered
- `client_secret`: the client secret when the app was registered
- `client_scopes`: a comma-separated list of scopes for the app. Recommended: `"channels:history,channels:read,groups:history,groups:read,im:history,im:read,mpim:history,mpim:read"`. Ensure these are all enabled in the app itself, too.

You can create a new app [here](https://api.slack.com/apps/) to get these values.
