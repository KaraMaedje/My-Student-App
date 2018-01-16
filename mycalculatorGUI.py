#My Calculator
from graphics import*
from button import*

'''this is a class that contains a Calculator program, it follows a simple guide
of what a calculator does'''

''' this program does not fully work, in order for it to run, you need to click "=" everytime you want to submit the object
for example: "2" "=" "X" "=" "5" "=" and then click anywhere on the screen'''

class Calculator:

    def __init__(self):
        ''' intializes the window'''
        self.win = GraphWin("My Calculator", 360, 360)
        self.win.setCoords(0, 0, 360, 360)
        self.win.setBackground("MistyRose")

        #Making all the Buttons
        self.numbers = []
        left = 0
        for self.number in ["7", "8", "9", "/"]:
            self.numbers +=[Button(self.win, Point(50+left, 230), 50,50, self.number)]
            left +=80
        left = 0
        for self.number in ["4", "5", "6", "X"]:
            self.numbers +=[Button(self.win, Point(50+left, 170), 50,50, self.number)]
            left +=80
        left = 0
        for self.number in ["1", "2", "3", "-"]:
            self.numbers +=[Button(self.win, Point(50+left, 110), 50,50, self.number)]
            left +=80
        left = 0
        for self.number in ["0", ".", "=", "+"]:
            self.numbers +=[Button(self.win, Point(50+left, 50), 50,50, self.number)]
            left +=80
        for self.number in self.numbers:
            self.number.activate()
    
        self.quitButton = Button(self.win, Point(345,350), 10, 10, "X")
        self.quitButton.activate()
        
        
        #Intializing to 0 in the begining of the program
        self.newscore= 0
        self.label = Text(Point(290, 300), self.newscore)
        self.label.setFace("arial")
        self.label.setSize(28)
        self.label.setStyle("bold")
        self.label.draw(self.win)

        
        #CALCULATOR TITLE(TEXT)
        self.mycal = Text(Point(90,320), "My Calculator")
        self.mycal.setFace("arial")
        self.mycal.setSize(16)
        self.mycal.setStyle("bold")
        self.mycal.draw(self.win)
        #CALCULATOR TITLE(BOX)
        self.calcu= Rectangle(Point(20,308), Point(160,332))
        self.calcu.setOutline("black")
        self.calcu.draw(self.win)
        
    def close(self):
        self.win.close()

    #Getting all the two numbers
    def get_numbers(self):
        num_1 = self.numbers[i].getText()
        print(num_1)
        num_2 = self.numbers[i].getText()
        
    #Adding function
    def add(self, num_1, num_2):
        if self.numbers[i].getText() == "+":
            num_3= num_1 + num_2
            self.newscore(num_3)
            self.label.setText(self.newscore)
    #Subtracting Function       
    def sub(self, num_1, num_2):
        if self.numbers[i].getText() == "-":
            num_3= num_1 - num_2
            self.newscore(num_3)
            self.label.setText(self.newscore)
            
    #Multiplying Function        
    def multi(self, num_1, num_2):
        if self.numbers[i].getText() == "X":
            num_3= num_1 * num_2
            self.newscore(num_3)
            self.label.setText(self.newscore)
            
    #Dividing Function        
    def divide(self, num_1, num_2):
        if self.numbers[i].getText() == "/":
            num_3= num_1 / num_2
            self.newscore(num_3)
            self.label.setText(self.newscore)
        

    def run(self):
        #Wait for mouse click
        pt = self.win.getMouse()
        number_1 = 0
    
        #Event loop
        count = 0
        list_num=[]
        num = ""
        while not self.quitButton.clicked(pt):
            
            while True:
                pt = self.win.getMouse()
                if not self.numbers[14].clicked(pt):
                    for i in range(len(self.numbers)):
                        #pt= self.win.getMouse()
                        
                        if count >= 3:
                            print("Equals!")
                            if list_num[1] == "X":
                                answer = int(list_num[0]) * int(list_num[2])
                                print(answer)
                                self.newscore = answer
                                self.label.setText(self.newscore)
                            elif list_num[1] == "+":
                                answer = int(list_num[0]) + int(list_num[2])
                                print(answer)
                                self.newscore = answer
                                self.label.setText(self.newscore)
                            elif list_num[1] == "-":
                                answer = int(list_num[0]) - int(list_num[2])
                                print(answer)
                                self.newscore = answer
                                self.label.setText(self.newscore)
                            elif list_num[1] == "/":
                                answer = int(list_num[0]) / int(list_num[2])
                                print(answer)
                                self.newscore = answer
                                self.label.setText(self.newscore)

                            else:
                                answer = "ERROR!"
                                print(answer)
                                self.newscore = answer
                                self.label.setText(self.newscore)
                                
                            break

                        if self.numbers[i].clicked(pt):
                            value = self.numbers[i].getLabel()
                            print(value)

                            num += value
                            print(num)


                            self.newscore = num
                            self.label.setText(self.newscore)


                else:
                    list_num.append(num)
                    print(list_num)
                    num = ""
                    count += 1
                    print(count)
                            
                    #for i in list_num:
                     #   nums.append(i)





                    self.newscore = num
                    self.label.setText(self.newscore)


                    '''
                        number_2 = int(number_1)
                        number_1 = self.numbers[i].getLabel() #debug
                        self.newscore = number_1 
                        self.label.setText(self.newscore)
                        print(number_1, number_2)
                    elif self.numbers[3].clicked(pt) or self.numbers[7].clicked(pt) or self.numbers[11].clicked(pt):
                        print("okay")
                    '''
                    

                    '''if self.numbers[7].clicked(pt):
                        number_3 = (int(number_1) * int(number_2))
                        self.newscore = number_3
                        self.label.setText(self.newscore)'''
                        
                    
        if self.quitButton.clicked(pt):
            self.win.close()
            
            pt = self.win.getMouse()

        self.win.close()
        
    


    



