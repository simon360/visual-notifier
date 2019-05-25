class Notifications:
    def __init__(self):
        self.data = {}

    def register(self, name, badge_num):
        self.data[name] = badge_num

    def update(self, name, badge_num):
        self.data[name] = badge_num

    def get_badge(self, name):
        return self.data[name]

    def get_all(self):
        # Return a copy
        return dict(self.data)
