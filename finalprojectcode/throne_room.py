from graphics import *
from final_project_person_class import *
def throneRoom(win):
    throne_room = Image(Point(500, 320), "throne_room.gif")
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
#well well well
    dialogue = Text(Point(500, 720), text_list[0])
    dialogue.setSize(20)
    dialogue.draw(win)
    player_input = win.getKey()
    dialogue.undraw()
#your efforts were in vain
    dialogue = Text(Point(500, 720), text_list[1])
    dialogue.setSize(20)
    dialogue.draw(win)
    player_input = win.getKey()
    dialogue.undraw()
#if shaving_cream == True: press y to attack, n to negotiate, space to use shaving cream   
    battle_file = open ("battle_text.txt", "r")
    battle_text = battle_file.read()
    battle_list = battle_text.split("*")
    battle = True
    while battle == True:
        if "shaving cream" in hero.inventory:
            dialogue = Text(Point(500, 700), "press y to attack\n press n to negotiate\n press s to shave his goatee")
        else:
            dialogue = Text(Point(500, 700), "press y to attack\n press n to negotiate")
#if you choose to attack it changes to a battle scene and runs through a brief account of the battle
        dialogue.setSize(20)
        dialogue.draw(win)
        player_input = win.getKey()
        dialogue.undraw()
        if player_input == "y":
#with what weapon?
            prompt = Text(Point(500,730), battle_list[0])
            prompt.setSize(20)
            prompt.draw(win)
            player_input = win.getKey()
            prompt.undraw()
#you take the pieces out of your backpack
            prompt = Text(Point(500,730), battle_list[1])
            prompt.setSize(20)
            prompt.draw(win)
            player_input = win.getKey()
            prompt.undraw()
#the pieces of metal form a sword
            throne_room.undraw()
            king.undraw()
            zenith.undraw()
            hero.undraw()
            king.undraw()
            sword = Image (Point(500, 400), "sword.gif")
            sword.draw(win)
            prompt = Text(Point(600,730), battle_list[2])
            prompt.setSize(20)
            prompt.draw(win)
            player_input = win.getKey()
            prompt.undraw()
            sword.undraw()
#draw battle background  
            battle_scene = Image(Point (500, 400), "battle_scene.gif")
            battle_scene.draw(win)
            prompt = Text(Point(500, 700), "press space to attack")
            prompt.setSize(20)
            prompt.draw(win)
            player_input = win.getKey()
            prompt.undraw()
            prompt = Text(Point(500, 700), battle_list[3])
            prompt.setSize(20)
            prompt.draw(win)
            player_input = win.getKey()
            prompt.undraw()
            prompt = Text(Point(500, 700), battle_list[4])
            prompt.setSize(20)
            prompt.draw(win)
            player_input = win.getKey()
            prompt.undraw()
            prompt = Text(Point(500, 700), battle_list[5])
            prompt.setSize(20)
            prompt.draw(win)
            player_input = win.getKey()
            prompt.undraw()
            battle = False
            battle_scene.undraw()
        elif player_input == "n":
            prompt = Text (Point(550, 725), "what do you offer the king? \n press y to offer money\n press n to offer power\n press space to offer nothing\n because you are a humble adventurer with nothing to give")
            prompt.setSize(20)
            prompt.draw(win)
            answered = False
            while answered == False:
                player_input = win.getKey()
                if player_input == "y" or player_input == "n" or player_input == " ":
                    answered = True
                    prompt.undraw()
            if player_input == "y":
                response = Text(Point(600, 700), "you have no money to offer\n press Space to continue")
                response.setSize(20)
                response.draw(win)
                player_input = win.getKey()
                response.undraw()
            elif player_input == "n":
                response = Text(Point(600, 700), "you have no power to offer\n press Space to continue")
                response.setSize(20)
                response.draw(win)
                player_input = win.getKey()
                response.undraw()
            elif player_input == " ":
                response = Text(Point(600, 700), "yeah, maybe negotiations were a bad idea\n press Space to continue")
                response.setSize(20)
                response.draw(win)
                player_input = win.getKey()
                response.undraw()
        elif player_input == "s":
            dialogue = Text(Point(600, 700), "you apply shaving cream to the king's face\n and shave off his goatee!\n press Space to continue")
            dialogue.setSize(20)
            dialgue.draw(win)
            player_input = win.getKey()
            dialogue = Text(Point(600, 700), text_list[2])
            dialogue.setSize(20)
            dialgue.draw(win)
            player_input = win.getKey()
            dialogue = Text(Point(600, 700), text_list[3])
            dialogue.setSize(20)
            dialgue.draw(win)
            player_input = win.getKey()
            battle = False
            #add dialogue to the king so that he stops being a homophobe!    
    throne_room.draw(win)
    king.draw(win)
    hero.draw(win)
    zenith.draw(win)
    dialogue = Text(Point(500, 700), battle_list[6])
    dialogue.setSize(20)
    dialogue.draw(win)
    player_input = win.getKey()
    king.undraw()
    dialogue.undraw()
    moving = True
    while moving == True:
        hero.move(40, 40, win)
        if hero.arms.getCenter().getX() < 400 and hero.arms.getCenter().getY() < 700:
            moving = False
    winning_message = Text(Point(500, 300), "You rescued me! Let's get outta here!\n press Space to continue")
    winning_message.setSize(20)
    winning_message.draw(win)
    player_input = win.getKey()
    winning_message.undraw()
    throne_room.undraw()
    zenith.undraw()
    hero.undraw()
    congratulations = Text(Point(500, 400), "Congratulations!\nYou journeyed into adventure and survived!")
    congratulations.setSize(36)
    congratulations.draw(win)
        

