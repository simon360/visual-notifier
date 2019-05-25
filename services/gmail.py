class Gmail:
    def __init__(self, ns):
        self.ns = ns
        self.badge = 0

        self.ns.register('gmail', self.badge)

    def refresh(self):
        self.badge = self.badge + 1
        self.ns.update('gmail', self.badge)
