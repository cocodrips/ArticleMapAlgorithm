from rect import Rect
class Page:
    def __init__(self, priority, string, name=None):
        self.priority = priority
        self.original_priority = priority
        self.type = string
        self.rect = Rect()
        self.id = priority
        self.ideal_area = 0
        self.name = name

    def __repr__(self):
        return unicode("<Page priority:{0}>".format(self.priority))

    def __eq__(self, target):
        if isinstance(target, Page):
            return self.id == target.id
        return False
