from graphics import *
class Shard_1:
    def __init__(self, x, y):
        self.shard_point1 = Point(x, y)
        self.shard_x = x
        self.shard_y = y
        self.shard_point2 = Point(x + 20, y - 5)
        self.shard_point3 = Point(x + 30, y +5)
        self.shard_point4 = Point(x + 5, y + 10)
        self.shard = Polygon(self.shard_point1, self.shard_point2, self.shard_point3, self.shard_point4)
    def draw(self, win):
        shard = Polygon(self.shard_point1, self.shard_point2, self.shard_point3, self.shard_point4)
        self.shard.draw(win)
        self.shard.setFill("Gray")
    def undraw(self):
        self.shard.undraw()
