from graphics import *
WIDTH = 1000
HEIGHT = 500
win = GraphWin( "BackStory", WIDTH, HEIGHT )
def BackGround():
    # draw the background
    back_ground = Image(Point(WIDTH/2, HEIGHT/2), "dungeon.gif")
    back_ground.draw(win)
    
## COPIED FROM INTERNET
 # Load the required library
##mixer.init()
##mixer.music.load('Medeival Music Royalty Free Game Music.mp3')
##mixer.music.play()

##
#### END OF COPIED SECTION


# title
def Title():
    title = Text(Point(500,40),50)
    title.setText("JOURNEY INTO ADVENTURE")
    title.setSize(30)
    title.setTextColor("white")
    title.draw(win)

class Story:
    def __init__(self,win):
        # story
        self.text_box = Text(Point(500,60), 80)
        self.text_box.setText("It’s been seven years since I last saw "),
        self.text_box2 = Text(Point(500,80), 80)
        self.text_box2.setText("her beautiful round face, since I last heard her subtle voice, or since I last felt")
        self.text_box3 = Text(Point(500,110), 80) 
        self.text_box3.setText("her heartbeat against my ear. The last memory I have of her is when she kissed ")
        self.text_box4 = Text(Point(500,140), 80)
        self.text_box4.setText("me goodbye before she left to go into town. The next thing I knew, there were knights ")
        self.text_box5 = Text(Point(500,170), 80)
        self.text_box5.setText(" swarming our humble little house on top of the hill. One of them was shaking me and  ")
        self.text_box6 =Text(Point(500,200), 50)
        self.text_box6.setText("asking me where she was. I was so confused, and I didn’t know what to say so ")
        self.text_box7 = Text(Point(500,230), 50)
        self.text_box7.setText("I ran away as fast as I could through the woods and into the town. It was a Sunday, so ")
        self.text_box8 = Text(Point(500,260), 50)
        self.text_box8.setText("Zenith would stop by the monks who sold their bread on the street. Blacwin, the monk ")
        self.text_box9 = Text(Point(500,280), 50)
        self.text_box9.setText("who was there, said that he hadn’t seen her. I spent the day looking for her, but ")
        self.text_box10 = Text(Point(500,310), 50)
        self.text_box10.setText("I eventually just gave up and waited back at the house. The knights were gone. ")
        self.text_box11 = Text(Point(500,340), 50)
        self.text_box11.setText("who was there, said that he hadn’t seen her. I spent the day looking for her, but ")
        self.text_box12 = Text(Point(500,370), 50)
        self.text_box12.setText("My heart was racing with the different places she could have gone and why the Kings ")
        self.text_box13 = Text(Point(500,400), 50)
        self.text_box13.setText("knights would have showed up looking for her. ")
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
        self.text_box8.setTextColor("white")
        self.text_box8.setSize(18)
        self.text_box8.draw(win)
        self.text_box9.setTextColor("white")
        self.text_box9.setSize(18)
        self.text_box9.draw(win)
        self.text_box10.setTextColor("white")
        self.text_box10.setSize(18)
        self.text_box10.draw(win)
        self.text_box11.setTextColor("white")
        self.text_box11.setSize(18)
        self.text_box11.draw(win)
        self.text_box12.setTextColor("white")
        self.text_box12.setSize(18)
        self.text_box12.draw(win)
        self.text_box13.setTextColor("white")
        self.text_box13.setSize(18)
        self.text_box13.draw(win)

    def undraw(self):
        self.text_box.undraw()
        self.text_box2.undraw()
        self.text_box3.undraw()
        self.text_box4.undraw()
        self.text_box5.undraw()
        self.text_box6.undraw()
        self.text_box7.undraw()
        self.text_box8.undraw()
        self.text_box9.undraw()
        self.text_box10.undraw()
        self.text_box11.undraw()
        self.text_box12.undraw()
        self.text_box13.undraw()
      
        


def Story2():
    text_box = Text(Point(500,60), 80)
    text_box.setText("Clang!! I suddenly heard a loud noise coming from the backside of my house. "),
    text_box2 = Text(Point(500,80), 80)
    text_box2.setText("Clang!! There it was again! I hurried through the kitchen to go outside and see what was happening.")
    text_box3 = Text(Point(500,110), 80) 
    text_box3.setText("A small green creature was hopping around clanging my pots and pans together. ")
    text_box4 = Text(Point(500,140), 80)
    text_box4.setText("I thought it was some sort of rabid animal at first but then it said “What are you looking at ugly”.")
    text_box5 = Text(Point(500,170), 80)
    text_box5.setText(" I was so surprised I almost screamed. “I am NOT ugly” I yelled back. How could such a small and weird call ME ugly.  ")
    text_box6 =Text(Point(500,200), 50)
    text_box6.setText("The creature looked me up and down then rolled its eyes. He was hooping closer to me and then he told me ")
    text_box7 = Text(Point(500,230), 50)
    text_box7.setText("“Look, I don’t care about you. I am just here to deliver a message. ")
    text_box8 = Text(Point(500,260), 50)
    text_box8.setText("Your girlfriend has been a part of a secret society of women who use magic to try and take down the king. ")
    text_box9 = Text(Point(500,280), 50)
    text_box9.setText("She didn’t tell you because she was blood sworn to secrecy. ")
    text_box10 = Text(Point(500,310), 50)
    text_box10.setText("The king has known for several months now that there was a secret society trying to take him down. ")
    text_box11 = Text(Point(500,340), 50)
    text_box11.setText("He just didn’t know who was a part of it. ")
    text_box12 = Text(Point(500,370), 50)
    text_box12.setText("He only found out Zenith was a part of it when a scumy little rat man saw her using magic to heal a hurt dove. ")
    text_box13 = Text(Point(500,400), 50)
    text_box13.setText("He sold her out to the king and now the king has her captured! ")
    text_box14 = Text(Point(500,425), 50)
    text_box14.setText("You must go through the dungeon of the castle to try and rescue her. ")
    text_box15 = Text(Point(500,445), 50)
    text_box15.setText("Time is of the essence because once the king finds out that he cant get any information from her he will kill her or")
    text_box16 = Text(Point(500,465), 50)
    text_box16.setText("keep her for himself. The dungeon will have levels and tricks that you must get through so that you can rescue her” ")
    text_box17 = Text(Point(500,475), 50)
    text_box17.setText("For the past seven years I have been trying to find a secret entrance to the dungeon.")
    text_box18 = Text(Point(500,500),50)
    text_box18.setText("I have finally found that entrance and now I must defeat all the levels to rescue Zenith!!")


    text_box.setTextColor("white")
    text_box.setSize(18)
    text_box.draw(win)
    text_box2.setTextColor("white")
    text_box2.setSize(18)
    text_box2.draw(win)
    text_box3.setTextColor("white")
    text_box3.setSize(18)
    text_box3.draw(win)
    text_box4.setTextColor("white")
    text_box4.setSize(18)
    text_box4.draw(win)
    text_box5.setTextColor("white")
    text_box5.setSize(18)
    text_box5.draw(win)
    text_box6.setTextColor("white")
    text_box6.setSize(18)
    text_box6.draw(win)
    text_box7.setTextColor("white")
    text_box7.setSize(18)
    text_box7.draw(win)
    text_box8.setTextColor("white")
    text_box8.setSize(18)
    text_box8.draw(win)
    text_box9.setTextColor("white")
    text_box9.setSize(18)
    text_box9.draw(win)
    text_box10.setTextColor("white")
    text_box10.setSize(18)
    text_box10.draw(win)
    text_box11.setTextColor("white")
    text_box11.setSize(18)
    text_box11.draw(win)
    text_box12.setTextColor("white")
    text_box12.setSize(18)
    text_box12.draw(win)
    text_box13.setTextColor("white")
    text_box13.setSize(18)
    text_box13.draw(win)
    text_box14.setTextColor("white")
    text_box14.setSize(18)
    text_box14.draw(win)
    text_box15.setTextColor("white")
    text_box15.setSize(18)
    text_box15.draw(win)
    text_box16.setTextColor("white")
    text_box16.setSize(18)
    text_box16.draw(win)
    text_box17.setTextColor("white")
    text_box17.setSize(18)
    text_box17.draw(win)
    text_box18.setTextColor("white")
    text_box18.setSize(18)
    text_box18.draw(win)







def go():
    BackGround()
    Title()
    first_page = Story(win)
    first_page.draw(win)
    win.getKey
    first_page.undraw()
    Story2()
    win.close()
    


