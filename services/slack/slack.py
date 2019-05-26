import json
import os
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

    def refresh(self):
        self.badge = self.badge + 1
        self.ns.update('slack', self.badge)
