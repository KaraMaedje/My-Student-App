from graphics import*
from button import*
import feedparser


def moreinfo():
    win = GraphWin("More Info", 360, 200)
    win.setCoords(0, 0, 360, 200)
    win.setBackground("MistyRose")

    #Drawing the Labels (More Info)
    #SUBTITLE
    school = Text(Point(90,160), "More Info")
    school.setFace("arial")
    school.setSize(20)
    school.setStyle("bold")
    school.draw(win)

    school= Rectangle(Point(27,150), Point(153,175))
    school.setOutline("black")
    school.draw(win)


    #Making Borders
    box = Rectangle(Point(10,10), Point(350,190))
    box.setOutline("Snow")
    box.draw(win)

    box2 = Rectangle(Point(20,20), Point(340,180))
    box2.setOutline("Snow")
    box2.draw(win)

    #Subject (Title)
    events = Text(Point(165,90), "Social Updates \n View Shell")
    events.setFill("Snow")
    events.setFace("arial")
    events.setSize(20)
    events.setStyle("bold")
    events.draw(win)

    #Getting social feed from yahoo entertainment (from the new class feedparser)
    d = feedparser.parse('http://sg.entertainment.yahoo.com/rss/')
    for post in d.entries:
        y= post.title+ ": " + post.description + "\n"
        print(y)
        #social = Text(Point(75,10), y[0])
        #social.draw(win)



