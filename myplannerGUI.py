from graphics import *
from button import *
import os

class MyPlannerGUI:

    def __init__(self):
    
        # Create graphic window
        self.win = GraphWin("My Planner", 360, 200)
        self.win.setCoords(0, 0, 360, 200)
        self.win.setBackground("MistyRose")

        # Create title and subtitle
        label = Text(Point(85, 170), "My Planner")
        label.setFace("arial")
        label.setSize(18)
        label.setStyle("bold")
        label.draw(self.win)

        label = Text(Point(110, 148), "Keep notes and stay organized!")
        label.setFace("arial")
        label.setSize(9)
        label.setStyle("bold")
        label.draw(self.win)

        # Create entry box label
        label = Text(Point(180, 57), "Enter notes here:")
        label.setFace("arial")
        label.setSize(11)
        label.draw(self.win)

        # Create entry box 
        self.textBox = Entry(Point(180, 35), 30)
        self.textBox.setText("")
        self.textBox.setFill("Snow")
        self.textBox.draw(self.win)

        # Making border
        self.outputBox = Rectangle(Point(10, 10), Point(350, 190))
        self.outputBox.setOutline("lightpink")
        self.outputBox.setWidth(5)
        self.outputBox.draw(self.win)

        # Creating buttons
        self.viewButton = Button(self.win, Point(100, 90), 50, 30, "View")
        self.viewButton.rect.setFill("floral white")
        self.viewButton.activate()

        self.saveButton = Button(self.win, Point(175, 90), 50, 30, "Save")
        self.saveButton.rect.setFill("floral white")
        self.saveButton.activate()

        self.closeButton = Button(self.win, Point(250, 90), 50, 30, "Close")
        self.closeButton.rect.setFill("floral white")
        self.closeButton.activate()

    def close(self):
        self.win.close()

#------------------------------------------   
    def run(self):

        pt = self.win.getMouse()

        # Event loop
        while not self.closeButton.clicked(pt):

            if self.saveButton.clicked(pt):
                
                # Open notes file for appending
                # Read entry and save to notes file
                # Reset entry box amd close notes file
                
                outfile = open("myPlanner_notes.txt", 'a')
                self.entry = self.textBox.getText()
                self.textBox.setText("")
                print(self.entry, file=outfile)
                outfile.close()
            
            #file = "myPlanner_notes.txt"
            #os.startfile(file)

            if self.viewButton.clicked(pt):
                
                # Allow viewing of current notes
                file = "myPlanner_notes.txt"
                os.startfile(file)
                
            if self.closeButton.clicked(pt):
                self.win.close()

            # Wait for mouse click
            pt = self.win.getMouse()

        # Close the window on mouse click
        self.win.close()
