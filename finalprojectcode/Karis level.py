from graphics import *
from Final_project_person_class import *
from random import *


def drawRoom(win):
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

    obstacle1 = Polygon(Point(263,400),Point(263,364),Point(338,364),Point(338,327),Point(375,327),Point(375,364),Point(450,364),
                        Point(450,327),Point(488,327),Point(488,364),Point(563,364),Point(563,327),Point(488,327),Point(488,291),
                        Point(563,291),Point(563,255),Point(488,255),Point(488,218),Point(563,218),Point(563,182),Point(488,182),
                        Point(488,145),Point(563,145),Point(563,109),Point(600,109),Point(600,400))
    obstacle1.setFill("Red")
    
    obstacle2 = Polygon(Point(38,72),Point(113,72),Point(113,36),Point(150,36),Point(150,72),Point(225,72),Point(225,109),
                        Point(150,109),Point(150,145),Point(113,145),Point(113,109),Point(38,109))
    obstacle2.setFill("Orange") #fix color
    
    obstacle4 = Circle(Point(244,273),15)
    obstacle4.setFill("Black")
    
    obstacle5 = Circle(Point(131,346),15)
    obstacle5.setFill("Black")#fix color
    
    obstacle8_1 = Rectangle(Point(191,223),Point(185,233))
    obstacle8_2 = Rectangle(Point(195,233),Point(181,249))
    obstacle8_1.setFill("Black")
    obstacle8_2.setFill("Black")

    obstacle10 = Circle(Point(300,309),17)
    obstacle10.setFill("Green")
    
    obstacle13 = Polygon(Point(0,182),Point(38,182),Point(38,218),Point(113,218),Point(113,255),Point(38,255),Point(38,291),
                         Point(113,291),Point(113,327),Point(38,327),Point(38,363),Point(0,363))
    obstacle13.setFill("Blue")
    
    obstacle14 = Rectangle(Point(263,72),Point(338,109))
    obstacle14.setFill("Green")
    
    obstacle15 = Circle(Point(469,127),13)
    obstacle15.setFill("Black")
    
    obstacle16 =Rectangle(Point(167,149),Point(208,182))
    obstacle16.setFill("SaddleBrown")

    obstacle17 = miniMime("Buddy",Point(411,237),win)
    

    obstacle18 = theRock("Dwayne",Point(298,164),win)

    obstacle19 = Circle(Point(200,357),15)
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

def checkurself(win):
    block = Rectangle(Point(5,5),Point(595,395))
    block.draw(win)
    x=randint(0,600)
    y=randint(0,400)
    point = Point(x,y)
    
    if 5<=point.getX()<=595 and 5<=point.getY()<=395:
        print("yeah dude")
    else:
        print("you stink loser. \nFry, pizza goin out, CMAHN!!!")

def main():
    truth = True
    win = GraphWin("boogies",600,400)

    tom = bittyBro("tom",Point(580,20),win)
    drawRoom(win)
    tom.draw(win)

##    key = win.getKey()
##    if key == "p" : 
##        truth = False
##    elif 38<tom.getX()<113 and 36<tom.getY()<72 and key == d:
##        truth = False
##    else:
##        truth = True
    while truth == True:
        tom.moveKarisLevel(6,6,win)
main()
