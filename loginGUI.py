from graphics import *
from button import *
import time

class LoginGUI:
 
    def __init__(self):

        # Create graphic window
        self.win = GraphWin("School App", 360, 360)
        self.win.setCoords(0, 0, 360, 360)
        self.win.setBackground("MistyRose")

        # Drawing Labels (Username and Password)
        label = Text(Point(92, 170), "Username: ")
        label.setFace("arial")
        label.setSize(13)
        label.setStyle("bold")
        label.draw(self.win)

        label2 = Text(Point(92, 110), "Password: ")
        label2.setFace("arial")
        label2.setSize(13)
        label2.setStyle("bold")
        label2.draw(self.win)
        
        # Entry box for input
        self.username = Entry(Point(115, 145), 15)
        self.username.setText("")
        self.username.setFill("Snow")
        self.username.draw(self.win)
        
        self.password = Entry(Point(115, 85), 15)
        self.password.setText("")
        self.password.setFill("Snow")
        self.password.draw(self.win)
        
        # Creating Buttons
        self.loginButton = Button(self.win, Point(260,117), 102, 30, "Log In")
        self.loginButton.rect.setFill("floral white")
        self.loginButton.activate()
        self.quitButton = Button(self.win, Point(320,320), 15,18, "X")
        self.quitButton.activate()
        
        # Making Borders
        box = Rectangle(Point(10,10), Point(350,350))
        box.setOutline("Snow")
        box.setWidth(4)
        box.draw(self.win)

        box2 = Rectangle(Point(20,20), Point(340,340))
        box2.setOutline("Snow")
        box2.setWidth(3)
        box2.draw(self.win)

        # Title
        title = Text(Point(170, 315), "My Student App")
        title.setSize(15)
        title.setFace("arial")
        title.setStyle("bold")
        title.draw(self.win)
        
        # Display Logo Image 
        logo = Image(Point(170, 245), "temp.png")
        logo.draw(self.win)
        
    def close(self):
        self.win.close()

    def getLogin(self):
        return self.login

    def getUserData(self):
        return self.user_data

    def run(self):
        self.login = False
        self.user_data = []

        # Read data file and pull out valid usernames and passwords
        all_info = []
        file = open("passwords.txt", 'r')
        for line in file.readlines():
            data = line.split("\t")
            user_info = []
            username = data[0]
            password = data[1]
            user_info.append(username)
            user_info.append(password[:-1])
            all_info.append(user_info)
        file.close()

        # Initialize Successful/Failed Login Message
        self.fail_msg = Text(Point(108, 65), "")
        self.fail_msg.setSize(7)
        self.fail_msg.setFill("red")
        self.fail_msg.draw(self.win)

        self.success_msg = Text(Point(86, 65), "")
        self.success_msg.setSize(7)
        self.success_msg.setFill("blue")
        self.success_msg.draw(self.win)

        self.success_msg.setText("")
        self.fail_msg.setText("")

        #print(all_info)
        pt = self.win.getMouse()

        while True:

            # Get username and password entered by user
            if self.loginButton.clicked(pt):
                user_data = []
                user_data.append(self.username.getText())
                user_data.append(self.password.getText())

                # Clear the username and password entry boxes
                self.username.setText("")
                self.password.setText("")

                # Check if username/password entered is valid
                if user_data in all_info:

                    print("Successful Log In.")
                    self.user_data = user_data
                    self.login = True

                    self.loginButton.deactivate()

                    self.username.setText("")
                    self.password.setText("")
                    
                    self.fail_msg.setText("")
                    self.success_msg.setText("Login Successful")

                    time.sleep(1)
                    
                    #---------------------------------------
                    # Creating and running loading animation
                    #---------------------------------------
                    
                    # Create loading bar
                    bar = Rectangle(Point(110, 35), Point(230, 45))
                    bar.setFill("grey")
                    bar.setOutline("black")
                    bar.draw(self.win)

                    # Display initial message
                    self.message = Text(Point(285, 55), "Loading...")
                    self.message.setSize(8)
                    self.message.draw(self.win)

                    # Display initial percentage
                    self.percentage = Text(Point(285, 40), "0%")
                    self.percentage.setSize(10)
                    self.percentage.draw(self.win)
                    
                    # Create loading boxes and display loading percentages 
                    box = Rectangle(Point(110, 35), Point(134, 45))
                    box.setFill("lightblue")
                    time.sleep(0.5)
                    box.draw(self.win)
                    self.percentage.setText("20%")

                    box = Rectangle(Point(134, 35), Point(158, 45))
                    box.setFill("lightblue")
                    time.sleep(0.5)
                    box.draw(self.win)
                    self.percentage.setText("40%")

                    box = Rectangle(Point(158, 35), Point(182, 45))
                    box.setFill("lightblue")
                    time.sleep(0.5)
                    box.draw(self.win)
                    self.percentage.setText("60%")
                    
                    box = Rectangle(Point(182, 35), Point(206, 45))
                    box.setFill("lightblue")
                    time.sleep(0.5)
                    box.draw(self.win)
                    self.percentage.setText("80%")
                    
                    box = Rectangle(Point(206, 35), Point(230, 45))
                    box.setFill("lightblue")
                    time.sleep(0.5)
                    box.draw(self.win)
                    self.percentage.setText("100%")

                    # Display final message
                    self.message.setText("Loading Complete!")
                    time.sleep(1)
                    
                    self.win.close()
                    break
                    

                #If login was unsuccessful
                else:
                    self.fail_msg.setText("Invalid Username/Password!") 
                    print("Unsuccessful Log In.")

            if self.quitButton.clicked(pt):
                self.win.close()

            pt = self.win.getMouse()
