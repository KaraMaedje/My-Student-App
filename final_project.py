from student import *
from loginGUI import *
from mainGUI import *

# Gets all valid ID's
def getID(a):
    return a[2]

# Searches data file for specific individuals data
def search(l, n):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high)//2
        if n == l[mid][2]:
            return mid
        elif n < l[mid][2]:
            high = mid - 1
        else:
            low = mid + 1 
    return -1

def main():

    # Run the login gui
    login = LoginGUI()
    login.run()

    if login.getLogin():
        user_data = login.getUserData()

        # Match the user to their data
        users_file = []
        file = open("kara_hajra.txt", 'r')
        for lines in file.readlines():
            info = lines[:-1].split("\t")
            users_file.append(info)
        file.close()

        # Sort all user data list by ID
        users_file.sort(key=getID)
        #print(users_file)
        
        # Perform binary search to find user_data[0]
        index = search(users_file, user_data[0])
        
        # CREATING/WORKING WITH STUDENT CLASS TO PULL OUT ALL INFO            
        student = Student(users_file[index])
        
        # DEBUGGING 
        homeroom = student.getHomeRoom() 
        print("HR:", homeroom)                      
        name = student.getName()
        print("Name:", name)
        year = student.getYear()
        print("Year/Grade:", year)
        number = student.getStudentNumber()
        print("Student ID:", number)
        semesters = student.getSemesters()
        print("Semesters:", semesters)
        periods = student.getPeriods()    
        print("Periods:", periods)
        rooms = student.getRooms()    
        print("Rooms:", rooms)
        teachers = student.getTeachers()    
        print("Teachers:", teachers)
        courses = student.getCourses()    
        print("Courses:", courses)
        grades = student.getGrades()    
        print("Grades:", grades)
        average = student.getAverage()
        print("Average:", average)
        
        # Run the main menu gui
        gui = MainGUI(student)
        gui.run()

             
main()
