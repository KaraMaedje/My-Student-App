#MY SCHOOL
from graphics import*
from button import*


def myschool():
    win = GraphWin("My School", 500, 500)
    win.setCoords(0, 0, 500, 500)
    win.setBackground("MistyRose")

    #Drawing the Labels
    #SUBTITLE
    school = Text(Point(85,460), "My School")
    school.setFace("arial")
    school.setSize(16)
    school.setStyle("bold")
    school.draw(win)

    school= Rectangle(Point(30,448), Point(140,472))
    school.setOutline("black")
    school.draw(win)


    #Making Borders
    box = Rectangle(Point(10,10), Point(490,490))
    box.setOutline("Snow")
    box.draw(win)

    box2 = Rectangle(Point(20,20), Point(480,480))
    box2.setOutline("Snow")
    box2.draw(win)

    #Late Title
    lates = Text(Point(385,380), "Late Start:")
    lates.setSize(13)
    lates.setStyle("bold")
    lates.draw(win)
    #Late Body Text
    late = Text(Point(385,300.5), "Period 1 \n 10:30 - 11:20 \n Period 2 \n 11:25 - 12:10 \n Lunch \n Period 3 \n 1:00  -  1:50 \n Period 4 \n 1:55  -  2:45")
    late.setFace("arial")
    late.setSize(10)
    late.draw(win)
    #Late Box
    late = Rectangle(Point(310, 210), Point(460,390))
    late.draw(win)

    #Lata Start Days
    lates_dates = Text(Point(250, 320), "Late Start Dates: \n2015/16 \n Oct 22, 2015 \n Nov 18, 2015 \n Feb 10, 2016 \n Apr 13, 2016")
    lates_dates.setStyle("bold")
    lates_dates.setFace("arial")
    lates_dates.setSize(10)
    lates_dates.draw(win)

    #Events Coming up
    events = Text(Point(235,130), "JAN 27- 29 : EXAMS \n FEB 1-2 : EXAMS \n FEB 1 : School Council Meeting \n FEB 3 : Turnaround Day \n FEB 4 : Semester 2 Begins")
    events.setFace("arial")
    events.setSize(12)
    events.setStyle("bold")
    events.draw(win)

    #Image
    
    '''s = Image(Point(170,225), "Schools.png")
    s.draw(win)'''


    #Charcater Counts Title
    char = Text(Point(115,380), "Character Counts:")
    char.setSize(12)
    char.setStyle("bold")
    char.draw(win)
    #Character Counts Body Text
    charcounts = Text(Point(120,295), "Period 1 \n 8:30 - 10:25 \n Period 2 \n 10:10 - 11:20 \n LUNCH \n 11:20 - 12:20 \n Period 3 \n 12:20 - 1:30 \n Period 4 \n 1:35 - 2:45")
    charcounts.setFace("arial")
    charcounts.setSize(10)
    charcounts.draw(win)
    #Character Counts Box
    charcounts = Rectangle(Point(40,210), Point(190,390))
    charcounts.draw(win)





