from Final_project_person_class import *
from graphics import *
import time


#put a background image on the window
#character moves across the screen to where an npc is instantiated
#this triggers the dialogue, allowing you to complete the riddle
#once the riddle is solved, a door will appear, the npc will disappear,
#and you will be able to progress to level 2

def levelOne(win):
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
    while unanswered == True:
        player_input = win.getKey().lower()
        if player_input == "w" or player_input == "s":
            unanswered = False
#press w to accept riddle, changes to riddle screen
    if player_input == "w":
        dialogue.undraw()
        background.undraw()
        npc.undraw()
        hero.undraw()
        farm_graph.draw(win)
        while riddle == True:
            dialogue = Text(Point(700, 300), text_list[1])
            dialogue.draw(win)
            player_input = win.getKey().lower()
            dialogue.undraw()
#press s if confused to get a hint
            if player_input == "s":
                hint = Text(Point (700, 300), text_list[2])
                hint.draw(win)
#press w to continue
                player_input = win.getKey().lower
                hint.undraw()
#press w if you have the answer, opens an entry box      
            elif player_input == "w":
#waits for you to enter answer and click the screen
                entry = Entry(Point(700, 500), 10)
                prompt = Text(Point(700, 400), "enter answer here, then click anywhere to check")
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
#if you answer incorrectly, it tells you so then brings you back to the start of the riddle
                else:
                    wrong_answer = Text(Point(600, 700), text_list[3])
                    wrong_answer.draw(win)
                    player_input = win.getKey()
                    entry.undraw()
                    prompt.undraw()
                    wrong_answer.undraw()    
#press w to refuse to solve             
    elif player_input == "s" :
        dialogue.undraw()
        dialogue = Text(Point(600,700), "Fine! don't help me!")
        dialogue.setSize(20)
        dialogue.draw(win)
        riddle = False

    player_input = win.getKey()
    right_answer.undraw()
    dialogue = Text(Point(600, 700), text_list[5])
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
    
def throneRoom(win):
    throne_room = Image(Point(400, 320), "throne_room.gif")
    throne_room.draw(win)
    hero = Player("questa", Point(800, 500), win)
    hero.draw(win)
    king = King("tim", Point(400, 400), win)
    king.draw(win)
    zenith = Cutie("Zenith", Point(200, 400), win)
    zenith.draw(win)
    file = open( "king_dialogue.txt", "r")
    text = file.read()
    text_list = text.split("*")
    dialogue = Text(Point(600, 700), text_list[0])
    dialogue.draw(win)
    player_input = win.getKey()
    dialogue.undraw()
    dialogue = Text(Point(600, 700), text_list[1])
    dialogue.draw(win)
    player_input = win.getKey()
    dialogue.undraw()
    dialogue = Text(Point(600, 700), """press w to kill the king and run
press s to surrender""")
    dialogue.draw(win)
    player_input = win.getKey()
    dialogue.undraw()
    if player_input == "w":
        king.undraw()
        moving = True
        while moving == True:
            hero.move(40, 40, win)
            if hero.arms.getCenter().getX() < 400 and hero.arms.getCenter().getY() < 700:
                moving = False
        winning_message = Text(Point(400, 300), "You rescued me! Let's get outta here!")
        winning_message.draw(win)
    elif player_input == "s":
        throne_room.undraw()
        hero.undraw()
        zenith.undraw()
        king.undraw()
        losing_message = Text(Point(500, 400), "Game Over")
        losing_message.draw(win)
        
        
    
    
    
    
    
    
def main():
    win = GraphWin("Console",1000, 800)
    
    levelOne(win)
    throneRoom(win)
    
    
    
    
    
main()









    
    
