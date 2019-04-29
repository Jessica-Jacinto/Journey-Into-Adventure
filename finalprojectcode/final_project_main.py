from lucys_level import *
from jess_level import *
from throne_room import *
from Margarets_level import *
from backstory import *
from graphics import *
from Karis_level import *


def main():
    go()
    win = GraphWin("Console",1000, 800)
    levelOne(win)
    letsPlay()
    this_level()
    throneRoom(win)
    karis_level()
    
   
main()
