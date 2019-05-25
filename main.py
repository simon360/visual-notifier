import sys
import time

from notifications.Notifications import Notifications
from outputs.TerminalOutput import TerminalOutput

from services.gmail import Gmail
from services.slack import Slack


def main():
    ns = Notifications()
    o = TerminalOutput(ns)

    gmail = Gmail(ns)
    slack = Slack(ns)

    for i in range(10):
        gmail.refresh()
        slack.refresh()

        o.refresh()
        time.sleep(0.5)


if __name__ == "__main__":
    main()
