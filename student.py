#STUDENT CLASS 

class Student:

    def __init__(self, info):

        # Initialize the student data
        self.info = info
        self.homeroom = info[0]
        self.name = info[1]
        self.studentnumber = info[2]
        self.year = info[3]
        self.initializeSemesters()
        self.initializePeriods()
        self.initializeRooms()
        self.initializeTeachers()
        self.initializeCourses()
        self.initializeGrades()
        self.initializeAverage()
        

    def initializeSemesters(self):
        self.semesters = []
        index = 4
        while index < len(self.info):
            self.semesters.append(self.info[index])
            index += 6

    def initializePeriods(self):
        self.periods = []
        index = 5
        while index < len(self.info):
            self.periods.append(self.info[index])
            index += 6

    def initializeRooms(self):
        self.rooms = []
        index = 6
        while index < len(self.info):
            self.rooms.append(self.info[index])
            index += 6

    def initializeTeachers(self):
        self.teachers = []
        index = 7
        while index < len(self.info):
            self.teachers.append(self.info[index])
            index += 6

    def initializeCourses(self):
        self.courses = []
        index = 8
        while index < len(self.info):
            self.courses.append(self.info[index])
            index += 6

    def initializeGrades(self):
        self.grades = []
        index = 9
        while index < len(self.info):
            self.grades.append(self.info[index])
            index += 6

    def initializeAverage(self):
        total = 0
        for i in self.grades:
            mark = int(i)
            total += mark
        self.average = round(total/(len(self.grades)),1)


    # Return data as their respective values 
    def getHomeRoom(self):
        return self.homeroom
    
    def getName(self):
        return self.name

    def getStudentNumber(self):
        return self.studentnumber

    def getYear(self):
        return self.year
            
    def getSemesters(self):
        return self.semesters

    def getPeriods(self):
        return self.periods

    def getRooms(self):
        return self.rooms

    def getTeachers(self):
        return self.teachers

    def getCourses(self):
        return self.courses
        
    def getGrades(self):
        return self.grades

    def getAverage(self):
        return str(self.average)
                         
    
