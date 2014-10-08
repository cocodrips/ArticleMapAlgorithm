# -*- coding: utf-8 -*-
IMAGE_RATIO = 1.3
class Rect:
    x = 0
    y = 0
    width = 0
    height = 0

    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def ratio(self):
        return self.width / float(self.height)

    def vec4(self):
        return (self.x, self.y, self.width, self.height)

    def __repr__(self):
        return unicode("<{}, {}, {}, {}>".format(self.x, self.y, self.width, self.height))
