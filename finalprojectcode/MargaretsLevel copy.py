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
        

        # eyes
        self.left_eye= Oval(Point(400,260),Point(450,290))
        self.left_eye.setFill("white")
        self.left_pupil= Oval(Point
        
            
        
    
    def draw(self,win):
        self.head.draw(win)
        self.left_ear.draw(win)
        self.right_ear.draw(win)
        self.left_eye.draw(win)





def main():
    BackGround()
    oldman = OldMan("old man",win)
    oldman.draw(win)


main()
