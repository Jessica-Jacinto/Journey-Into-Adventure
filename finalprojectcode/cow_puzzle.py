from graphics import *
from levelintro import *
# creating background
class Grass:
    def __init__(self,win):
        self.grass =Rectangle(Point(0,400), Point(1000,500))
        self.grass.setFill("green")
        self.grassy = Line(Point(700,400), Point(700,350))
        self.grassy.setFill("green")
        self.grassy2 = Line(Point(700,400), Point(680,350))
        self.grassy2.setFill("green")
        self.grassy3 = Line(Point(700,400), Point(720,350))
        self.grassy3.setFill("green")
        self.grassy4 = Line(Point(800,400), Point(800,350))
        self.grassy4.setFill("green")
        self.grassy5 = Line(Point(800,400), Point(780,350))
        self.grassy5.setFill("green")
        self.grassy6 = Line(Point(800,400), Point(820,350))
        self.grassy6.setFill("green")



    def draw(self,win):
        self.grass.draw(win)
        self.grassy.draw(win)
        self.grassy2.draw(win)
        self.grassy3.draw(win)
        self.grassy4.draw(win)
        self.grassy5.draw(win)
        self.grassy6.draw(win)

class Sky:
    def __init__(self,win):
          self.sky = Rectangle(Point(0,0), Point(1000,400))
          self.sky.setFill("blue")
          self.cloud1 = Oval(Point(750,100), Point(830,200))
          self.cloud1.setFill("white")
          self.cloud1.setOutline("white")
          self.cloud2 = Oval(Point(710,100), Point(790,200))
          self.cloud2.setFill("white")
          self.cloud2.setOutline("white")
          self.cloud3 = Oval(Point(690,120), Point(850,180))
          self.cloud3.setFill("white")
          self.cloud3.setOutline("white")
          self.cloud4 = Oval(Point(550,100), Point(630,200))
          self.cloud4.setFill("white")
          self.cloud4.setOutline("white")
          self.cloud5 = Oval(Point(510,100), Point(590,200))
          self.cloud5.setFill("white")
          self.cloud5.setOutline("white")
          self.cloud6 = Oval(Point(490,120), Point(650,180))
          self.cloud6.setFill("white")
          self.cloud6.setOutline("white")
          
          
    def draw(self,win):
        self.sky.draw(win)
        self.cloud1.draw(win)
        self.cloud2.draw(win)
        self.cloud3.draw(win)
        self.cloud4.draw(win)
        self.cloud5.draw(win)
        self.cloud6.draw(win)
        
class Cow:
    def __init__(self,win):
        #legs
        self.back_leg = Rectangle(Point(130,300),Point(160,400))
        self.front_leg = Rectangle(Point(330,300),Point(360,400))

        #body
        self.body = Rectangle(Point(130,200),Point(360,300))

        # head
        self.head = Rectangle(Point(360,120),Point(400,220))

        #ears
        self.left_ear = Polygon(Point(350,130),Point(360,140),Point(360,120))
        self.right_ear = Polygon(Point(410, 130),Point(400,140),Point(400,120))

        #eyes
        self.left_eye = Rectangle(Point(360,155),Point(370,165))
        self.right_eye = Rectangle(Point(390,155),Point(400,165))

        # nostrils
        self.left_nostril = Polygon(Point(360,210),Point(370,220), Point(360,220))
        self.right_nostril = Polygon(Point(390,220),Point(400,210), Point(400,220))

        # tail
        self.tail = Polygon(Point(100,330),Point(90,310),Point(105,300),Point(130,200),Point(130,220),Point(106,300),Point(110,310))
        
        #spots
        self.spot = Oval(Point(150,230),Point(190,250))
        self.spot2 = Oval(Point(320,270),Point(350,280))
        self.spot3 = Oval(Point(230,250),Point(270,270))

          
    def draw(self,win):
        # draw a cow
        self.back_leg.draw(win)
        self.front_leg.draw(win)
        self.body.draw(win)
        self.head.draw(win)
        self.left_ear.draw(win)
        self.right_ear.draw(win)
        self.left_eye.draw(win)
        self.right_eye.draw(win)
        self.left_nostril.draw(win)
        self.right_nostril.draw(win)
        self.tail.draw(win)
        self.spot.draw(win)
        self.spot2.draw(win)
        self.spot3.draw(win)
# resposes to tell user if they did it right or not 
class goodResponse:
    def __init__(self,win):
        self.text_box = Text(Point(300,60), 100)
        self.text_box.setText("Great Job! Press any key to draw the next body part")      
    def draw(self,win):
        self.text_box.setTextColor("white")
        self.text_box.setSize(18)
        self.text_box.draw(win)
    def undraw(self):
        self.text_box.undraw()
        
class badResponse:
    def __init__(self,win):
        self.text_box2 = Text(Point(300,60), 100)
        self.text_box2.setText("hmm, thats not quite right. Press u to undo and try again")
    def draw(self,win):
        self.text_box2.setTextColor("white")
        self.text_box2.setSize(18)
        self.text_box2.draw(win)
    def undraw(self):
        self.text_box2.undraw()
 # for each limb, checks if the points they clicked are close enough to the original
# allows them to undo and redo untill they get it right
def backLeg():        
    p1 = win.getMouse()
    p2 = win.getMouse()
    back_leg = Rectangle(p1,p2)
    back_leg.setFill("white")
    back_leg.draw(win)
    solved = False  
    while solved == False:
        if 135 > p1.getX() >125 and 305 > p1.getY() >295 and 165 > p2.getX()  >155 and 405 > p2.getY() >395:
            good = goodResponse(win)
            good.draw(win)
            win.getKey()
            good.undraw()
            solved = True
        else:
            bad = badResponse(win)
            bad.draw(win)
            a = win.getKey()
            if a == "u":
                bad.undraw()
                back_leg.undraw()
                p1 = win.getMouse()
                p2 = win.getMouse()
                back_leg = Rectangle(p1,p2)
                back_leg.setFill("white")
                back_leg.draw(win)
                a = win.getKey()
            
def frontLeg():
    p3 = win.getMouse()
    p4 = win.getMouse()
    front_leg = Rectangle(p3,p4)
    front_leg.setFill("white")
    front_leg.draw(win)
    solved = False  
    while solved == False:
        if  335> p3.getX() >325 and 305 > p3.getY() >295 and 365 > p4.getX()  >355 and 405 > p4.getY() >395:
            good = goodResponse(win)
            good.draw(win)
            win.getKey()
            good.undraw()
            solved = True
        else:
            bad = badResponse(win)
            bad.draw(win)
            a = win.getKey()
            if a == "u":
                bad.undraw()
                front_leg.undraw()
                p1 = win.getMouse()
                p2 = win.getMouse()
                front_leg = Rectangle(p3,p4)
                front_leg.setFill("white")
                front_leg.draw(win)
                a = win.getKey()
            else:
                bad.undraw()
                front_leg.undraw()
                p1 = win.getMouse()
                p2 = win.getMouse()
                front_leg = Rectangle(p3,p4)
                front_leg.setFill("white")
                front_leg.draw(win)
                a = win.getKey()


def Body():
    #body
    p5 = win.getMouse()
    p6 = win.getMouse()
    body = Rectangle(p5,p6)
    body.setFill("white")
    body.draw(win)
    solved = False  
    while solved == False:
        if  135> p5.getX() >125 and 205 > p5.getY() >195 and 365 > p6.getX()  >355 and 305 > p6.getY() >295:
            good = goodResponse(win)
            good.draw(win)
            win.getKey()
            good.undraw()
            solved = True
        else:
            bad = badResponse(win)
            bad.draw(win)
            a = win.getKey()
            if a == "u":
                bad.undraw()
                body.undraw()
                p5 = win.getMouse()
                p6 = win.getMouse()
                body = Rectangle(p5,p6)
                body.setFill("white")
                body.draw(win)
                a = win.getKey()
            else:
                bad.undraw()
                body.undraw()
                p5 = win.getMouse()
                p6 = win.getMouse()
                body = Rectangle(p5,p6)
                body.setFill("white")
                body.draw(win)
                a = win.getKey()
                
      
        
def Head():
    # head
    p7 = win.getMouse()
    p8 = win.getMouse()
    head = Rectangle(p7,p8)
    head.setFill("white")
    head.draw(win)
    solved = False  
    while solved == False:
        if  365> p7.getX() >355 and 125 > p7.getY() >115 and 405 > p8.getX()  >355 and 225 > p8.getY() >215:
            good = goodResponse(win)
            good.draw(win)
            win.getKey()
            good.undraw()
            solved = True
        else:
            bad = badResponse(win)
            bad.draw(win)
            a = win.getKey()
            if a == "u":
                bad.undraw()
                head.undraw()
                p7 = win.getMouse()
                p8 = win.getMouse()
                head = Rectangle(p7,p8)
                head.setFill("white")
                head.draw(win)
                a = win.getKey()
            else:
                bad.undraw()
                head.undraw()
                p7 = win.getMouse()
                p8 = win.getMouse()
                head = Rectangle(p7,p8)
                head.setFill("white")
                head.draw(win)
                a = win.getKey()
                
        
def leftEar():
    #ears
    p9 = win.getMouse()
    p10 = win.getMouse()
    p11 = win.getMouse()
    left_ear = Polygon(p9,p10,p11)
    left_ear.setFill("white")
    left_ear.draw(win)
    solved = False  
    while solved == False:
        if  355> p9.getX() >345 and 135 > p9.getY() >125 and 365 > p10.getX()  >355 and 145 > p10.getY() >135 and 365 > p11.getX() > 355 and 125 > p11.getY() >115:
            good = goodResponse(win)
            good.draw(win)
            win.getKey()
            good.undraw()
            solved = True
        else:
            bad = badResponse(win)
            bad.draw(win)
            a = win.getKey()
            if a == "u":
                bad.undraw()
                left_ear.undraw()
                p9 = win.getMouse()
                p10 = win.getMouse()
                p11 = win.getMouse()
                left_ear = Polygon(p9,p10,p11)
                left_ear.setFill("white")
                left_ear.draw(win)
                a = win.getKey()
            else:
                bad.undraw()
                left_ear.undraw()
                p9 = win.getMouse()
                p10 = win.getMouse()
                p11 = win.getMouse()
                left_ear = Polygon(p9,p10,p11)
                left_ear.setFill("white")
                left_ear.draw(win)
                a = win.getKey()
                
        
def rightEar():
    p12 = win.getMouse()
    p13 = win.getMouse()
    p14 = win.getMouse()
    right_ear = Polygon(p12,p13,p14)
    right_ear.setFill("white")
    right_ear.draw(win)
    solved = False  
    while solved == False:
        if  415> p12.getX() >405 and 135 > p12.getY() >125 and 405 > p13.getX()  >395 and 145 > p13.getY() >135 and 405 > p14.getX() > 395 and 125 > p14.getY() >115:
            good = goodResponse(win)
            good.draw(win)
            win.getKey()
            good.undraw()
            solved = True
        else:
            bad = badResponse(win)
            bad.draw(win)
            a = win.getKey()
            if a == "u":
                bad.undraw()
                right_ear.undraw()
                p12 = win.getMouse()
                p13 = win.getMouse()
                p14 = win.getMouse()
                right_ear = Polygon(p12,p13,p14)
                right_ear.setFill("white")
                right_ear.draw(win)
                a = win.getKey()
            else:
                bad.undraw()
                right_ear.undraw()
                p12 = win.getMouse()
                p13 = win.getMouse()
                p14 = win.getMouse()
                right_ear = Polygon(p12,p13,p14)
                right_ear.setFill("white")
                right_ear.draw(win)
                a = win.getKey()
                
    
def leftEye():
    #eyes
    p15 = win.getMouse()
    p16 = win.getMouse()
    left_eye = Rectangle(p15,p16)
    left_eye.setFill("black")
    left_eye.draw(win)
    solved = False  
    while solved == False:
        if  365> p15.getX() >355 and 160> p15.getY() >150 and 375 > p16.getX()  >365 and 170 > p16.getY() >160:
            good = goodResponse(win)
            good.draw(win)
            win.getKey()
            good.undraw()
            solved = True
        else:
            bad = badResponse(win)
            bad.draw(win)
            a = win.getKey()
            if a == "u":
                bad.undraw()
                left_eye.undraw()
                p15 = win.getMouse()
                p16 = win.getMouse()
                left_eye = Rectangle(p15,p16)
                left_eye.setFill("black")
                left_eye.draw(win)
                a = win.getKey()
            else:
                bad.undraw()
                left_eye.undraw()
                p15 = win.getMouse()
                p16 = win.getMouse()
                left_eye = Rectangle(p15,p16)
                left_eye.setFill("black")
                left_eye.draw(win)
                a = win.getKey()
                    
    
        
def rightEye():
    p17 = win.getMouse()
    p18 = win.getMouse()
    right_eye = Rectangle(p17,p18)
    right_eye.setFill("black")
    right_eye.draw(win)
    solved = False  
    while solved == False:
        if  395> p17.getX() >385 and 160> p17.getY() >150 and 405 > p18.getX()  >395 and 170 > p18.getY() >160:
            good = goodResponse(win)
            good.draw(win)
            win.getKey()
            good.undraw()
            solved = True
        else:
            bad = badResponse(win)
            bad.draw(win)
            a = win.getKey()
            if a == "u":
                bad.undraw()
                right_eye.undraw()
                p17 = win.getMouse()
                p18 = win.getMouse()
                right_eye = Rectangle(p17,p18)
                right_eye.setFill("black")
                right_eye.draw(win)
                a = win.getKey()
            else:
                bad.undraw()
                right_eye.undraw()
                p17 = win.getMouse()
                p18 = win.getMouse()
                right_eye = Rectangle(p17,p18)
                right_eye.setFill("black")
                right_eye.draw(win)
                a = win.getKey()
                
    
        
##def leftNostril():
##    # nostrils
##    p19 = win.getMouse()
##    p20 = win.getMouse()
##    p36 = win.getMouse()
##    left_nostril = Polygon(p19,p20,p36)
##    left_nostril.setFill("black")
##    left_nostril.draw(win)
##    solved = False  
##    while solved == False:
##        if  365 > p19.getX() >355 and 215 > p19.getY() > 205 and 375 > p20.getX()  >365 and 225 > p20.getY() >215 and 365 > p36.getX > 355 and 225 > p36.getY() > 215:
##            good = goodResponse(win)
##            good.draw(win)
##            win.getKey()
##            good.undraw()
##            solved = True
##        else:
##            bad = badResponse(win)
##            bad.draw(win)
##            a = win.getKey()
##            if a == "u":
##                bad.undraw()
##                left_nostril.undraw()
##                p19 = win.getMouse()
##                p20 = win.getMouse()
##                left_nostril = Line(p19,p20)
##                left_nostril.setFill("black")
##                left_nostril.draw(win)
##                a = win.getKey()
##            else:
##                bad.undraw()
##                left_nostril.undraw()
##                p19 = win.getMouse()
##                p20 = win.getMouse()
##                left_nostril = Line(p19,p20)
##                left_nostril.setFill("black")
##                left_nostril.draw(win)
##                a = win.getKey()
##                
##    
##        
##def rightNostril():
##    p21 = win.getMouse()
##    p22 = win.getMouse()
##    p37 = win.getMouse()
##    right_nostril = Polygon(p21,p22,p37)
##    right_nostril.setFill("black")
##    right_nostril.draw(win)
##    solved = False  
##    while solved == False:
##        if  395> p21.getX() >385 and 215> p21.getY() >205 and 405 > p22.getX()  >395 and 225 > p22.getY() >215 and 405 > p37.getX() > 395 and 225 > p37.getY() > 215:
##            good = goodResponse(win)
##            good.draw(win)
##            win.getKey()
##            good.undraw()
##            solved = True
##        else:
##            bad = badResponse(win)
##            bad.draw(win)
##            a = win.getKey()
##            if a == "u":
##                bad.undraw()
##                right_nostril.undraw()
##                p21 = win.getMouse()
##                p22 = win.getMouse()
##                right_nostril = Line(p21,p22)
##                right_nostril.setFill("black")
##                right_nostril.draw(win)
##                a = win.getKey()
##            else:
##                bad.undraw()
##                right_nostril.undraw()
##                p21 = win.getMouse()
##                p22 = win.getMouse()
##                right_nostril = Line(p21,p22)
##                right_nostril.setFill("black")
##                right_nostril.draw(win)
##                a = win.getKey()
                
def tail():
    # tail
    p23 = win.getMouse()
    p24 = win.getMouse()
    p25 = win.getMouse()
    p26 = win.getMouse()
    p27 = win.getMouse()
    p28 = win.getMouse()
    p29 = win.getMouse()
    tail = Polygon(p23,p24,p25,p26,p27,p28,p29)
    tail.setFill("black")
    tail.draw(win)
    solved = False  
    while solved == False:
        if  105> p23.getX() >95 and 335> p23.getY() >325 and 95 > p24.getX()  >85 and 315 > p24.getY() >305 and 110 > p25.getX() >100 and 305 > p25.getY() >295 and 135 > p26.getX() > 125 and 205 > p26.getY() > 195 and 135 > p27.getX() >125 and 225 > p27.getY() > 215 and  111 > p28.getX() > 101 and  305 > p28.getY() > 295 and  115 > p29.getX() > 105 and 315 > p29.getY() > 305:
            good = goodResponse(win)
            good.draw(win)
            win.getKey()
            good.undraw()
            solved = True
        else:
            bad = badResponse(win)
            bad.draw(win)
            a = win.getKey()
            if a == "u":
                bad.undraw()
                tail.undraw()
                p23 = win.getMouse()
                p24 = win.getMouse()
                p25 = win.getMouse()
                p26 = win.getMouse()
                p27 = win.getMouse()
                p28 = win.getMouse()
                p29 = win.getMouse()
                tail = Polygon(p23,p24,p25,p26,p27,p28,p29)
                tail.setFill("black")
                tail.draw(win)
                a = win.getKey()
            else:
                bad.undraw()
                tail.undraw()
                p23 = win.getMouse()
                p24 = win.getMouse()
                p25 = win.getMouse()
                p26 = win.getMouse()
                p27 = win.getMouse()
                p28 = win.getMouse()
                p29 = win.getMouse()
                tail = Polygon(p23,p24,p25,p26,p27,p28,p29)
                tail.setFill("black")
                tail.draw(win)
                a = win.getKey()
                
    
def spot():
    p30 = win.getMouse()
    p31 = win.getMouse()
    spot = Oval(p30,p31)
    spot.setFill("black")
    spot.draw(win)
    solved = False  
    while solved == False:
        if  155> p30.getX() >145 and 235> p30.getY() >225 and 195 > p31.getX()  >185 and 255 > p31.getY() >245:
            good = goodResponse(win)
            good.draw(win)
            win.getKey()
            good.undraw()
            solved = True
        else:
            bad = badResponse(win)
            bad.draw(win)
            a = win.getKey()
            if a == "u":
                bad.undraw()
                spot.undraw()
                p30 = win.getMouse()
                p31 = win.getMouse()
                spot = Oval(p30,p31)
                spot.setFill("black")
                spot.draw(win)
                a = win.getKey()
            else:
                bad.undraw()
                spot.undraw()
                p30 = win.getMouse()
                p31 = win.getMouse()
                spot = Oval(p30,p31)
                spot.setFill("black")
                spot.draw(win)
                a = win.getKey()
                

def spot2():
    p32 = win.getMouse()
    p33 = win.getMouse()
    spot2 = Oval(p32,p33)
    spot2.setFill("black")
    spot2.draw(win)
    solved = False  
    while solved == False:
        if  325 > p32.getX() >315 and 275> p32.getY() >265 and 355 > p33.getX()  >345 and 285 > p33.getY() >275:
            good = goodResponse(win)
            good.draw(win)
            win.getKey()
            good.undraw()
            solved = True
        else:
            bad = badResponse(win)
            bad.draw(win)
            a = win.getKey()
            if a == "u":
                bad.undraw()
                spot2.undraw()
                p32 = win.getMouse()
                p33 = win.getMouse()
                spot2 = Oval(p32,p33)
                spot2.setFill("black")
                spot2.draw(win)
                a = win.getKey()
            else:
                bad.undraw()
                spot2.undraw()
                p32 = win.getMouse()
                p33 = win.getMouse()
                spot2 = Oval(p32,p33)
                spot2.setFill("black")
                spot2.draw(win)
                a = win.getKey()
                


def spot3():
    p34 = win.getMouse()
    p35 = win.getMouse()
    spot3 = Oval(p34,p35)
    spot3.setFill("black")
    spot3.draw(win)
    solved = False  
    while solved == False:
        if  235> p34.getX() >225 and 255> p34.getY() >245 and 275 > p35.getX()  >265 and 275 > p35.getY() >265:
            good = goodResponse(win)
            good.draw(win)
            win.getKey()
            good.undraw()
            solved = True
        else:
            bad = badResponse(win)
            bad.draw(win)
            a = win.getKey()
            if a == "u":
                bad.undraw()
                spot3.undraw()
                p34 = win.getMouse()
                p35 = win.getMouse()
                spot3 = Oval(p34,p35)
                spot3.setFill("black")
                spot3.draw(win)
                a = win.getKey()
            else:
                bad.undraw()
                spot3.undraw()
                p34 = win.getMouse()
                p35 = win.getMouse()
                spot3 = Oval(p34,p35)
                spot3.setFill("black")
                spot3.draw(win)
                a = win.getKey()
                


class Instructions:
    def __init__(self,win):
        self.text_box = Text(Point(600,210), 100)
        self.text_box.setText("for rectangular limbs: click top left and bottom right")
        self.text_box2 = Text(Point(600,225), 100)
        self.text_box2.setText("for triangles: click all three points")
        self.text_box3 = Text(Point(600,240), 100)
        self.text_box3.setText("for ovals: click upper left and lower right points") 
        self.text_box4 = Text(Point(900,40), 100)
        self.text_box4.setText("fill in limbs in this order") 
        self.text_box5 = Text(Point(900,55), 100)
        self.text_box5.setText("back leg")
        self.text_box6 = Text(Point(900,70), 100)
        self.text_box6.setText("front leg")
        self.text_box7 = Text(Point(900,85), 100)
        self.text_box7.setText("body")
        self.text_box8 = Text(Point(900,100), 100)
        self.text_box8.setText("head")
        self.text_box9 = Text(Point(900,115), 100)
        self.text_box9.setText("left ear")
        self.text_box10 = Text(Point(900,130), 100)
        self.text_box10.setText("right ear ")
        self.text_box11 = Text(Point(900,145), 100)
        self.text_box11.setText("left eye ")
        self.text_box12 = Text(Point(900,160), 100)
        self.text_box12.setText("right eye")
##        self.text_box13 = Text(Point(900,175), 100)
##        self.text_box13.setText("left nostril")
##        self.text_box14 = Text(Point(900,190), 100)
##        self.text_box14.setText("right nostril")
        self.text_box15 = Text(Point(900,175), 100)
        self.text_box15.setText("tail")
        self.text_box16 = Text(Point(900,190), 100)
        self.text_box16.setText("back spot")
        self.text_box17 = Text(Point(900,205), 100)
        self.text_box17.setText("front spot")
        self.text_box18 = Text(Point(900,220), 100)
        self.text_box18.setText("middle spot")
        self.text_box19 = Text(Point(600,255), 100)
        self.text_box19.setText("note: order in which you click the points matters")
        
    def draw(self,win):
        self.text_box.setTextColor("white")
        self.text_box.setSize(12)
        self.text_box.draw(win)
        self.text_box2.setTextColor("white")
        self.text_box2.setSize(12)
        self.text_box2.draw(win)
        self.text_box3.setTextColor("white")
        self.text_box3.setSize(12)
        self.text_box3.draw(win)
        self.text_box4.setTextColor("white")
        self.text_box4.setSize(12)
        self.text_box4.draw(win)
        self.text_box5.setTextColor("white")
        self.text_box5.setSize(12)
        self.text_box5.draw(win)
        self.text_box6.setTextColor("white")
        self.text_box6.setSize(12)
        self.text_box6.draw(win)
        self.text_box7.setTextColor("white")
        self.text_box7.setSize(12)
        self.text_box7.draw(win)
        self.text_box8.setTextColor("white")
        self.text_box8.setSize(12)
        self.text_box8.draw(win)
        self.text_box9.setTextColor("white")
        self.text_box9.setSize(12)
        self.text_box9.draw(win)
        self.text_box10.setTextColor("white")
        self.text_box10.setSize(12)
        self.text_box10.draw(win)
        self.text_box11.setTextColor("white")
        self.text_box11.setSize(12)
        self.text_box11.draw(win)
        self.text_box12.setTextColor("white")
        self.text_box12.setSize(12)
        self.text_box12.draw(win)
##        self.text_box13.setTextColor("white")
##        self.text_box13.setSize(12)
##        self.text_box13.draw(win)
##        self.text_box14.setTextColor("white")
##        self.text_box14.setSize(12)
##        self.text_box14.draw(win)
        self.text_box15.setTextColor("white")
        self.text_box15.setSize(12)
        self.text_box15.draw(win)
        self.text_box16.setTextColor("white")
        self.text_box16.setSize(12)
        self.text_box16.draw(win)
        self.text_box17.setTextColor("white")
        self.text_box17.setSize(12)
        self.text_box17.draw(win)
        self.text_box18.setTextColor("white")
        self.text_box18.setSize(12)
        self.text_box18.draw(win)
        self.text_box19.setTextColor("white")
        self.text_box19.setSize(12)
        self.text_box19.draw(win)
    




    
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
