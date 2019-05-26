# Visual notifier

> Puts badge numbers from various services in one place.

## Configuring

Currently, configuration is highly manual.

### Gmail

See [the service configuration README.md](services_config/gmail/README.md).

### Slack

See [the service configuration README.md](services_config/slack/README.md).

Get OAuth tokens by running `FLASK_APP=slack_auth_server.py python3 -m flask run -h localhost -p 5172`, and following the instructions.

## Running

Requires Python 3.

Install dependencies with `pip` or `pip3`:

```sh
pip3 install -r requirements.txt
```

Run with `python` or `python3`:

```sh
python3 main.py
```

## Why?

For fun, mostly. For an excuse to play around with a Raspberry Pi, and GPIO, and Python.

But also, because peripheral vision is handy. The ultimate application of this is a small, secondary screen that sits on your desk - think of a desk clock - which shows icons with badges when you:

- have unread emails
- have unread Slack messages
- have new Twitter notifications
- haven't activated your time tracker

You might think: isn't that what the dock is for, or why we have Notification Centre, or what our phones are for?

Sure, but some people miss those. For example, someone using screen zooming might not see notifications as they arrive, or someone in full-screen mode might not see a badge on their dock. Hey, maybe someone's working with honest-to-goodness pen and paper.
