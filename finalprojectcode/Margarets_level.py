from levelintro import *
from cow_puzzle import *

def intro():
    background = BackGround(win)
    background.draw(win)
    oldman = OldMan("old man",win)
    oldman.draw(win)
    instructions = dialogue(win)
    instructions2 = dialogue2(win)
    instructions.draw(win)
    win.getKey()
    instructions.undraw()
    instructions2.draw(win)

def outro():
    background = BackGround(win)
    background.draw(win)
    oldman2 = OldMan("old man2", win)
    oldman2.draw(win)
    outro = winCow(win)
    outro.draw(win)

def cow_level():
    sky = Sky(win)
    sky.draw(win)
    grass = Grass(win)
    grass.draw(win)
    cow = Cow(win)
    cow.draw(win)
    instructions = Instructions(win)
    instructions.draw(win)
    cow2 = Cow(win)
    cow3 = Cow(win)
    backLeg()
    frontLeg()
    Body()
    cow2.draw(win)
    Head()
    cow3.draw(win)
    leftEar()
    rightEar()
    leftEye()
    rightEye()
    tail()
    spot()
    spot2()
    spot3()

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
def my_level():
    
    intro()
    win.getKey()
    cow_level()
    win.getKey()
    outro()
    sword = Shard_1(100,200)
    sword.draw(win)
    text_box7 = Text(Point(180,230), 50)
    text_box7.setText("press any key to continue")
    text_box7.setTextColor("white")
    text_box7.setSize(18)
    text_box7.draw(win)
    win.getKey()
    win.close()

    


    
