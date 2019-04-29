from graphics import *
WIDTH = 1000
HEIGHT = 500
win = GraphWin( "myLevel", WIDTH, HEIGHT )
class BackGround:
    def __init__(self,win):
        # draw the background
       self.back_ground = Image(Point(WIDTH/2, HEIGHT/2), "cell.png")
    def draw(self,win):
        self.back_ground.draw(win)
    def undraw():
        self.back_ground.undraw()
        


class OldMan:
    def __init__(self, name,win):
        self.name = name

        # head
        self.head = Oval(Point(350,50), Point(700,450))
        self.head.setFill("pink")
        self.head.setOutline("pink")

        # ears
        self.left_ear = Oval(Point(360,220),Point(300,300))
        self.left_ear.setFill("pink")
        self.left_ear.setOutline("pink")
        self.right_ear = Oval(Point(690,220),Point(750,300))
        self.right_ear.setFill("pink")
        self.right_ear.setOutline("pink")
        self.left_hole = Oval(Point(330,260), Point(340,280))
        self.left_hole.setFill("black")
        self.right_hole = Oval(Point(710,260), Point(720,280))
        self.right_hole.setFill("black")
        

        # eyes
        self.left_eye= Oval(Point(400,260),Point(450,290))
        self.left_eye.setFill("white")
        self.left_pupil= Oval(Point(410,265), Point(440, 285))
        self.left_pupil.setFill("black")
        self.right_eye = Oval(Point(600,260), Point(650,290))
        self.right_eye.setFill("white")
        self.right_pupil = Oval(Point(610,265),Point(640,285))
        self.right_pupil.setFill("black")

        # mouth
        self.top_lip = Polygon(Point(450,350), Point(520,340),Point(525,345),Point(530,340),Point(600,350))
        self.top_lip.setFill("red")
        self.bottom_lip = Polygon(Point(450,350),Point(525,370),Point(600,350))
        self.bottom_lip.setFill("red")

        #eye brows

        self.left_brow = Polygon(Point(400,245),Point(425,240), Point(450, 245))
        self.left_brow.setFill("grey")
        self.left_brow.setOutline("grey")
        self.right_brow = Polygon(Point(600,245),Point(625,240),Point(650,245))
        self.right_brow.setFill("grey")
        self.right_brow.setOutline("grey")

        #nose
        self.left_nostril = Oval(Point(510,320), Point(520, 330))
        self.left_nostril.setFill("brown")
        self.right_nostril = Oval(Point(530,320),Point(540,330))
        self.right_nostril.setFill("brown")
        self.nose_bridge = Line(Point(525,260),Point(530,330))
        self.nose_tip = Line(Point(530,330), Point(520,332))
        self.nose_skin = Oval(Point(500,320),Point(515,330))
        self.nose_skin.setFill("pink")
        self.nose_skin2 = Oval(Point(530,320),Point(545,330))
        self.nose_skin2.setFill("pink")

        # wrinkles
        self.mouth_wrinkle = Line(Point(440,340), Point(430, 360))
        self.mouth_wrinkle2 = Line(Point(610,340), Point(620, 360))
        self.forehead_wrinkle = Line(Point(400,200),Point(650,200))
        self.forehead_wrinkle2 = Line(Point(400,190), Point(650,190))
        self.forehead_wrinkle3 = Line(Point(400,180), Point(650,180))
        self.left_eye_wrinkle = Line(Point(370,270), Point(390,270))
        self.left_eye_wrinkle2 = Line(Point(370,280),Point(390,270))
        self.left_eye_wrinkle3 = Line(Point(370,260),Point(390,270))
        self.right_eye_wrinkle = Line(Point(660,270), Point(680,270))
        self.right_eye_wrinkle2 = Line(Point(660,270),Point(680,280))
        self.right_eye_wrinkle3 = Line(Point(660,270),Point(680,260))
        
        
        
        
            
        
    def draw(self,win):
        self.head.draw(win)
        self.left_ear.draw(win)
        self.right_ear.draw(win)
        self.left_hole.draw(win)
        self.right_hole.draw(win)
        self.left_eye.draw(win)
        self.left_pupil.draw(win)
        self.right_eye.draw(win)
        self.right_pupil.draw(win)
        self.top_lip.draw(win)
        self.bottom_lip.draw(win)
        self.left_brow.draw(win)
        self.right_brow.draw(win)
        self.nose_skin.draw(win)
        self.left_nostril.draw(win)
        self.nose_skin2.draw(win)
        self.right_nostril.draw(win)
        self.nose_bridge.draw(win)
        self.nose_tip.draw(win)
        self.mouth_wrinkle.draw(win)
        self.mouth_wrinkle2.draw(win)
        self.forehead_wrinkle.draw(win)
        self.forehead_wrinkle2.draw(win)
        self.forehead_wrinkle3.draw(win)
        self.left_eye_wrinkle.draw(win)
        self.left_eye_wrinkle2.draw(win)
        self.left_eye_wrinkle3.draw(win)
        self.right_eye_wrinkle.draw(win)
        self.right_eye_wrinkle2.draw(win)
        self.right_eye_wrinkle3.draw(win)

    def undraw(self):
        self.head.undraw()
        self.left_ear.undraw()
        self.right_ear.undraw()
        self.left_hole.undraw()
        self.right_hole.undraw()
        self.left_eye.undraw()
        self.left_pupil.undraw()
        self.right_eye.undraw()
        self.right_pupil.undraw()
        self.top_lip.undraw()
        self.bottom_lip.undraw()
        self.left_brow.undraw()
        self.right_brow.undraw()
        self.nose_skin.undraw()
        self.left_nostril.undraw()
        self.nose_skin2.undraw()
        self.right_nostril.undraw()
        self.nose_bridge.undraw()
        self.nose_tip.undraw()
        self.mouth_wrinkle.undraw()
        self.mouth_wrinkle2.undraw()
        self.forehead_wrinkle.undraw()
        self.forehead_wrinkle2.undraw()
        self.forehead_wrinkle3.undraw()
        self.left_eye_wrinkle.undraw()
        self.left_eye_wrinkle2.undraw()
        self.left_eye_wrinkle3.undraw()
        self.right_eye_wrinkle.undraw()
        self.right_eye_wrinkle2.undraw()
        self.right_eye_wrinkle3.undraw()
    


class dialogue:
    def __init__(self,win):
        self.text_box = Text(Point(170,60), 80)
        self.text_box.setText("hello there! I need your help!"),
        self.text_box2 = Text(Point(180,80), 80)
        self.text_box2.setText("I am an old man and i have lost all my cows.")
        self.text_box3 = Text(Point(180,110), 80) 
        self.text_box3.setText("The coyotes from the forest ate them all :( ")
        self.text_box4 = Text(Point(220,140), 80)
        self.text_box4.setText("i have created a magic spell to bring them back to life!")
        self.text_box5 = Text(Point(180,170), 80)
        self.text_box5.setText("but i need your help to do it ")
        self.text_box6 =Text(Point(180,200), 50)
        self.text_box6.setText("will you help me?")
        self.text_box7 = Text(Point(180,230), 50)
        self.text_box7.setText("press any key to continue")

    def draw(self,win):
        self.text_box.setTextColor("white")
        self.text_box.setSize(18)
        self.text_box.draw(win)
        self.text_box2.setTextColor("white")
        self.text_box2.setSize(18)
        self.text_box2.draw(win)
        self.text_box3.setTextColor("white")
        self.text_box3.setSize(18)
        self.text_box3.draw(win)
        self.text_box4.setTextColor("white")
        self.text_box4.setSize(18)
        self.text_box4.draw(win)
        self.text_box5.setTextColor("white")
        self.text_box5.setSize(18)
        self.text_box5.draw(win)
        self.text_box6.setTextColor("white")
        self.text_box6.setSize(18)
        self.text_box6.draw(win)
        self.text_box7.setTextColor("white")
        self.text_box7.setSize(18)
        self.text_box7.draw(win)

    def undraw(self):
        self.text_box.undraw()
        self.text_box2.undraw()
        self.text_box3.undraw()
        self.text_box4.undraw()
        self.text_box5.undraw()
        self.text_box6.undraw()
        self.text_box7.undraw()

class dialogue2:
    def __init__(self,win):
    
        self.text_box = Text(Point(150,60), 80)
        self.text_box.setText("awesome!"),
        self.text_box2 = Text(Point(150,80), 80)
        self.text_box2.setText("all you need to do is put the")
        self.text_box3 = Text(Point(150,110), 80) 
        self.text_box3.setText("peices of my cow back together ")
        self.text_box4 = Text(Point(150,140), 80)
        self.text_box4.setText("press enter to begin")

    def draw(self,win):
        self.text_box.setTextColor("white")
        self.text_box.setSize(18)
        self.text_box.draw(win)
        self.text_box2.setTextColor("white")
        self.text_box2.setSize(18)
        self.text_box2.draw(win)
        self.text_box3.setTextColor("white")
        self.text_box3.setSize(18)
        self.text_box3.draw(win)
        self.text_box4.setTextColor("white")
        self.text_box4.setSize(18)
        self.text_box4.draw(win)


    def undraw(self):
        self.text_box.undraw()
        self.text_box2.undraw()
        self.text_box3.undraw()
        self.text_box4.undraw()

class winCow:
    def __init__(self,win):
        self.text_box = Text(Point(250,60), 80)
        self.text_box.setText("Congratulations!! You brought my cows back to Life :)")
        self.text_box2 = Text(Point(200,80), 80)
        self.text_box2.setText("As a reward you will receive a peice of a sword!")
    def draw(self,win):
        self.text_box.setTextColor("white")
        self.text_box.setSize(18)
        self.text_box.draw(win)
        self.text_box2.setTextColor("white")
        self.text_box2.setSize(18)
        self.text_box2.draw(win)
        
    
        
        

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
    



    
    
    


