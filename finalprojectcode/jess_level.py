from graphics import *
from sword_shard1 import *
#set up perameters for the window
WIDTH = 1000
HEIGHT = 700

#set up perameters for the table

left_table = 350
right_table = 650



class CupGame:
    def __init__(self, win, position):
        self.move_ud = False
        self.move_side = False
        self.position = position
        self.move1 = False
        self.move2 = False
        self.move3 = False
        self.win = False

 #create cups       
        p1 = Point(position.getX()-125, position.getY())
        p2 = Point(position.getX()-75, position.getY())
        p3 = Point(position.getX()-80, position.getY()-50)
        p4 = Point(position.getX()-120, position.getY()-50)
        self.cup1 = Polygon(p1, p2, p3, p4)
        self.cup1.setFill("blue")



        p1 = Point(position.getX()-25, position.getY())
        p2 = Point(position.getX()+25, position.getY())
        p3 = Point(position.getX()+20, position.getY()-50)
        p4 = Point(position.getX()-20, position.getY()-50)
        self.cup2 = Polygon(p1, p2, p3, p4)
        self.cup2.setFill("blue")
 

        p1 = Point(position.getX()+75, position.getY())
        p2 = Point(position.getX()+125, position.getY())
        p3 = Point(position.getX()+120, position.getY()-50)
        p4 = Point(position.getX()+80, position.getY()-50)
        self.cup3 = Polygon(p1, p2, p3, p4)
        self.cup3.setFill("blue")


#create dots for selection
        p1 = Point(position.getX()-110, position.getY()-30)
        p2 = Point(position.getX()-90, position.getY()-10)
        self.sel1 = Oval(p1, p2)
        self.sel1.setFill("red")

        p1 = Point(position.getX()-10, position.getY()-30)
        p2 = Point(position.getX()+10, position.getY()-10)
        self.sel2 = Oval(p1, p2)
        self.sel2.setFill("red")

        p1 = Point(position.getX()+90, position.getY()-30)
        p2 = Point(position.getX()+110, position.getY()-10)
        self.sel3 = Oval(p1, p2)
        self.sel3.setFill("red")



#create pearls
        p1 = Point(position.getX(), position.getY()-295)
        p2 = Point(position.getX()+20, position.getY()-275)
        self.head_pearl = Oval(p1, p2)
        self.head_pearl.setFill("white")

        self.pearl_rect = Rectangle(p1, p2)


        p1 = Point(position.getX()-10, position.getY()-20)
        p2 = Point(position.getX()+10, position.getY())
        self.pearl = Oval(p1, p2)
        self.pearl.setFill("white")
        


#create rectangles that act as bounding boxes
        p1 = Point(position.getX()-125, position.getY()-60)
        p2 = Point(position.getX()-75, position.getY())
        self.rec1 = Rectangle(p1, p2)
        self.rec1.setFill("blue")

        p1 = Point(position.getX()-25, position.getY()-60)
        p2 = Point(position.getX()+25, position.getY())
        self.rec2 = Rectangle(p1, p2)
        self.rec2.setFill("blue")

        p1 = Point(position.getX()+75, position.getY()-60)
        p2 = Point(position.getX()+125, position.getY())
        self.rec3 = Rectangle(p1, p2)
        self.rec3.setFill("blue")


        

#draw relevant things
    def draw(self, win):
        self.pearl.draw(win)
        self.head_pearl.draw(win)
        self.cup1.draw(win)
        self.cup2.draw(win)
        self.cup3.draw(win)

#undraws everything so the game can restart
    def undrawCupGame(self, win):
        self.head_pearl.undraw()
        self.pearl.undraw()
        self.cup1.undraw()
        self.cup2.undraw()
        self.cup3.undraw()
    
    
                
#select either a cup or the hidden pearl
    def select(self, win):
        while True:
            mouse = win.getMouse()
            if self.rec1.getP1().getX() < mouse.getX() < self.rec1.getP2().getX() and self.rec1.getP1().getY() < mouse.getY() < self.rec1.getP2().getY():
                self.move_ud = True
                self.move1 = True
                self.sel1.draw(win)
                break
            if self.rec2.getP1().getX() < mouse.getX() < self.rec2.getP2().getX() and self.rec2.getP1().getY() < mouse.getY() < self.rec2.getP2().getY():
                self.move_ud = True
                self.move2 = True
                self.sel2.draw(win)
                break
            if self.rec3.getP1().getX() < mouse.getX() < self.rec3.getP2().getX() and self.rec3.getP1().getY() < mouse.getY() < self.rec3.getP2().getY():
                self.move_ud = True
                self.move3 = True
                self.sel3.draw(win)
                break
            if self.pearl_rect.getP1().getX() < mouse.getX() < self.pearl_rect.getP2().getX() and self.pearl_rect.getP1().getY() < mouse.getY() < self.pearl_rect.getP2().getY():
                self.win = True
                self.head_pearl.setFill("red")
                break

#move cups side to side fast
    def moveFast(self, win):
        self.pearl.undraw()
        self.dx1 = -20
        self.dx2 = -20
        self.dx3 = -20
        move_count = 0
        while move_count <= 100:
            self.cup1.move(self.dx1, 0)
            self.rec1.move(self.dx1, 0)
            self.sel1.move(self.dx1, 0)
            
            self.cup2.move(self.dx2, 0)
            self.rec2.move(self.dx2, 0)
            self.sel2.move(self.dx2, 0)
            
            self.cup3.move(self.dx3, 0)
            self.rec3.move(self.dx3, 0)
            self.sel3.move(self.dx3, 0)
            
            
            move_count +=1
            
            if self.rec1.getP1().getX() <= left_table:
                self.dx1 = -self.dx1

            if self.rec1.getP2().getX() >= right_table:
                self.dx1 = -self.dx1

            if self.rec2.getP1().getX() <= left_table:
                self.dx2 = -self.dx2

            if self.rec2.getP2().getX() >= right_table:
                self.dx2 = -self.dx2

            
            if self.rec3.getP1().getX() <= left_table:
                self.dx3 = -self.dx3

            if self.rec3.getP2().getX() >= right_table:
                self.dx3 = -self.dx3


          
        

#move a cup up and down
    def moveUpDown(self, win):
        self.dy = -.5
        if self.move1 == True:
            while self.move_ud == True:
                self.sel1.move(0, self.dy)
                self.cup1.move(0,self.dy)
                self.rec1.move(0,self.dy)

                if self.rec1.getP1().getY() <= self.position.getY()-100:
                    self.dy = -self.dy

                if self.rec1.getP2().getY() >= self.position.getY()+1:
                    self.dy = 0
                    self.move_ud = False
                    self.move1 = False
                    self.sel1.undraw()

                    
        if self.move2 == True or self.npc_move == True:           
            while self.move_ud == True or self.npc_move == True:
                self.sel2.move(0, self.dy)
                self.cup2.move(0,self.dy)
                self.rec2.move(0,self.dy)

                if self.rec2.getP1().getY() <= self.position.getY()-100:
                    self.dy = -self.dy

                if self.rec2.getP2().getY() >= self.position.getY()+1:
                    self.dy = 0
                    self.move_ud = False
                    self.move2 = False
                    self.npc_move = False
                    self.sel2.undraw()

        if self.move3 == True:
            while self.move_ud == True:
                self.sel3.move(0, self.dy)
                self.cup3.move(0,self.dy)
                self.rec3.move(0,self.dy)

                if self.rec3.getP1().getY() <= self.position.getY()-100:
                    self.dy = -self.dy

                if self.rec3.getP2().getY() >= self.position.getY()+1:
                    self.dy = 0
                    self.move_ud = False
                    self.move3 = False
                    self.sel3.undraw()



#mechanics of the game
def letsPlay():
    win = GraphWin("Cups", WIDTH, HEIGHT)

    background = Image(Point(500, 350), "dungeon_back.gif")
    background.draw(win)
    
    genie = Image(Point(500, 300), "genie.gif")
    genie.draw(win)

    p1 = Point(left_table-50, 500)
    p2 = Point(right_table+50, 700)
    table = Rectangle(p1, p2)
    table.setFill("brown")
    table.draw(win)
    
    cont = True
    moving = True
    play = True
    while play == True:
        position2 = Point(500, 500)
        cup = CupGame(win, position2)
        cup.draw(win)

        file = open ("cups.txt", "r")
        text = file.read()
        text_list = text.split("*")
        dialogue = Text(Point (500, 600), text_list[0])
        dialogue.draw(win)

        unanswered = True
        while unanswered == True:
            player_input = win.getKey().lower()
            
            if player_input == "y":
                unanswered = False
                
        if player_input == "y":
            dialogue.undraw()
            dialogue = Text(Point (500, 600), text_list[1])
            dialogue.draw(win)
            cup.npc_move = True
            cup.moveUpDown(win)

            unanswered = True
            while unanswered == True:
                player_input = win.getKey().lower()
                
                if player_input == "y":
                    unanswered = False
                
            if player_input == "y":
                move = True
                dialogue.undraw()
                dialogue = Text(Point (500, 600), text_list[2])
                dialogue.draw(win)

                cup.moveFast(win)

                dialogue.undraw()
                dialogue = Text(Point (500, 600), text_list[3])
                dialogue.draw(win)
                
                cup.select(win)
                cup.moveUpDown(win)
                dialogue.undraw()
                
                if cup.win == True:
                    dialogue = Text(Point (500, 600), text_list[4])
                    dialogue.setSize(20)
                    dialogue.draw(win)

                    shard = Shard_1(500, 550)
                    shard.draw(win)
                    play = False
                    
                else:
                    dialogue = Text(Point (500, 600), text_list[5])
                    dialogue.draw(win)
                    text.close()
                    
                    unanswered = True
                    while unanswered == True:
                        player_input = win.getKey().lower()
                        
                        if player_input == "y":
                            unanswered = False

                    if player_input == "y":
                        dialogue.undraw()
                        dialogue.undraw()
                        cup.undrawCupGame(win)

    win.getKey()
    win.close()
                
                    
            
        


                 
            
        








                
                    
            
        







