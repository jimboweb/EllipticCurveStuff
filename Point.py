class Point:
    #need a way to represent infinity.
    def __init__(self, x,y, infinity = False):
        self.infinity = infinity
        if infinity:
            self.x = None
            self.y = None
        else:
            self.x = x
            self.y = y
