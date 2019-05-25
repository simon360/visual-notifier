import sys


class TerminalOutput:
    def __init__(self, ns, out=sys.stdout):
        self.ns = ns
        self.out = out

    def refresh(self):
        badges = self.ns.get_all()
        badges_list = badges.items()

        badges_strings = ["%s: %i" % (name, badge)
                          for [name, badge] in badges_list]

        self.out.write("\r%s" % (', '.join(badges_strings)))
        self.out.flush()
