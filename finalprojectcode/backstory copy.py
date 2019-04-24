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
mixer.init()
mixer.music.load('Medeival Music Royalty Free Game Music.mp3')
mixer.music.play()

##
#### END OF COPIED SECTION

def text():
    # draw box with words in it
    text_box = Entry(Point(500,50), 80)
    text_box.setText("It’s been seven years since I last saw ")
    text_box2 = Entry(Point(500,80), 80)
    text_box2.setText("her beautiful round face, since I last heard her subtle voice, or since I last felt")
    text_box3 = Entry(Point(500,110), 80)
    text_box3.setText("her heartbeat against my ear. The last memory I have of her is when she kissed ")
    text_box4 = Entry(Point(500,140), 80)
    text_box4.setText("me goodbye before she left to go into town. The next thing I knew, there were knights ")
    text_box5 = Entry(Point(500,170), 80)
    text_box5.setText(" swarming our humble little house on top of the hill. One of them was shaking me and  ")
##    text_box = Entry(Point(250,250), 50)
##    text_box.setText("It’s been seven years since I last saw ")
##    text_box = Entry(Point(250,250), 50)
##    text_box.setText("It’s been seven years since I last saw ")
##    text_box = Entry(Point(250,250), 50)
##    text_box.setText("It’s been seven years since I last saw ")
##    text_box = Entry(Point(250,250), 50)
##    text_box.setText("It’s been seven years since I last saw ")
##    
##                      
##                      
##                      
##                     
##                      asking me where she was. I was so confused, and I didn’t know what to say so
##                      I ran away as fast as I could through the woods and into the town. It was a Sunday, so
##                      Zenith would stop by the monks who sold their bread on the street. Blacwin, the monk
##                      who was there, said that he hadn’t seen her. I spent the day looking for her, but
##                      I eventually just gave up and waited back at the house. The knights were gone.
##                      My heart was racing with the different places she could have gone and why the Kings
##                      knights would have showed up looking for her. As I paced around my room, I
##                      remembered how I first met Zenith.
    text_box.setTextColor("white")
    text_box.draw(win)
    text_box2.setTextColor("white")
    text_box2.draw(win)
    text_box3.setTextColor("white")
    text_box3.draw(win)
    text_box4.setTextColor("white")
    text_box4.draw(win)
    text_box5.setTextColor("white")
    text_box5.draw(win)



def main():
    BackGround()
    text()

main()
