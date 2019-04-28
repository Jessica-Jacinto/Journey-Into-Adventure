from graphics import *
WIDTH = 1000
HEIGHT = 500
win = GraphWin( "cowLevel", WIDTH, HEIGHT )

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
        self.left_nostril = Line(Point(360,210),Point(370,220))
        self.right_nostril = Line(Point(390,220),Point(400,210))

        # tail
        self.tail = Polygon(Point(100,330),Point(90,310),Point(105,300),Point(130,200),Point(130,220),Point(106,300),Point(110,310))
        
        #spots
        self.spot = Oval(Point(150,230),Point(190,250))
        self.spot2 = Oval(Point(320,270),Point(350,280))
        self.spot3 = Oval(Point(230,250),Point(270,270))

          
    def draw(self,win):
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
 
class goodResponse:
    def __init__(self,win):
        self.text_box = Text(Point(150,60), 80)
        self.text_box.setText("Great Job! Press any key to draw the next leg")      
    def draw(self,win):
        self.text_box.setTextColor("white")
        self.text_box.setSize(18)
        self.text_box.draw(win)
        
class badResponse:
    def __init__(self,win):
        self.text_box2 = Text(Point(300,60), 100)
        self.text_box2.setText("hmm, thats not quite right. Press u to undo and try again")
    def draw(self,win):
        self.text_box2.setTextColor("white")
        self.text_box2.setSize(18)
        self.text_box2.draw(win)
  
def backLeg():        
    p1 = win.getMouse()
    p2 = win.getMouse()
    back_leg = Rectangle(p1,p2)
    back_leg.setFill("white")
    back_leg.draw(win)
    a = win.getKey()
    solved = False
    while solved == False:
        if p1 == (130,300) and p2 == (160,400):
            good = goodResponse(win)
            good.draw(win)
            solved = True
        else:
            bad = badResponse(win)
            bad.draw(win)
            if a == "u":
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

def Body():
    #body
    p5 = win.getMouse()
    p6 = win.getMouse()
    body = Rectangle(p5,p6)
    body.setFill("white")
    body.draw(win)
        
def Head():
    # head
    p7 = win.getMouse()
    p8 = win.getMouse()
    head = Rectangle(p7,p8)
    head.setFill("white")
    head.draw(win)
        
def leftEar():
    #ears
    p9 = win.getMouse()
    p10 = win.getMouse()
    p11 = win.getMouse()
    left_ear = Polygon(p9,p10,p11)
    left_ear.setFill("white")
    left_ear.draw(win)
        
def rightEar():
    p12 = win.getMouse()
    p13 = win.getMouse()
    p14 = win.getMouse()
    right_ear = Polygon(p12,p13,p14)
    right_ear.setFill("white")
    right_ear.draw(win)
def leftEye():
    #eyes
    p15 = win.getMouse()
    p16 = win.getMouse()
    left_eye = Rectangle(p15,p16)
    left_eye.setFill("black")
    left_eye.draw(win)
        
def rightEye():
    p17 = win.getMouse()
    p18 = win.getMouse()
    right_eye = Rectangle(p17,p18)
    right_eye.setFill("black")
    right_eye.draw(win)
        
def leftNostril():
    # nostrils
    p19 = win.getMouse()
    p20 = win.getMouse()
    left_nostril = Line(p19,p20)
    left_nostril.setFill("black")
    left_nostril.draw(win)
        
def rightNostril():
    p21 = win.getMouse()
    p22 = win.getMouse()
    right_nostril = Line(p21,p22)
    right_nostril.setFill("black")
    right_nostril.draw(win)
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
    
def spot():
    p30 = win.getMouse()
    p31 = win.getMouse()
    spot = Oval(p30,p31)
    spot.setFill("black")
    spot.draw(win)

def spot2():
    p32 = win.getMouse()
    p33 = win.getMouse()
    spot2 = Oval(p32,p33)
    spot2.setFill("black")
    spot2.draw(win)

def spot3():
    p34 = win.getMouse()
    p35 = win.getMouse()
    spot3 = Oval(p34,p35)
    spot3.setFill("black")
    spot3.draw(win)
    
def main():
    sky = Sky(win)
    sky.draw(win)
    grass = Grass(win)
    grass.draw(win)
    cow = Cow(win)
    cow.draw(win)
    backLeg()
   
main()
