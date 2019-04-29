from graphics import *
from Final_project_person_class import *
from random import *

def drawRoom(win):
    #all of the walls for the room
    block1 = Rectangle(Point(38,36),Point(113,72))
    block2 = Rectangle(Point(38,109),Point(113,145))
    block3 = Rectangle(Point(38,182),Point(113,218))
    block4 = Rectangle(Point(38,255),Point(113,291))
    block5 = Rectangle(Point(38,327),Point(113,363))
    block6 = Rectangle(Point(150,36),Point(225,72))
    block7 = Rectangle(Point(150,109),Point(225,145))
    block8 = Rectangle(Point(150,182),Point(225,218))
    block9 = Rectangle(Point(150,255),Point(225,291))
    block10 = Rectangle(Point(150,327),Point(225,363))
    block11 = Rectangle(Point(263,36),Point(338,72))
    block12 = Rectangle(Point(263,109),Point(338,145))
    block13 = Rectangle(Point(263,182),Point(338,218))
    block14 = Rectangle(Point(263,255),Point(338,291))
    block15 = Rectangle(Point(263,327),Point(338,363))
    block16 = Rectangle(Point(375,36),Point(450,72))
    block17 = Rectangle(Point(375,109),Point(450,145))
    block18 = Rectangle(Point(375,182),Point(450,218))
    block19 = Rectangle(Point(375,255),Point(450,291))
    block20 = Rectangle(Point(375,327),Point(450,363))
    block21 = Rectangle(Point(488,36),Point(563,72))
    block22 = Rectangle(Point(488,109),Point(563,145))
    block23 = Rectangle(Point(488,182),Point(563,218))
    block24 = Rectangle(Point(488,255),Point(563,291))
    block25 = Rectangle(Point(488,327),Point(563,363))

    #all of the obstacles in the room
    obstacle1 = Polygon(Point(263,400),Point(263,364),Point(338,364),Point(338,327),Point(375,327),Point(375,364),Point(450,364),
                        Point(450,327),Point(488,327),Point(488,364),Point(563,364),Point(563,327),Point(488,327),Point(488,291),
                        Point(563,291),Point(563,255),Point(488,255),Point(488,218),Point(563,218),Point(563,182),Point(488,182),
                        Point(488,145),Point(563,145),Point(563,109),Point(600,109),Point(600,400))
    obstacle1.setFill("Red")
    
    obstacle2 = Polygon(Point(38,72),Point(113,72),Point(113,36),Point(150,36),Point(150,72),Point(225,72),Point(225,109),
                        Point(150,109),Point(150,145),Point(113,145),Point(113,109),Point(38,109))
    obstacle2.setFill("Silver")
    
    obstacle4 = Circle(Point(244,273),15)
    obstacle4.setFill("Black")
    
    obstacle5 = Circle(Point(131,346),15)
    obstacle5.setFill(color_rgb(55,71,96))
    
    obstacle8_1 = Rectangle(Point(191,223),Point(185,233))
    obstacle8_2 = Rectangle(Point(195,233),Point(181,249))
    obstacle8_1.setFill("Black")
    obstacle8_2.setFill("Black")

    obstacle10 = Circle(Point(300,309),17)
    obstacle10.setFill("Green")
    
    obstacle13 = Polygon(Point(0,182),Point(38,182),Point(38,218),Point(113,218),Point(113,255),Point(38,255),Point(38,291),
                         Point(113,291),Point(113,327),Point(38,327),Point(38,363),Point(0,363))
    obstacle13.setFill("Blue")
    
    obstacle14 = Circle(Point(300,91),13)
    obstacle14.setFill("Green")
    
    obstacle15 = Circle(Point(469,127),13)
    obstacle15.setFill("Black")
    
    obstacle16 =Rectangle(Point(167,149),Point(208,182))
    obstacle16.setFill("SaddleBrown")

    obstacle17 = miniMime("Buddy",Point(411,237),win)
    

    obstacle18 = theRock("Dwayne",Point(298,164),win)

    obstacle19 = Circle(Point(357,200),15)
    obstacle19.setFill("DarkSlateGray")

    obstacle20 = Rectangle(Point(263,0),Point(563,72))
    obstacle20.setFill("Tomato")
    
    block1.setFill("Gray")
    block2.setFill("Gray")
    block3.setFill("Gray")
    block4.setFill("Gray")
    block5.setFill("Gray")
    block6.setFill("Gray")
    block7.setFill("Gray")
    block8.setFill("Gray")
    block9.setFill("Gray")
    block10.setFill("Gray")
    block11.setFill("Gray")
    block12.setFill("Gray")
    block13.setFill("Gray")
    block14.setFill("Gray")
    block15.setFill("Gray")
    block16.setFill("Gray")
    block17.setFill("Gray")
    block18.setFill("Gray")
    block19.setFill("Gray")
    block20.setFill("Gray")
    block21.setFill("Gray")
    block22.setFill("Gray")
    block23.setFill("Gray")
    block24.setFill("Gray")
    block25.setFill("Gray")

    #drawing out the room
    obstacle1.draw(win)
    obstacle2.draw(win)
    obstacle4.draw(win)
    obstacle5.draw(win)
    obstacle8_1.draw(win)
    obstacle8_2.draw(win)
    obstacle10.draw(win)
    obstacle13.draw(win)
    obstacle14.draw(win)
    obstacle15.draw(win)
    obstacle16.draw(win)
    obstacle17.draw(win)
    obstacle18.draw(win)
    obstacle19.draw(win)
    obstacle20.draw(win)

    
    block1.draw(win)
    block2.draw(win)
    block3.draw(win)
    block4.draw(win)
    block5.draw(win)
    block6.draw(win)
    block7.draw(win)
    block8.draw(win)
    block9.draw(win)
    block10.draw(win)
    block11.draw(win)
    block12.draw(win)
    block13.draw(win)
    block14.draw(win)
    block15.draw(win)
    block16.draw(win)
    block17.draw(win)
    block18.draw(win)
    block19.draw(win)
    block20.draw(win)
    block21.draw(win)
    block22.draw(win)
    block23.draw(win)
    block24.draw(win)
    block25.draw(win)


def Puzzle():
    win = GraphWin("Maze",550,550)

    #drawing out the game platform
    line1 = Line(Point(50,0),Point(50,550))
    line2 = Line(Point(100,0),Point(100,550))
    line3 = Line(Point(150,0),Point(150,550))
    line4 = Line(Point(200,0),Point(200,550))
    line5 = Line(Point(250,0),Point(250,550))
    line6 = Line(Point(300,0),Point(300,550))
    line7 = Line(Point(350,0),Point(350,550))
    line8 = Line(Point(400,0),Point(400,550))
    line9 = Line(Point(450,0),Point(450,550))
    line10 = Line(Point(500,0),Point(500,550))
    line11 = Line(Point(0,50),Point(550,50))
    line12 = Line(Point(0,100),Point(550,100))
    line13 = Line(Point(0,150),Point(550,150))
    line14 = Line(Point(0,200),Point(550,200))
    line15 = Line(Point(0,250),Point(550,250))
    line16 = Line(Point(0,300),Point(550,300))
    line17 = Line(Point(0,350),Point(550,350))
    line18 = Line(Point(0,400),Point(550,400))
    line19 = Line(Point(0,450),Point(550,450))
    line20 = Line(Point(0,500),Point(550,500))

    line1.draw(win)
    line2.draw(win)
    line3.draw(win)
    line4.draw(win)
    line5.draw(win)
    line6.draw(win)
    line7.draw(win)
    line8.draw(win)
    line9.draw(win)
    line10.draw(win)
    line11.draw(win)
    line12.draw(win)
    line13.draw(win)
    line14.draw(win)
    line15.draw(win)
    line16.draw(win)
    line17.draw(win)
    line18.draw(win)
    line19.draw(win)
    line20.draw(win)

    #Instructions:
    box = Rectangle(Point(0,400),Point(550,500))
    box.setFill("White")
    message = Text(Point(275,450),"Click to boxes in the right order to unlock the door (you have 49 clicks for 49 spots).")
    box.draw(win)
    message.draw(win)
    win.getClick()

    #The answer to the puzzle is the path through the room
    
    #gets and stores the location of each of the players clicks
    locations = []
    for i in range(49):
        location = win.getMouse()
        point = Circle(location,5)
        point.setFill("Red")
        point.draw(win)
        locations.append(location)

    #checks and stores all of the correct spots
    good_spots = []
    if 500 < locations[0].getX() < 550 and 0 < locations[0].getY() < 50:
        good_spots.append(True)
    if 500 < locations[1].getX() < 550 and 50 < locations[1].getY() < 100:
        good_spots.append(True)
    if 500 < locations[2].getX() < 550 and 100 < locations[2].getY() < 150:
        good_spots.append(True)
    if 450 < locations[3].getX() < 500 and 100 < locations[3].getY() < 150:
        good_spots.append(True)
    if 400 < locations[4].getX() < 450 and 100 < locations[4].getY() < 150:
        good_spots.append(True)
    if 350 < locations[5].getX() < 400 and 100 < locations[5].getY() < 150:
        good_spots.append(True)
    if 300 < locations[6].getX() < 350 and 100 < locations[6].getY() < 150:
        good_spots.append(True)
    if 300 < locations[7].getX() < 350 and 150 < locations[7].getY() < 200:
        good_spots.append(True)
    if 300 < locations[8].getX() < 350 and 200 < locations[8].getY() < 250:
        good_spots.append(True)
    if 350 < locations[9].getX() < 400 and 200 < locations[9].getY() < 250:
        good_spots.append(True)
    if 400 < locations[10].getX() < 450 and 200 < locations[10].getY() < 250:
        good_spots.append(True)
    if 400 < locations[11].getX() < 450 and 250 < locations[11].getY() < 300:
        good_spots.append(True)
    if 400 < locations[12].getX() < 450 and 300 < locations[12].getY() < 350:
        good_spots.append(True)
    if 400 < locations[13].getX() < 450 and 350 < locations[13].getY() < 400:
        good_spots.append(True)
    if 400 < locations[14].getX() < 450 and 400 < locations[14].getY() < 450:
        good_spots.append(True)
    if 350 < locations[15].getX() < 400 and 400 < locations[15].getY() < 450:
        good_spots.append(True)
    if 300 < locations[16].getX() < 350 and 400 < locations[16].getY() < 450:
        good_spots.append(True)
    if 300 < locations[17].getX() < 350 and 350 < locations[17].getY() < 400:
        good_spots.append(True)
    if 300 < locations[18].getX() < 350 and 300 < locations[18].getY() < 350:
        good_spots.append(True)
    if 250 < locations[19].getX() < 300 and 300 < locations[19].getY() < 350:
        good_spots.append(True)
    if 200 < locations[20].getX() < 250 and 300 < locations[20].getY() < 350:
        good_spots.append(True)
    if 200 < locations[21].getX() < 250 and 250 < locations[21].getY() < 300:
        good_spots.append(True)
    if 200 < locations[22].getX() < 250 and 200 < locations[22].getY() < 250:
        good_spots.append(True)
    if 200 < locations[23].getX() < 250 and 150 < locations[23].getY() < 200:
        good_spots.append(True)
    if 200 < locations[24].getX() < 250 and 100 < locations[24].getY() < 150:
        good_spots.append(True)
    if 200 < locations[25].getX() < 250 and 50 < locations[25].getY() < 100:
        good_spots.append(True)
    if 200 < locations[26].getX() < 250 and 0 < locations[26].getY() < 50:
        good_spots.append(True)
    if 150 < locations[27].getX() < 200 and 0 < locations[27].getY() < 50:
        good_spots.append(True)
    if 100 < locations[28].getX() < 150 and 0 < locations[28].getY() < 50:
        good_spots.append(True)
    if 50 < locations[29].getX() < 100 and 0 < locations[29].getY() < 50:
        good_spots.append(True)
    if 0 < locations[30].getX() < 50 and 0 < locations[30].getY() < 50:
        good_spots.append(True)
    if 0 < locations[31].getX() < 50 and 50 < locations[31].getY() < 100:
        good_spots.append(True)
    if 0 < locations[32].getX() < 50 and 100 < locations[32].getY() < 150:
        good_spots.append(True)
    if 0 < locations[33].getX() < 50 and 150 < locations[33].getY() < 200:
        good_spots.append(True)
    if 0 < locations[34].getX() < 50 and 200 < locations[34].getY() < 250:
        good_spots.append(True)
    if 50 < locations[35].getX() < 100 and 200 < locations[35].getY() < 250:
        good_spots.append(True)
    if 100 < locations[36].getX() < 150 and 200 < locations[36].getY() < 250:
        good_spots.append(True)
    if 100 < locations[37].getX() < 150 and 250 < locations[37].getY() < 300:
        good_spots.append(True)
    if 100 < locations[38].getX() < 150 and 300 < locations[38].getY() < 350:
        good_spots.append(True)
    if 100 < locations[39].getX() < 150 and 350 < locations[39].getY() < 400:
        good_spots.append(True)
    if 100 < locations[40].getX() < 150 and 400 < locations[40].getY() < 450:
        good_spots.append(True)
    if 150 < locations[41].getX() < 200 and 400 < locations[41].getY() < 450:
        good_spots.append(True)
    if 200 < locations[42].getX() < 250 and 400 < locations[42].getY() < 450:
        good_spots.append(True)
    if 200 < locations[43].getX() < 250 and 450 < locations[43].getY() < 500:
        good_spots.append(True)
    if 200 < locations[44].getX() < 250 and 500 < locations[44].getY() < 550:
        good_spots.append(True)
    if 150 < locations[45].getX() < 200 and 500 < locations[45].getY() < 550:
        good_spots.append(True)
    if 100 < locations[46].getX() < 150 and 0 < locations[46].getY() < 550:
        good_spots.append(True)
    if 50 < locations[47].getX() < 100 and 0 < locations[47].getY() < 550:
        good_spots.append(True)
    if 0 < locations[48].getX() < 50 and 0 < locations[48].getY() < 550:
        good_spots.append(True)
            
    #If all of the spots were correct then you win
    if len(good_spots) == 49:
        box = Rectangle(Point(0,400),Point(550,500))
        box.setFill("White")
        message = Text(Point(275,450),"Correct! \nThe door opens and a piece of a sword falls \nfrom where it was wedged in the frame.")
        box.draw(win)
        message.draw(win)
        win.getClick()
        win.close()
    else:
        box = Rectangle(Point(0,425),Point(550,475))
        box.setFill("White")
        message = Text(Point(275,450),"Wrong, you lose.")
        box.draw(win)
        message.draw(win)
        win.getClick()
        win.close()
        
        
def main():
    truth = True
    win = GraphWin("boogies",600,400)

    tom = bittyBro("tom",Point(580,20),win)
    drawRoom(win)
    tom.draw(win)

    #moving the character and checking to see if the end of the level was reached
    while truth == True:
        tom.moveKarisLevel(6,6,win)
        if 5 < tom.getX() < 13 and ( 363 < tom.getY()+1.5 < 400 ):
            Puzzle()
            win.close()
main()
