from graphics import *
WIDTH = 1000
HEIGHT = 500
win = GraphWin( "myLevel", WIDTH, HEIGHT )
def BackGround():
    # draw the background
    back_ground = Image(Point(WIDTH/2, HEIGHT/2), "cell.png")
    back_ground.draw(win)


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
        
        





def main():
    BackGround()
    oldman = OldMan("old man",win)
    oldman.draw(win)


main()
