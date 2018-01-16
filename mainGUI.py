from graphics import *
from button import *
from mydataGUI import *
from myplannerGUI import *
from mycalendarGUI import * 
from mycalculatorGUI import*
from moreinfoGUI import*
from myschoolGUI import*
import time


class MainGUI:
 
    def __init__(self, student):

        self.student = student

        # Create the window 
        self.win = GraphWin("My Account", 360, 360)
        self.win.setCoords(0, 0, 360, 360)
        self.win.setBackground("lightpink")
        
        # Create main buttons
        self.mydataButton = Button(self.win, Point(100,138), 120, 40, "My Data")
        self.mydataButton.rect.setFill("floral white")
        self.mydataButton.activate()
        
        self.mycaluButton = Button(self.win, Point(100,93), 120, 40, "My Calculator")
        self.mycaluButton.rect.setFill("floral white")
        self.mycaluButton.activate()
        
        self.mycaleButton = Button(self.win, Point(100,48), 120, 40, "My Calendar")
        self.mycaleButton.rect.setFill("floral white")
        self.mycaleButton.activate()
        
        self.myplanButton = Button(self.win, Point(260,138), 120, 40, "My Planner")
        self.myplanButton.rect.setFill("floral white")
        self.myplanButton.activate()
        
        self.myschoolButton = Button(self.win, Point(260,93), 120, 40, "My School")
        self.myschoolButton.rect.setFill("floral white")
        self.myschoolButton.activate()
        
        self.myinfoButton = Button(self.win, Point(260,48), 120, 40, "My Info")
        self.myinfoButton.rect.setFill("floral white")
        self.myinfoButton.activate()

        # Create title and border
        myacc = Text(Point(176,318), "My Account")
        myacc.setFace("arial")
        myacc.setSize(16)
        myacc.setStyle("bold")
        myacc.draw(self.win)

        account= Rectangle(Point(111,305), Point(242,331))
        account.setOutline("Misty Rose")
        account.setWidth(1.5)
        account.draw(self.win)

        # Exit button
        self.quitButton = Button(self.win, Point(320,320), 15,18, "X")
        self.quitButton.activate()

        # Implement current date and time
        self.time_title = Text(Point(65, 290), "Time:")
        self.time_title.setStyle("bold")   
        self.time_title.draw(self.win)
        self.time = Text(Point(120, 290), time.strftime("%I:%M:%S"))
        self.time.draw(self.win)

        self.date_title = Text(Point(210, 290), "Date:")
        self.date_title.setStyle("bold")   
        self.date_title.draw(self.win)
        self.date = Text(Point(275, 290), time.strftime("%d/%m/%Y"))
        self.date.draw(self.win)
        
        # Draw window borders 
        box = Rectangle(Point(10,10), Point(350,350))
        box.setOutline("Misty Rose")
        box.setWidth(4)
        box.draw(self.win)

        box2 = Rectangle(Point(20,20), Point(340,340))
        box2.setOutline("Misty Rose")
        box2.setWidth(3)
        box2.draw(self.win)

        # Store images into a list 
        self.images = ["Day_1.png", "Day_2.png"]
        
    
    def run(self):
        
        # Read date to determine whether Day 1 or Day 2 
        date = ""
        text = self.date.getText()
        date = date + text[0] + text[1]
        date = int(date)

        if (date % 2 == 0):
            self.day = Image(Point(176,225), "day_2.png")
            self.day.draw(self.win)

        if (date % 2 != 0):
            self.day = Image(Point(176,225), "Day_1.png")
            self.day.draw(self.win)

        # Run the rest of the program
        pt = self.win.getMouse()
          
        while True:
            if self.mydataButton.clicked(pt):
                mydata = MyDataGUI(self.student)
                #self.mydataButton.deactivate()

            if self.myplanButton.clicked(pt):
                myplanner = MyPlannerGUI()
                myplanner.run()
                #self.myplanButton.deactivate()

            if self.mycaleButton.clicked(pt):
                my_calendar = mycalendar()
                #self.mycaleButton.deactivate()

            if self.mycaluButton.clicked(pt):
                my_calc = Calculator()
                my_calc.run()
                #self.mycaluButton.deactivate()
            
            if self.myinfoButton.clicked(pt):
                myinfo = moreinfo()
                #self.myinfoButton.deactivate()
            
                
            if self.myschoolButton.clicked(pt):
                my_school = myschool()
                #self.myschoolButton.deactivate()

            if self.quitButton.clicked(pt):
                self.win.close()

            pt = self.win.getMouse()
