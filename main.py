import os
import sys
import time

from notifications.Notifications import Notifications
from outputs.TerminalOutput import TerminalOutput

from services.gmail.gmail import Gmail
from services.slack import Slack


def main():
    ns = Notifications()
    o = TerminalOutput(ns)

    gmail = Gmail(ns, os.path.join(
        os.path.dirname(__file__), 'services_config/gmail'))
    slack = Slack(ns)

    try:
        while True:
            gmail.refresh()
            slack.refresh()

            o.refresh()
            time.sleep(10)
    except KeyboardInterrupt:
        print('\n\nExiting.\n')


if __name__ == "__main__":
    main()
