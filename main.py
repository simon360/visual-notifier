import sys
import time

from notifications.Notifications import Notifications
from outputs.TerminalOutput import TerminalOutput


def main():
    ns = Notifications()
    o = TerminalOutput(ns)
    ns.register('slack', 2)
    ns.register('gmail', 14)

    for i in range(10):
        ns.update('slack', ns.get_badge('slack') + 1)
        ns.update('gmail', ns.get_badge('gmail') - 1)

        o.refresh()
        ns.register('hubblehq', 12)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
