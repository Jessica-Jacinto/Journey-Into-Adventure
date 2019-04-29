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
        
        self.inventory = []

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
            update(30)
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
            update(30)
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
            update(30)
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
            update(30)

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
        #moving the whole person by +/- dy or dx when the right key is pressed
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
            update(30)
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
            update(30)
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
            update(30)
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
            update(30)

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
    def __init__(self, name, position, win):
        #super().__init__(name, position, win)
        
        self.inventory = []
        
        #head
        p1 = Point(position.getX()+12, position.getY()-25)
        p2 = Point(position.getX()-12, position.getY()-5)
        self.head = Rectangle(p1,p2)
        self.head.setFill("Peru")

        #arms
        p1 = Point(position.getX()+25, position.getY()-5)
        p2 = Point(position.getX()-25, position.getY()+25)
        self.arms = Rectangle(p1,p2)
        self.arms.setFill("Red")

        #legs
        p1 = Point(position.getX()+15, position.getY()+25)
        p2 = Point(position.getX()-15, position.getY()+55)
        self.legs = Rectangle(p1,p2)
        self.legs.setFill("Navy")
        
        #pits
        p1 = Point(position.getX()+15, position.getY()+25)
        p2 = Point(position.getX()+15, position.getY()+5)
        p3 = Point(position.getX()-15, position.getY()+25)
        p4 = Point(position.getX()-15, position.getY()+5)
        self.rightPit = Line(p1,p2)
        self.leftPit = Line(p3,p4)


        #crotch
        p1 = Point(position.getX(), position.getY()+35)
        p2 = Point(position.getX(), position.getY()+55)
        self.crotch = Line(p1,p2)

        #shirt
        p1 = Point(position.getX()-8, position.getY()-5)
        p2 = Point(position.getX()+8, position.getY()+25)
        self.shirt = Rectangle(p1,p2)
        self.shirt.setFill("White")
        
    def draw(self, win):
        self.head.draw(win)
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
    def move( self , dx, dy, win):
        #moving the whole person by +/- dy or dx when the right key is pressed
        key = win.getKey()
        if key == "d":
            self.head.move( dx, 0 )
            self.arms.move( dx, 0 )
            self.legs.move( dx, 0 )
            self.rightPit.move( dx, 0 )
            self.leftPit.move( dx, 0 )
            self.crotch.move( dx, 0 )
            self.shirt.move( dx, 0 )
            update(30)

        if key == "a":
            self.head.move( -dx, 0 )
            self.arms.move( -dx, 0 )
            self.legs.move( -dx, 0 )
            self.rightPit.move( -dx, 0 )
            self.leftPit.move( -dx, 0 )
            self.crotch.move( -dx, 0 )
            self.shirt.move( -dx, 0 )
            update(30)

        if key == "s":
            self.head.move( 0, dy )
            self.arms.move( 0, dy )
            self.legs.move( 0, dy )
            self.rightPit.move( 0, dy )
            self.leftPit.move( 0, dy )
            self.crotch.move( 0, dy )
            self.shirt.move( 0, dy )
            update(30)

        if key == "w":
            self.head.move( 0, -dy )
            self.arms.move( 0, -dy )
            self.legs.move( 0, -dy )
            self.rightPit.move( 0, -dy )
            self.leftPit.move( 0, -dy )
            self.crotch.move( 0, -dy )
            self.shirt.move( 0, -dy )
            update(30)
        
class bittyBro(Person):
    def __init__(self, name, position, win):
        self.position = position
        
        #head
        p1 = Point(position.getX()-5, position.getY()-7)
        p2 = Point(position.getX()+5, position.getY()-15)
        self.head = Rectangle(p1,p2)
        self.head.setFill("Peru")

        #arms
        p1 = Point(position.getX()-10, position.getY()-7)
        p2 = Point(position.getX()+10, position.getY()+4)
        self.arms = Rectangle(p1,p2)
        self.arms.setFill("Red")

        #legs
        p1 = Point(position.getX()-6, position.getY()+4)
        p2 = Point(position.getX()+6, position.getY()+15)
        self.legs = Rectangle(p1,p2)
        self.legs.setFill("Navy")

        #crotch
        p1 = Point(position.getX(), position.getY()+15)
        p2 = Point(position.getX(), position.getY()+8)
        self.crotch = Line(p1,p2)

        #pits
        p1 = Point(position.getX()-6, position.getY()+4)
        p2 = Point(position.getX()-6, position.getY()-3)
        p3 = Point(position.getX()+6, position.getY()-3)
        p4 = Point(position.getX()+6, position.getY()+4)
        self.rightPit = Line(p1,p2)
        self.leftPit = Line(p3,p4)

        #shirt
        p1 = Point(position.getX()+3, position.getY()-7)
        p2 = Point(position.getX()-3, position.getY()+4)
        self.shirt = Rectangle(p1,p2)
        self.shirt.setFill("White")

    def draw(self, win):
        self.head.draw(win)
        self.arms.draw(win)
        self.legs.draw(win)
        self.rightPit.draw(win)
        self.leftPit.draw(win)
        self.crotch.draw(win)
        self.shirt.draw(win)

    def move( self , dx, dy, win ):
        key = win.getKey()
        #moving the whole person by +/- dy or dx when the right key is pressed
        if key == "d":
            self.head.move( dx, 0 )
            self.arms.move( dx, 0 )
            self.legs.move( dx, 0 )
            self.rightPit.move( dx, 0 )
            self.leftPit.move( dx, 0 )
            self.crotch.move( dx, 0 )
            self.shirt.move( dx, 0 )
            update(30)
        if key == "a":
            self.head.move( -dx, 0 )
            self.arms.move( -dx, 0 )
            self.legs.move( -dx, 0 )
            self.rightPit.move( -dx, 0 )
            self.leftPit.move( -dx, 0 )
            self.crotch.move( -dx, 0 )
            self.shirt.move( -dx, 0 )
            update(30)
        if key == "s":
            self.head.move( 0, dy )
            self.arms.move( 0, dy )
            self.legs.move( 0, dy )
            self.rightPit.move( 0, dy )
            self.leftPit.move( 0, dy )
            self.crotch.move( 0, dy )
            self.shirt.move( 0, dy )
            update(30)
        if key == "w":
            self.head.move( 0, -dy )
            self.arms.move( 0, -dy )
            self.legs.move( 0, -dy )
            self.rightPit.move( 0, -dy )
            self.leftPit.move( 0, -dy )
            self.crotch.move( 0, -dy )
            self.shirt.move( 0, -dy )
            update(30)
    
    def moveKarisLevel( self , dx, dy, win ):
        key = win.getKey()
        #Kari's level has a lot of interactions so it requires a special move function to account for all the objects
        #If the player tries to go through an obstacle or wall it stops them by returning none instead of moving the character
        if key == "d":
            if 25 < self.arms.getCenter().getX() < 31 and ( 36 < self.arms.getCenter().getY()+1.5 < 145 ):
                if 25 < self.arms.getCenter().getX() < 31 and ( 72 < self.arms.getCenter().getY()+1.5 < 109 ):
                    msg = Text(Point(300,350), "There's a strange humming coming from this area and \nlots of little objects stuck to the ceiling.\nYou'd have to be thick to miss this gravity trap.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 137 < self.arms.getCenter().getX() < 143 and ( 145 < self.arms.getCenter().getY()+1.5 < 291 ):
                if 137 < self.arms.getCenter().getX() < 143 and ( 145 < self.arms.getCenter().getY()+1.5 < 182 ):
                    msg = Text(Point(300,350), "It's a crate filled with bee sting ointment.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                elif 137 < self.arms.getCenter().getX() < 143 and ( 218 < self.arms.getCenter().getY()+1.5 < 255 ):
                    msg = Text(Point(300,350), "A legless, armless knight challenges you to a fight. \nYou back away, not knowing exactly how that would work.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 250 <= self.arms.getCenter().getX() <= 256 and ( self.arms.getCenter().getY()+1.5 < 218 ):
                if 250 <= self.arms.getCenter().getX() <= 256 and ( self.arms.getCenter().getY()+1.5 < 36 ):
                    msg = Text(Point(300,350), "There's a huge hole heaten in the floor here. \nFrom the looks of that metal base over there I'd wager someone broke their lava lamp.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                elif 250 <= self.arms.getCenter().getX() <= 256 and ( 72 < self.arms.getCenter().getY()+1.5 < 109 ):
                    msg = Text(Point(300,350), "There's a woman shaped cactus over there. Her arms seem outstretched for a hug.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                elif 250 <= self.arms.getCenter().getX() <= 256 and ( 145 < self.arms.getCenter().getY()+1.5 < 182 ):
                    msg = Text(Point(300,350), "This rock looks like the village strongman Dwayne, son of John.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                    return None
            elif 250 <= self.arms.getCenter().getX() <= 256 and ( 291 < self.arms.getCenter().getY()+1.5 ):
                if 250 <= self.arms.getCenter().getX() <= 256 and ( 291 < self.arms.getCenter().getY()+1.5 < 327 ):
                    msg = Text(Point(300,350), "It's a huge bush with sweet-smelling flowers.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                elif 250 <= self.arms.getCenter().getX() <= 256 and ( 363 < self.arms.getCenter().getY()+1.5 ):
                    msg = Text(Point(300,350), "It's a huge raging fire!!!")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 362 < self.arms.getCenter().getX() < 368 and ( 109 < self.arms.getCenter().getY()+1.5 < 145 ):
                return None
            elif 362 < self.arms.getCenter().getX() < 368 and ( 218 < self.arms.getCenter().getY()+1.5 < 291 ):
                if 362 < self.arms.getCenter().getX() < 368 and ( 218 < self.arms.getCenter().getY()+1.5 < 255 ):
                    msg = Text(Point(300,350), "This mime is stuck in a real box.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 475 < self.arms.getCenter().getX() < 481 and ( 145 < self.arms.getCenter().getY()+1.5 < 327 ):
                if 475 < self.arms.getCenter().getX() < 481 and ( 145 < self.arms.getCenter().getY()+1.5 < 182 ):
                    msg = Text(Point(300,350), "It's a huge raging fire!!!")
                    msg.setFill("White")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                elif 475 < self.arms.getCenter().getX() < 481 and ( 218 < self.arms.getCenter().getY()+1.5 < 255 ):
                    msg = Text(Point(300,350), "It's a huge raging fire!!!")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                elif 475 < self.arms.getCenter().getX() < 481 and ( 291 < self.arms.getCenter().getY()+1.5 < 327 ):
                    msg = Text(Point(300,350), "It's a huge raging fire!!!")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 587 < self.arms.getCenter().getX() < 593 and ( self.arms.getCenter().getY()+1.5 < 145 ):
                return None
            else:
                self.head.move( dx, 0 )
                self.arms.move( dx, 0 )
                self.legs.move( dx, 0 )
                self.rightPit.move( dx, 0 )
                self.leftPit.move( dx, 0 )
                self.crotch.move( dx, 0 )
                self.shirt.move( dx, 0 )
                update(30)
        if key == "a":
            if 7 < self.arms.getCenter().getX() < 13 and ( 15 < self.arms.getCenter().getY()+1.5 < 182 ):
                return None
            elif 7 < self.arms.getCenter().getX() < 13 and ( 363 < self.arms.getCenter().getY()+1.5 < 400 ):
                return None
            elif 120 < self.arms.getCenter().getX() < 126 and ( 182 < self.arms.getCenter().getY()+1.5 < 327 ):
                if 120 < self.arms.getCenter().getX() < 126 and ( 218 < self.arms.getCenter().getY()+1.5 < 225 ):
                    msg = Text(Point(300,350), "Looks like there's more piranha than pond here.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                elif 120 < self.arms.getCenter().getX() < 126 and ( 291 < self.arms.getCenter().getY()+1.5 < 327 ):
                    msg = Text(Point(300,350), "Looks like there's more piranha than pond here.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 232 <= self.arms.getCenter().getX() <= 2338 and ( 36 < self.arms.getCenter().getY()+1.5 < 255 ):
                if 232 <= self.arms.getCenter().getX() <= 338 and ( 145 < self.arms.getCenter().getY()+1.5 < 182 ):
                    msg = Text(Point(300,350), "It's a crate filled with bee sting ointment.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                elif 232 <= self.arms.getCenter().getX() <= 338 and ( 72 < self.arms.getCenter().getY()+1.5 < 109 ):
                    msg = Text(Point(300,350), "There's a strange humming coming from this area and \nlots of little objects stuck to the ceiling.\nYou'd have to be thick to miss this gravity trap.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 345 < self.arms.getCenter().getX() < 351 and ( 72 < self.arms.getCenter().getY()+1.5 < 182 ):
                if 345 < self.arms.getCenter().getX() < 351 and ( 72 < self.arms.getCenter().getY()+1.5 < 109 ):
                    msg = Text(Point(300,350), "There's a woman shaped cactus over there. Her arms seem outstretched for a hug.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                elif 345 < self.arms.getCenter().getX() < 351 and ( 145 < self.arms.getCenter().getY()+1.5 < 182 ):
                    msg = Text(Point(300,350), "This rock looks like the village strongman Dwayne, son of John.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                elif 345 < self.arms.getCenter().getX() < 351 and ( 145 < self.arms.getCenter().getY()+1.5 < 182 ):
                    msg = Text(Point(300,350), "A legless, armless knight challenges you to a fight. \nYou back away, not knowing exactly how that would work.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 345 < self.arms.getCenter().getX() < 351 and ( 255 < self.arms.getCenter().getY()+1.5 < 327 ):
                if 345 < self.arms.getCenter().getX() < 351 and ( 291 < self.arms.getCenter().getY()+1.5 < 327 ):
                    msg = Text(Point(300,350), "It's a huge bush with sweet-smelling flowers.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 457 < self.arms.getCenter().getX() < 463 and ( 182 < self.arms.getCenter().getY()+1.5 < 291 ):
                if 457 < self.arms.getCenter().getX() < 463 and ( 218 < self.arms.getCenter().getY()+1.5 < 255 ):
                    msg = Text(Point(300,350), "This mime is stuck in a real box.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 570 < self.arms.getCenter().getX() < 576 and (  self.arms.getCenter().getY()+1.5 < 72 ):
                if 570 < self.arms.getCenter().getX() < 576 and ( self.arms.getCenter().getY()+1.5 < 36 ):
                    msg = Text(Point(300,350), "There's a huge hole heaten in the floor here. \nFrom the looks of that metal base over there I'd wager someone broke their lava lamp.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None

            else:
                self.head.move( -dx, 0 )
                self.arms.move( -dx, 0 )
                self.legs.move( -dx, 0 )
                self.rightPit.move( -dx, 0 )
                self.leftPit.move( -dx, 0 )
                self.crotch.move( -dx, 0 )
                self.shirt.move( -dx, 0 )
                update(30)
        if key == "s":
            if 18 < self.arms.getCenter().getY()+1.5 < 24 and ( 38 < self.arms.getCenter().getX() < 225 ):
                if 18 < self.arms.getCenter().getY()+1.5 < 24 and ( 113 < self.arms.getCenter().getX() < 150 ):
                    msg = Text(Point(300,350), "There's a strange humming coming from this area and \nlots of little objects stuck to the ceiling.\nYou'd have to be thick to miss this gravity trap.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 91 < self.arms.getCenter().getY()+1.5 < 97 and ( self.arms.getCenter().getX() > 375 ):
                if 91 < self.arms.getCenter().getY()+1.5 < 97 and ( 563 < self.arms.getCenter().getX() ):
                    msg = Text(Point(300,350), "It's a huge raging fire!!!")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                elif 91 < self.arms.getCenter().getY()+1.5 < 97 and ( 450 < self.arms.getCenter().getX() < 488 ):
                    msg = Text(Point(300,350), "It's a huge pile of nothing but right shoes.\nIt may be wrong but it feels so right.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 164 < self.arms.getCenter().getY()+1.5 <= 170 and ( self.arms.getCenter().getX() < 113 ):
                if 164 < self.arms.getCenter().getY()+1.5 <= 170 and ( self.arms.getCenter().getX() < 38 ):
                    msg = Text(Point(300,350), "Looks like there's more piranha than pond here.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 164 < self.arms.getCenter().getY()+1.5 <= 170 and ( 338 < self.arms.getCenter().getX() < 450 ):
                if 164 < self.arms.getCenter().getY()+1.5 <= 170 and ( 338 < self.arms.getCenter().getX() < 375 ):
                    msg = Text(Point(300,350), "That's one rowdy mosh pit!")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 237 < self.arms.getCenter().getY()+1.5 < 243 and ( 225 < self.arms.getCenter().getX() < 338 ):
                if 237 < self.arms.getCenter().getY()+1.5 < 243 and ( 225 < self.arms.getCenter().getX() < 263 ):
                    msg = Text(Point(300,350), "This hole isn't very wide but you can't see the bottom.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 310 < self.arms.getCenter().getY()+1.5 < 316 and ( 113 < self.arms.getCenter().getX() < 225 ):
                if 310 < self.arms.getCenter().getY()+1.5 < 316 and ( 113 < self.arms.getCenter().getX() < 150 ):
                    msg = Text(Point(300,350), "A group of whippersnappers! \nYou yell at them for loitering but they just laugh in your face. Ouch.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 310 < self.arms.getCenter().getY()+1.5 < 316 and ( 338 < self.arms.getCenter().getX() < 488 ):
                if 310 < self.arms.getCenter().getY()+1.5 < 316 and ( 450 < self.arms.getCenter().getX() < 488 ):
                    msg = Text(Point(300,350), "It's a huge raging fire!!!")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                elif 310 < self.arms.getCenter().getY()+1.5 < 316 and ( 338 < self.arms.getCenter().getX() < 375 ):
                    msg = Text(Point(300,350), "It's a huge raging fire!!!")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 382 < self.arms.getCenter().getY()+1.5 < 388 and ( self.arms.getCenter().getX() < 263 ):
                return None
            
            else:
                self.head.move( 0, dy )
                self.arms.move( 0, dy )
                self.legs.move( 0, dy )
                self.rightPit.move( 0, dy )
                self.leftPit.move( 0, dy )
                self.crotch.move( 0, dy )
                self.shirt.move( 0, dy )
                update(30)
        if key == "w":
            if 69 < self.arms.getCenter().getY()+1.5 < 75 and ( 338 < self.arms.getCenter().getX() < 563 ):
                if 69 < self.arms.getCenter().getY()+1.5 < 75 and ( 338 < self.arms.getCenter().getX() < 375 ):
                    msg = Text(Point(300,350), "There's a huge hole heaten in the floor here. \nFrom the looks of that metal base over there I'd wager someone broke their lava lamp.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                elif 69 < self.arms.getCenter().getY()+1.5 < 75 and ( 450 < self.arms.getCenter().getX() < 488 ):
                    msg = Text(Point(300,350), "There's a huge hole heaten in the floor here. \nFrom the looks of that metal base over there I'd wager someone broke their lava lamp.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 12 < self.arms.getCenter().getY()+1.5 < 18 and ( self.arms.getCenter().getX() < 263 ):
                return None
            elif 12 < self.arms.getCenter().getY()+1.5 < 18 and ( self.arms.getCenter().getX() > 563 ):
                return None
            elif 142 < self.arms.getCenter().getY()+1.5 < 148 and ( self.arms.getCenter().getX() > 375 ):
                if 142 < self.arms.getCenter().getY()+1.5 < 148 and ( 450 < self.arms.getCenter().getX() < 488 ):
                    msg = Text(Point(300,350), "It's a huge pile of nothing but right shoes.\nIt may be wrong but it feels so right.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 142 < self.arms.getCenter().getY()+1.5 < 148 and ( 38 < self.arms.getCenter().getX() < 150 ):
                if 142 < self.arms.getCenter().getY()+1.5 < 148 and ( 113 < self.arms.getCenter().getX() < 150 ):
                    msg = Text(Point(300,350), "There's a strange humming coming from this area and \nlots of little objects stuck to the ceiling.\nYou'd have to be thick to miss this gravity trap.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 215 < self.arms.getCenter().getY()+1.5 < 221 and ( 263 < self.arms.getCenter().getX() < 375 ):
                if 215 < self.arms.getCenter().getY()+1.5 < 221 and ( 338 < self.arms.getCenter().getX() < 375 ):
                    msg = Text(Point(300,350), "That's one rowdy mosh pit!")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 288 < self.arms.getCenter().getY()+1.5 < 294 and ( 150 < self.arms.getCenter().getX() < 263 ):
                if 288 < self.arms.getCenter().getY()+1.5 < 294 and ( 225 < self.arms.getCenter().getX() < 263 ):
                    msg = Text(Point(300,350), "This hole isn't very wide but you can't see the bottom.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            elif 288 < self.arms.getCenter().getY()+1.5 < 294 and ( 375 < self.arms.getCenter().getX() < 450 ):
                return None
            elif 360 < self.arms.getCenter().getY()+1.5 < 365 and (  self.arms.getCenter().getX() < 255 ):
                if 360 < self.arms.getCenter().getY()+1.5 < 366 and ( self.arms.getCenter().getX() < 38 ):
                    msg = Text(Point(300,350), "Looks like there's more piranha than pond here.")
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                if 360 < self.arms.getCenter().getY()+1.5 < 366 and ( 113 < self.arms.getCenter().getX() < 150 ):
                    msg = Text(Point(300,350), "A group of whippersnappers! \nYou yell at them for loitering but they just laugh in your face. Ouch.")
                    
                    msg.draw(win)
                    win.getMouse()
                    msg.undraw()
                return None
            else:
                self.head.move( 0, -dy )
                self.arms.move( 0, -dy )
                self.legs.move( 0, -dy )
                self.rightPit.move( 0, -dy )
                self.leftPit.move( 0, -dy )
                self.crotch.move( 0, -dy )
                self.shirt.move( 0, -dy )
                update(30)
                
        if key == "b" :
            if 345 < self.arms.getCenter().getX() < 351 and ( 291 < self.arms.getCenter().getY()+1.5 < 327 ):
                msg = Text(Point(300,350), "Yes there sure is a bee there! Would you like to pet it? (y/n)")
                msg.draw(win)
                if key == "y":
                    message = Text(Point(300,350),"You corner the bee inside to bush and give it a nice little pat, but suddenly you see something shiny behind it. \n It's a can of shaving cream! You pick it up and the bee stings you. \nOuch!")
                    message.draw(win)
                    self.inventory.append("Shaving Cream")
                    win.getMouse()
                    message.undraw()
                msg.undraw()
    def getX(self):
        return self.arms.getCenter().getX()
    def getY(self):
        return self.arms.getCenter().getY()

class miniMime(bittyBro):
    #class for an obstacle in Kari's level
    def __init__(self, name, position, win):
        super().__init__(name,position,win)
        self.arms.setFill("DarkSlateGray")
        self.legs.setFill("Black")
    def draw(self,win):
        super().draw(win)
        self.shirt.undraw()

class theRock(bittyBro):
    #class for an obstacle in Kari's level
    def __init__(self, name, position, win):
        super().__init__(name,position,win)
        self.arms.setFill("Gray")
        self.legs.setFill("Gray")
        self.head.setFill("Gray")
    def draw(self,win):
        super().draw(win)
        self.shirt.undraw()
