import json
import os
import slack
import sys


class Slack:
    def __init__(self, ns, config_dir):
        self.ns = ns
        self.badge = 0

        self.ns.register('slack', self.badge)

        token_loc = os.path.join(config_dir, 'tokens.json')

        if not os.path.exists(token_loc):
            raise RuntimeError(
                "No Slack tokens file exists. Do you need to complete the auth flow?")

        with open(token_loc) as token_file:
            tokens = json.load(token_file)
            self.access_token = tokens["access_token"]

        # pylint: disable=no-member
        self.client = slack.WebClient(token=self.access_token)

        channels_request = self.client.channels_list()
        self.all_channels = [
            channel['id'] for channel in channels_request['channels']]

    def refresh(self):
        self.badge = 0

        for channel in self.all_channels:
            info = self.client.channels_info(channel=channel)
            if info['ok'] and info['channel']['unread_count'] > 0:
                self.badge += info['channel']['unread_count']

        self.ns.update('slack', self.badge)
