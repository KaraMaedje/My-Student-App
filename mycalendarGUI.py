from graphics import*
from button import*
import calendar


def mycalendar():
    win = GraphWin("My Calendar", 360, 360)
    win.setCoords(0, 0, 360, 360)
    win.setBackground("MistyRose")

    # Title and Border
    school = Text(Point(176, 302), "My Calendar")
    school.setFace("arial")
    school.setSize(18)
    school.setStyle("bold")
    school.draw(win)

    school= Rectangle(Point(93,285), Point(258,318))
    school.setOutline("Snow")
    school.setWidth(2)
    school.draw(win)

    # Window Borders
    box = Rectangle(Point(20,20), Point(340,340))
    box.setOutline("Snow")
    box.setWidth(4)
    box.draw(win)

    box2 = Rectangle(Point(10,10), Point(350,350))
    box2.setOutline("Snow")
    box2.setWidth(5)
    box2.draw(win)

    # Importing and drawing the calendar 
    cal = calendar.month(2016,1)
    #print(cal)
    cale = Text(Point(175,155), cal)
    cale.setFace("arial")
    cale.setSize(18)
    cale.setStyle("bold")
    cale.draw(win)

