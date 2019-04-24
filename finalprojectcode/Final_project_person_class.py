from graphics import *
class Person:
    def __init__(self, name, position, win):
        self.name = name

        #Head
        p1 = Point(position.getX()+25, position.getY()-70)
        p2 = Point(position.getX()-25, position.getY()-30)
        self.head = Rectangle(p1,p2)
        self.head.setFill("Peru")
        
        #arms
        p1 = Point(position.getX()+50, position.getY()-30)
        p2 = Point(position.getX()-50, position.getY()+30)
        self.arms = Rectangle(p1,p2)
        self.arms.setFill("Red")

        #legs
        p1 = Point(position.getX()+30, position.getY()+30)
        p2 = Point(position.getX()-30, position.getY()+90)
        self.legs = Rectangle(p1,p2)
        self.legs.setFill("Navy")

        #Armpits
        p1 = Point(position.getX()+30, position.getY()-10)
        p2 = Point(position.getX()+30, position.getY()+30)
        p3 = Point(position.getX()-30, position.getY()-10)
        p4 = Point(position.getX()-30, position.getY()+30)
        self.rightPit = Line(p1,p2)
        self.leftPit = Line(p3,p4)

        #crotch
        p1 = Point(position.getX(), position.getY()+50)
        p2 = Point(position.getX(), position.getY()+90)
        self.crotch = Line(p1,p2)

        #face
##        p1 = Point(position.getX()+9, position.getY()-53)
##        p2 = Point(position.getX()-9, position.getY()-53)
##        p3 = Point(position.getX()-7, position.getY()-44)
##        p4 = Point(position.getX()+7,position.getY()-44)
##        self.rightEye = Circle(p1, 3)
##        self.leftEye = Circle(p2,3)
##        self.mouth = Line(p3,p4)
##        self.rpupil = p1
##        self.lpupil = p2
##        self.rightEye.setFill("White")
##        self.leftEye.setFill("White")


    def draw(self, win):
        self.head.draw(win)
        self.arms.draw(win)
        self.legs.draw(win)
        self.rightPit.draw(win)
        self.leftPit.draw(win)
        self.crotch.draw(win)
##        self.rightEye.draw(win)
##        self.leftEye.draw(win)
##        self.rpupil.draw(win)
##        self.lpupil.draw(win)
##        self.mouth.draw(win)

    def undraw(self):
        self.head.undraw()
        self.arms.undraw()
        self.legs.undraw()
        self.rightPit.undraw()
        self.leftPit.undraw()
        self.crotch.undraw()

    def move( self , dx, dy, win):
        key = win.getKey()
        if key == "d":
            self.head.move( dx, 0 )
            self.arms.move( dx, 0 )
            self.legs.move( dx, 0 )
            self.rightPit.move( dx, 0 )
            self.leftPit.move( dx, 0 )
            self.crotch.move( dx, 0 )
            self.rightEye.move( dx, 0 )
            self.leftEye.move( dx, 0 )
            self.rpupil.move(dx, 0)
            self.lpupil.move( dx, 0)
            self.mouth.move( dx, 0 )
        if key == "a":
            self.head.move( -dx, 0 )
            self.arms.move( -dx, 0 )
            self.legs.move( -dx, 0 )
            self.rightPit.move( -dx, 0 )
            self.leftPit.move( -dx, 0 )
            self.crotch.move( -dx, 0 )
            self.rightEye.move( -dx, 0 )
            self.leftEye.move( -dx, 0 )
            self.rpupil.move( -dx, 0)
            self.lpupil.move( -dx, 0)
            self.mouth.move( -dx, 0 )
        if key == "s":
            self.head.move( 0, dy )
            self.arms.move( 0, dy )
            self.legs.move( 0, dy )
            self.rightPit.move( 0, dy )
            self.leftPit.move( 0, dy )
            self.crotch.move( 0, dy )
            self.rightEye.move( 0, dy )
            self.leftEye.move( 0, dy )
            self.rpupil.move( 0, dy )
            self.lpupil.move( 0, dy )
            self.mouth.move( 0, dy )
        if key == "w":
            self.head.move( 0, -dy )
            self.arms.move( 0, -dy )
            self.legs.move( 0, -dy )
            self.rightPit.move( 0, -dy )
            self.leftPit.move( 0, -dy )
            self.crotch.move( 0, -dy )
            self.rightEye.move( 0, -dy )
            self.leftEye.move( 0, -dy )
            self.rpupil.move( 0, -dy )
            self.lpupil.move( 0, -dy )
            self.mouth.move( 0, -dy )

class Player(Person):
    def __init__(self, name, position, win):
        super().__init__(name, position, win)

        #hat
        p1 = Point(position.getX(), position.getY()-70)
        p2 = Point(position.getX()+20, position.getY()-70)
        p3 = Point(position.getX()+40, position.getY()-75)
        self.hat = Circle(p1, 25)
        self.brim = Rectangle(p2,p3)
        self.hat.setFill("Darkorange")
        self.brim.setFill("Darkorange")

        
        #shirt
        p1 = Point(position.getX()+15, position.getY()+30)
        p2 = Point(position.getX()-15, position.getY()-30)
        self.shirt = Rectangle(p1,p2)
        self.shirt.setFill("White")

        #hair
        p1 = Point(position.getX()-25, position.getY()-32)
        p2 = Point(position.getX()-25, position.getY()-70)
        p3 = Point(position.getX()+25, position.getY()-70)
        p4 = Point(position.getX()+25, position.getY()-32)
        p5 = Point(position.getX()+21, position.getY()-32)
        p6 = Point(position.getX()+21, position.getY()-64)
        p7 = Point(position.getX()-21, position.getY()-64)
        p8 = Point(position.getX()-21, position.getY()-32)
        self.hair = Polygon(p1,p2,p3,p4,p5,p6,p7,p8)
        self.hair.setFill("Black")
        
    def draw(self,win):
        self.brim.draw(win)
        self.hat.draw(win)
        self.head.draw(win)
        self.hair.draw(win)
        self.arms.draw(win)
        self.legs.draw(win)
        self.rightPit.draw(win)
        self.leftPit.draw(win)
        self.crotch.draw(win)
        self.shirt.draw(win)
##        self.rightEye.draw(win)
##        self.leftEye.draw(win)
##        self.rpupil.draw(win)
##        self.lpupil.draw(win)
##        self.mouth.draw(win)

    def undraw(self):
        self.brim.undraw()
        self.hat.undraw()
        self.head.undraw()
        self.hair.undraw()
        self.arms.undraw()
        self.legs.undraw()
        self.rightPit.undraw()
        self.leftPit.undraw()
        self.crotch.undraw()
        self.shirt.undraw()
        
    def move( self , dx, dy, win):
        key = win.getKey()
        if key == "d":
            self.hat.move( dx, 0)
            self.brim.move( dx, 0)
            self.head.move( dx, 0 )
            self.arms.move( dx, 0 )
            self.legs.move( dx, 0 )
            self.rightPit.move( dx, 0 )
            self.leftPit.move( dx, 0 )
            self.crotch.move( dx, 0 )
            self.shirt.move( dx, 0 )
            self.hair.move( dx, 0 )
##            self.rightEye.move( dx, 0 )
##            self.leftEye.move( dx, 0 )
##            self.rpupil.move(dx, 0)
##            self.lpupil.move( dx, 0)
##            self.mouth.move( dx, 0 )
        elif key == "a":
            self.hat.move( -dx, 0)
            self.brim.move( -dx, 0)
            self.head.move( -dx, 0 )
            self.arms.move( -dx, 0 )
            self.legs.move( -dx, 0 )
            self.rightPit.move( -dx, 0 )
            self.leftPit.move( -dx, 0 )
            self.crotch.move( -dx, 0 )
            self.shirt.move( -dx, 0 )
            self.hair.move( -dx, 0 )
##            self.rightEye.move( -dx, 0 )
##            self.leftEye.move( -dx, 0 )
##            self.rpupil.move( -dx, 0)
##            self.lpupil.move( -dx, 0)
##            self.mouth.move( -dx, 0 )
        elif key == "s":
            self.hat.move( 0, dy)
            self.brim.move( 0, dy)
            self.head.move( 0, dy )
            self.arms.move( 0, dy )
            self.legs.move( 0, dy )
            self.rightPit.move( 0, dy )
            self.leftPit.move( 0, dy )
            self.crotch.move( 0, dy )
            self.shirt.move( 0, dy )
            self.hair.move( 0, dy )
##            self.rightEye.move( 0, dy )
##            self.leftEye.move( 0, dy )
##            self.rpupil.move( 0, dy )
##            self.lpupil.move( 0, dy )
##            self.mouth.move( 0, dy )
        elif key == "w":
            self.hat.move( 0, -dy)
            self.brim.move( 0, -dy)
            self.head.move( 0, -dy )
            self.arms.move( 0, -dy )
            self.legs.move( 0, -dy )
            self.rightPit.move( 0, -dy )
            self.leftPit.move( 0, -dy )
            self.crotch.move( 0, -dy )
            self.shirt.move( 0, -dy )
            self.hair.move( 0, -dy )
##            self.rightEye.move( 0, -dy )
##            self.leftEye.move( 0, -dy )
##            self.rpupil.move( 0, -dy )
##            self.lpupil.move( 0, -dy )
##            self.mouth.move( 0, -dy )

class King(Person):
    def __init__(self, name, position, win):
        super().__init__(name, position, win)
        #Crown
        p1 = Point(position.getX()-28, position.getY()-70)
        p2 = Point(position.getX()-28, position.getY()-90)
        p3 = Point(position.getX()-21, position.getY()-80)
        p4 = Point(position.getX()-14, position.getY()-90)
        p5 = Point(position.getX()-7, position.getY()-80)
        p6 = Point(position.getX(), position.getY()-90)
        p7 = Point(position.getX()+7, position.getY()-80)
        p8 = Point(position.getX()+14, position.getY()-90)
        p9 = Point(position.getX()+21, position.getY()-80)
        p10 = Point(position.getX()+28, position.getY()-90)
        p11 = Point(position.getX()+28, position.getY()-70)
        self.crown = Polygon(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11)
        self.crown.setFill("Gold")
        gold = color_rgb(235,164,0)
        self.arms.setFill(gold)
        self.legs.setFill("Gray")

        #BEARD
        p1 = Point(position.getX()-5,position.getY()-40)
        p2 = Point(position.getX()+5,position.getY()-40)
        p3 = Point(position.getX(),position.getY()-33)
        self.beard = Polygon(p1,p2,p3)
        self.beard.setFill("Sienna")


    def draw(self, win):
        self.head.draw(win)
        self.arms.draw(win)
        self.legs.draw(win)
        self.rightPit.draw(win)
        self.leftPit.draw(win)
        self.crotch.draw(win)
        self.crown.draw(win)
        self.beard.draw(win)
##        self.rightEye.draw(win)
##        self.leftEye.draw(win)
##        self.rpupil.draw(win)
##        self.lpupil.draw(win)
##        self.mouth.draw(win)

    def undraw(self):
        self.head.undraw()
        self.arms.undraw()
        self.legs.undraw()
        self.rightPit.undraw()
        self.leftPit.undraw()
        self.crotch.undraw()
        self.crown.undraw()
        self.beard.undraw()
        
    def move( self , dx, dy, win):
        self.head.move( dx, dy )
        self.arms.move( dx, dy )
        self.legs.move( dx, dy )
        self.rightPit.move( dx, dy )
        self.leftPit.move( dx, dy )
        self.crotch.move( dx, dy )
        self.crown.move( dx, dy )
        self.beard.move( dx, dy )
##        self.rightEye.move( dx, dy )
##        self.leftEye.move( dx, dy )
##        self.rpupil.move(dx, dy)
##        self.lpupil.move( dx, dy)
##        self.mouth.move( dx, dy )

class Cutie(Person):
    def __init__(self, name, position, win):
        super().__init__(name, position, win)
        #crown
        p1 = Point(position.getX()-10, position.getY()-70)
        p2 = Point(position.getX()-5, position.getY()-85)
        p3 = Point(position.getX(), position.getY()-75)
        p4 = Point(position.getX()+5, position.getY()-85)
        p5 = Point(position.getX()+10, position.getY()-70)
        self.crown = Polygon(p1,p2,p3,p4,p5)
        self.crown.setFill(color_rgb(235,164,0))

        #sweater stripe
        p1 = Point(position.getX()+50,position.getY()+5)
        p2 = Point(position.getX()-50,position.getY()-5)
        self.stripe = Rectangle(p1,p2)

        self.arms.setFill(color_rgb(134,166,255))
        self.stripe.setFill("Red")
        self.legs.setFill(color_rgb(40,40,40))

        #hair
        p1 = Point(position.getX()-25, position.getY()-37)
        p2 = Point(position.getX()-25, position.getY()-70)
        p3 = Point(position.getX()+25, position.getY()-70)
        p4 = Point(position.getX()+25, position.getY()-37)
        p5 = Point(position.getX()+21, position.getY()-37)
        p6 = Point(position.getX()+21, position.getY()-62)
        p7 = Point(position.getX()-21, position.getY()-62)
        p8 = Point(position.getX()-21, position.getY()-37)
        self.hair = Polygon(p1,p2,p3,p4,p5,p6,p7,p8)
        self.hair.setFill("Black")
        
    def draw(self, win):
        self.head.draw(win)
        self.arms.draw(win)
        self.legs.draw(win)
        self.stripe.draw(win)
        self.rightPit.draw(win)
        self.leftPit.draw(win)
        self.crotch.draw(win)
        self.crown.draw(win)
        self.hair.draw(win)
##        self.rightEye.draw(win)
##        self.leftEye.draw(win)
##        self.rpupil.draw(win)
##        self.lpupil.draw(win)
##        self.mouth.draw(win)
    def undraw(self):
        self.head.undraw()
        self.arms.undraw()
        self.legs.undraw()
        self.rightPit.undraw()
        self.leftPit.undraw()
        self.crotch.undraw()
        self.crown.undraw()
        self.stripe.undraw()
        self.hair.undraw()

    def move( self , dx, dy, win):
        self.head.move( dx, dy )
        self.arms.move( dx, dy )
        self.legs.move( dx, dy )
        self.rightPit.move( dx, dy )
        self.leftPit.move( dx, dy )
        self.crotch.move( dx, dy )
        self.crown.move( dx, dy )
        self.hair.move( dx, dy )
        self.stripe.move( dx, dy )
##        self.rightEye.move( dx, dy )
##        self.leftEye.move( dx, dy )
##        self.rpupil.move(dx, dy)
##        self.lpupil.move( dx, dy)
##        self.mouth.move( dx, dy )

class Mini(Person):
    def __init__():
        super().__init__()
        

def main():
    bose = True
    win = GraphWin("WALL",600,400)
    thisguy = Player("Tony", Point(400,200),win)
    dood = Person("Bro",Point(100,100), win)
    oops = King("King Shirtbain",Point(200,300),win)
    #who = NPC("Um",Point(200,300),win)
    wow = Cutie("Janis",Point(250,100),win)
    wow.draw(win)
    oops.draw(win)
    dood.draw(win)
    thisguy.draw(win)
    while bose == True:
        dood.move(10,10,win)
        thisguy.move(6,6,win)
        wow.move(7,7,win)
        oops.move(5,5,win)

#main()
