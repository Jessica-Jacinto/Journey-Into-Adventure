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


def my_level():
    intro()
    win.getKey()
    cow_level()
    win.getKey()

    outro()
my_level()
    


    
