from Final_project_person_class import *
from graphics import *
import time
from sword_shard1 import *


#put a background image on the window
#character moves across the screen to where an npc is instantiated
#this triggers the dialogue, allowing you to complete the riddle
#once the riddle is solved, a door will appear, the npc will disappear,
#and you will be able to progress to level 2

def lucys_level(win):
    hero = Player("questa", Point(950, 450), win)
    door_1 = Point(40, 203)
    door_2 = Point (124, 130)
    door_3 = Point (124, 515)
    door_4 = Point (40, 588)
    door = Polygon(door_1, door_2, door_3, door_4)
    door.setFill("saddle brown")
    door.setOutline("saddle brown")
    background = Image(Point(520, 400), "final_project_background_1.gif")
    background.draw(win)
    hero.draw(win)
    npc = Person("farmer", Point(200, 450), win)
    npc.draw(win)
    farm_graph = Image(Point(500, 400), "math_riddle.gif")
#creates a loop of intereacting with farmer until you solve the riddle
    unsolved = True
    while unsolved == True:
        moving = True
        while moving == True:
            hero.move(40, 40, win)
            if hero.arms.getCenter().getX() < 420:
                moving = False
        file = open ("npc_1.txt", "r")
        text = file.read()
        text_list = text.split("*")
        riddle = True
        dialogue = Text(Point (600, 700), text_list[0])
        dialogue.setSize(20)
        dialogue.draw(win)
        unanswered = True
#loops until it gets an acceptable response
        while unanswered == True:
            player_input = win.getKey().lower()
            if player_input == "y" or player_input == "n":
                unanswered = False
#press w to accept riddle, changes to riddle screen
        if player_input == "y":
            dialogue.undraw()
            background.undraw()
            npc.undraw()
            hero.undraw()
            farm_graph.draw(win)
            while riddle == True:
                dialogue = Text(Point(700, 300), text_list[1])
                dialogue.setSize(18)
                dialogue.draw(win)
                player_input = win.getKey().lower()
                dialogue.undraw()
#press s if confused to get a hint
                if player_input == "n":
                    hint = Text(Point (700, 300), text_list[2])
                    hint.draw(win)
#press w to continue
                    player_input = win.getKey().lower
                    hint.undraw()
#press w if you have the answer, opens an entry box      
                elif player_input == "y":
#waits for you to enter answer and click the screen
                    entry = Entry(Point(700, 500), 10)
                    prompt = Text(Point(700, 400), "enter answer here, then click anywhere to check")
                    prompt.setSize(20)
                    prompt.draw(win)
                    entry.draw(win)
                    point = win.getMouse()
                    answer = entry.getText()
#if you input the correct response, you exit the riddle screen    
                    if answer== "22" or "twenty-two":
                        riddle = False
                        entry.undraw()
                        farm_graph.undraw()
                        dialogue.undraw()
                        prompt.undraw()
                        background.draw(win)
                        npc.draw(win)
                        hero.draw(win)
                        right_answer = Text(Point(600, 700), text_list[4])
                        right_answer.draw(win)
                        unsolved = False
#if you answer incorrectly, it tells you so then brings you back to the start of the riddle
                    else:
                        wrong_answer = Text(Point(600, 700), text_list[3])
                        wrong_answer.draw(win)
                        player_input = win.getKey()
                        entry.undraw()
                        prompt.undraw()
                        wrong_answer.undraw()    
#press w to refuse to solve             
        elif player_input == "n" :
            dialogue.undraw()
            dialogue = Text(Point(600,700), "Fine! don't help me!\n Press space to continue")
            dialogue.setSize(20)
            dialogue.draw(win)
            player_input = win.getKey()
            dialogue.undraw()
            hero.undraw()
            hero = Player("questa", Point(500, 450), win)
            hero.draw(win)
            #riddle = False
#escape the while loop,
    player_input = win.getKey()
    right_answer.undraw()
#character gives you a shard of metal
    shard = Shard_1(230, 470)
    shard.draw(win)
    dialogue = Text(Point(600, 700), text_list[5])
    dialogue.setSize(20)
    dialogue.draw(win)
    accepted = False
    while accepted == False:
        player_input = win.getKey()
        if player_input == "y":
            accepted = True
            dialogue.undraw()
    dialogue = Text(Point(600, 700), "You have gained one shard of metal! \n You place it in your inventory\n press Space to continue")
    dialogue.setSize(20)
    shard.undraw()
    dialogue.draw(win)
    player_input = win.getKey()
    dialogue.undraw()
    dialogue = Text(Point(600, 700), text_list[6])
    dialogue.setSize(20)
    dialogue.draw(win)
    door.draw(win)
    moving = True
    while moving == True:
        hero.move(40, 40, win)
        if hero.arms.getCenter().getX() < 200:
            moving = False
    file.close()
    hero.undraw()
    npc.undraw()
    background.undraw()
    door.undraw()
    dialogue.undraw()
    









    
    
