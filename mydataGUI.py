from graphics import*
from button import*
from student import *

def MyDataGUI(student):
    
    win = GraphWin("My Data", 680, 460)
    win.setCoords(0, 0, 680, 460)
    win.setBackground("Snow")

    # SUBTITLE
    mydata = Text(Point(65,430), "My Data")
    mydata.setFace("arial")
    mydata.setSize(16)
    mydata.setStyle("bold")
    mydata.draw(win)

    mydata= Rectangle(Point(20,415), Point(110,445))
    mydata.setOutline("black")
    mydata.draw(win)

    # SCHEDULE(TITLE)
    schedule = Text(Point(330,430), "Student Timetable")
    schedule.setFace("arial")
    schedule.setSize(12)
    schedule.setStyle("bold")
    schedule.draw(win)
    
    # SCHOOL NAME(TITLE)
    school_name = Text(Point(330,410), "THE BEST Secondary School")
    school_name.setFace("arial")
    school_name.setSize(10)
    school_name.setStyle("bold")
    school_name.draw(win)

    # SCHOOL YEAR(TITLE)
    school_yr = Text(Point(328,390), "School Year: 2015/2016")
    school_yr.setFace("arial")
    school_yr.setSize(10)
    school_yr.setStyle("bold")
    school_yr.draw(win)

    # HOMEROOM(TITLE)
    homeroom = Text(Point(55,385), "HR:  " + student.getHomeRoom())
    homeroom.setFace("arial")
    homeroom.setSize(10)
    homeroom.setStyle("bold")
    homeroom.draw(win)

    # YEAR/GRADE(TITLE)
    year = Text(Point(66,370), "Grade:  " + student.getYear())
    year.setFace("arial")
    year.setSize(10)
    year.setStyle("bold")
    year.draw(win)

    # NAME(TITLE)
    name = Text(Point(550,425), "Name:  " + student.getName())
    name.setFace("arial")
    name.setSize(10)
    name.setStyle("bold")
    name.draw(win)

    # STUDENT NUMBER(TITLE)
    number = Text(Point(550,410), "Student #:  " + student.getStudentNumber())
    number.setFace("arial")
    number.setSize(10)
    number.setStyle("bold")
    number.draw(win)

    # AVERAGE(TITLE)
    average = Text(Point(550,395), "Average:  " + student.getAverage())
    average.setFace("arial")
    average.setSize(10)
    average.setStyle("bold")
    average.draw(win)
    
#==============================================================
#==============================================================
# Read through all the students data and print out the required values
# Part 1 - Print out values for the courses

    d1_courses = student.getCourses()

    # Term 1 - Day 1 
    pt1 = 150
    pt2 = 290
    count1 = 0
    count2 = 0
    for i in range(2):
        course = Text(Point(pt1, (pt2 - count1 - count2)), d1_courses[i])
        count1 += 40
        count2 += 10
        course.setSize(8)
        course.draw(win)

    pt1 = 150
    pt2 = 140
    count1 = 0
    count2 = 0
    for i in range(2):
        course = Text(Point(pt1, (pt2 - count1 - count2)), d1_courses[i+2])
        count1 += 40
        count2 += 10
        course.setSize(8)
        course.draw(win)

    d2_courses = []
    d2_courses.append(d1_courses[1])
    d2_courses.append(d1_courses[0])
    d2_courses.append(d1_courses[3])
    d2_courses.append(d1_courses[2])

    # Term 1 - Day 2  
    pt1 = 288
    pt2 = 290
    count1 = 0
    count2 = 0
    for i in range(2):
        course = Text(Point(pt1, (pt2 - count1 - count2)), d2_courses[i])
        count1 += 40
        count2 += 10
        course.setSize(8)
        course.draw(win)

    pt1 = 288
    pt2 = 140
    count1 = 0
    count2 = 0
    for i in range(2):
        course = Text(Point(pt1, (pt2 - count1 - count2)), d2_courses[i+2])
        count1 += 40
        count2 += 10
        course.setSize(8)
        course.draw(win)


    # Term 2 - Day 1
    d1_courses2 = d1_courses[4:]
    pt1 = 435
    pt2 = 290
    count1 = 0
    count2 = 0
    for i in range(2):
        course = Text(Point(pt1, (pt2 - count1 - count2)), d1_courses2[i])
        count1 += 40
        count2 += 10
        course.setSize(8)
        course.draw(win)
    
    pt1 = 435
    pt2 = 140
    count1 = 0
    count2 = 0
    for i in range(2):
        course = Text(Point(pt1, (pt2 - count1 - count2)), d1_courses2[i+2])
        count1 += 40
        count2 += 10
        course.setSize(8)
        course.draw(win)
    
    # Term 2 - Day 2
    d2_courses2 = []
    d2_courses2.append(d1_courses[5])
    d2_courses2.append(d1_courses[4])
    d2_courses2.append(d1_courses[7])
    d2_courses2.append(d1_courses[6])
    
    pt1 = 588
    pt2 = 290
    count1 = 0
    count2 = 0
    for i in range(2):
        course = Text(Point(pt1, (pt2 - count1 - count2)), d2_courses2[i])
        count1 += 40
        count2 += 10
        course.setSize(8)
        course.draw(win)

    pt1 = 588
    pt2 = 140
    count1 = 0
    count2 = 0
    for i in range(2):
        course = Text(Point(pt1, (pt2 - count1 - count2)), d2_courses2[i+2])
        count1 += 40
        count2 += 10
        course.setSize(8)
        course.draw(win)

#==============================================================
#==============================================================
# Part 2 - Print out values for the teachers

    #Term 1 - Day 1
    d1_teachers = student.getTeachers()
    
    pt1 = 150
    pt2 = 275
    count1 = 0
    count2 = 0
    for i in range(2):
        teacher = Text(Point(pt1, (pt2 - count1 - count2)), d1_teachers[i])
        count1 += 40
        count2 += 10
        teacher.setSize(8)
        teacher.draw(win)

    pt1 = 150
    pt2 = 125
    count1 = 0
    count2 = 0
    for i in range(2):
        teacher = Text(Point(pt1, (pt2 - count1 - count2)), d1_teachers[i+2])
        count1 += 40
        count2 += 10
        teacher.setSize(8)
        teacher.draw(win)

    d2_teachers = []
    d2_teachers.append(d1_teachers[1])
    d2_teachers.append(d1_teachers[0])
    d2_teachers.append(d1_teachers[3])
    d2_teachers.append(d1_teachers[2])


    # Term 1 - Day 2  
    pt1 = 288
    pt2 = 275
    count1 = 0
    count2 = 0
    for i in range(2):
        teacher = Text(Point(pt1, (pt2 - count1 - count2)), d2_teachers[i])
        count1 += 40
        count2 += 10
        teacher.setSize(8)
        teacher.draw(win)

    pt1 = 288
    pt2 = 125
    count1 = 0
    count2 = 0
    for i in range(2):
        teacher = Text(Point(pt1, (pt2 - count1 - count2)), d2_teachers[i+2])
        count1 += 40
        count2 += 10
        teacher.setSize(8)
        teacher.draw(win)


    # Term 2 - Day 1
    d1_teachers2 = d1_teachers[4:]
    pt1 = 435
    pt2 = 275
    count1 = 0
    count2 = 0
    for i in range(2):
        teacher = Text(Point(pt1, (pt2 - count1 - count2)), d1_teachers2[i])
        count1 += 40
        count2 += 10
        teacher.setSize(8)
        teacher.draw(win)
    
    pt1 = 435
    pt2 = 125
    count1 = 0
    count2 = 0
    for i in range(2):
        teacher = Text(Point(pt1, (pt2 - count1 - count2)), d1_teachers2[i+2])
        count1 += 40
        count2 += 10
        teacher.setSize(8)
        teacher.draw(win)

    # Term 2 - Day 2
    d2_teachers2 = []
    d2_teachers2.append(d1_teachers[5])
    d2_teachers2.append(d1_teachers[4])
    d2_teachers2.append(d1_teachers[7])
    d2_teachers2.append(d1_teachers[6])
    
    pt1 = 588
    pt2 = 275
    count1 = 0
    count2 = 0
    for i in range(2):
        teacher = Text(Point(pt1, (pt2 - count1 - count2)), d2_teachers2[i])
        count1 += 40
        count2 += 10
        teacher.setSize(8)
        teacher.draw(win)

    pt1 = 588
    pt2 = 125
    count1 = 0
    count2 = 0
    for i in range(2):
        teacher = Text(Point(pt1, (pt2 - count1 - count2)), d2_teachers2[i+2])
        count1 += 40
        count2 += 10
        teacher.setSize(8)
        teacher.draw(win)

#==============================================================
#==============================================================
# Part 3 - Print out the values for the rooms

    # Term 1 - Day 1
    d1_rooms = student.getRooms()
    
    pt1 = 150
    pt2 = 260
    count1 = 0
    count2 = 0
    for i in range(2):
        room = Text(Point(pt1, (pt2 - count1 - count2)), d1_rooms[i])
        count1 += 40
        count2 += 10
        room.setSize(8)
        room.draw(win)

    pt1 = 150
    pt2 = 110
    count1 = 0
    count2 = 0
    for i in range(2):
        room = Text(Point(pt1, (pt2 - count1 - count2)), d1_rooms[i+2])
        count1 += 40
        count2 += 10
        room.setSize(8)
        room.draw(win)

    d2_rooms = []
    d2_rooms.append(d1_rooms[1])
    d2_rooms.append(d1_rooms[0])
    d2_rooms.append(d1_rooms[3])
    d2_rooms.append(d1_rooms[2])


    # Term 1 - Day 2  
    pt1 = 288
    pt2 = 260
    count1 = 0
    count2 = 0
    for i in range(2):
        room = Text(Point(pt1, (pt2 - count1 - count2)), d2_rooms[i])
        count1 += 40
        count2 += 10
        room.setSize(8)
        room.draw(win)

    pt1 = 288
    pt2 = 110
    count1 = 0
    count2 = 0
    for i in range(2):
        room = Text(Point(pt1, (pt2 - count1 - count2)), d2_rooms[i+2])
        count1 += 40
        count2 += 10
        room.setSize(8)
        room.draw(win)


    # Term 2 - Day 1
    d1_rooms2 = d1_rooms[4:]
    pt1 = 435
    pt2 = 260
    count1 = 0
    count2 = 0
    for i in range(2):
        room = Text(Point(pt1, (pt2 - count1 - count2)), d1_rooms2[i])
        count1 += 40
        count2 += 10
        room.setSize(8)
        room.draw(win)
    
    pt1 = 435
    pt2 = 110
    count1 = 0
    count2 = 0
    for i in range(2):
        room = Text(Point(pt1, (pt2 - count1 - count2)), d1_rooms2[i+2])
        count1 += 40
        count2 += 10
        room.setSize(8)
        room.draw(win)

    # Term 2 - Day 2
    d2_rooms2 = []
    d2_rooms2.append(d1_rooms[5])
    d2_rooms2.append(d1_rooms[4])
    d2_rooms2.append(d1_rooms[7])
    d2_rooms2.append(d1_rooms[6])
    #print("in here", d2_rooms2)
    
    pt1 = 588
    pt2 = 260
    count1 = 0
    count2 = 0
    for i in range(2):
        room = Text(Point(pt1, (pt2 - count1 - count2)), d2_rooms2[i])
        count1 += 40
        count2 += 10
        room.setSize(8)
        room.draw(win)

    pt1 = 588
    pt2 = 110
    count1 = 0
    count2 = 0
    for i in range(2):
        room = Text(Point(pt1, (pt2 - count1 - count2)), d2_rooms2[i+2])
        count1 += 40
        count2 += 10
        room.setSize(8)
        room.draw(win)
        
    #--------------------------------------------------
    # Return to formating the GUI 
    # LINES
    # x
    line = Line(Point(20,50), Point(20,340))
    line.draw(win)  
    line = Line(Point(85,50), Point(85,340))
    line.draw(win)
    line = Line(Point(215,50), Point(215,340))
    line.draw(win)
    line = Line(Point(365,50), Point(365,340))
    line.draw(win)
    line = Line(Point(515,50), Point(515,340))
    line.draw(win)
    line = Line(Point(665,50), Point(665,340))
    line.draw(win)
    
    # y
    line = Line(Point(20,340), Point(666,340))
    line.draw(win)
    line = Line(Point(20,300), Point(665,300))
    line.draw(win)
    line = Line(Point(20,250), Point(665,250))
    line.draw(win)
    line = Line(Point(20,200), Point(665,200))
    line.draw(win)
    line = Line(Point(20,150), Point(665,150))
    line.draw(win)
    line = Line(Point(20,100), Point(665,100))
    line.draw(win)
    line = Line(Point(20,50), Point(665,50))
    line.draw(win)
    line = Line(Point(20,50), Point(665,50))
    line.draw(win)

    # TEXT
    text = Text(Point(150,320), "Term 1 Day 1")
    text.setStyle("bold")
    text.draw(win)
    text = Text(Point(290,320), "Term 1 Day 2")
    text.setStyle("bold")
    text.draw(win)

    text = Text(Point(440,320), "Term 2 Day 1")
    text.setStyle("bold")
    text.draw(win)
    text = Text(Point(590,320), "Term 2 Day 2")
    text.setStyle("bold")
    text.draw(win)

    # LUNCH TEXT
    lunch = Text(Point(150,175), "LUNCH")
    lunch.setStyle("bold")
    lunch.draw(win)
    lunch_2 = Text(Point(290,175), "LUNCH")
    lunch_2.setStyle("bold")
    lunch_2.draw(win)
    lunch_3 = Text(Point(440,175), "LUNCH")
    lunch_3.setStyle("bold")
    lunch_3.draw(win)
    lunch_4 = Text(Point(590,175), "LUNCH")
    lunch_4.setStyle("bold")
    lunch_4.draw(win)

    # TIMES TEXT
    time = Text(Point(54,280), "8:30 - 9:40")
    time.setSize(8)
    time.draw(win)
    p1 =Text(Point(54,260), "P1")
    p1.setStyle("bold")
    p1.setSize(8)
    p1.draw(win)
    time_2 = Text(Point(54,230), "9:50 - 11:10")
    time_2.setSize(8)
    time_2.draw(win)
    p2 =Text(Point(53.5,210), "P2")
    p2.setStyle("bold")
    p2.setSize(8)
    p2.draw(win)
    time_3 = Text(Point(53.5,175), "11:10 - 12:10")
    time_3.setSize(8)
    time_3.draw(win)
    time_4 = Text(Point(54,130), "12:10 - 1:25")
    time_4.setSize(8)
    time_4.draw(win)
    p3 =Text(Point(55,110), "P3")
    p3.setStyle("bold")
    p3.setSize(8)
    p3.draw(win)
    time_5 = Text(Point(54,80), "1:25 - 2:45")
    time_5.setSize(8)
    time_5.draw(win)
    p4 =Text(Point(53.5,60), "P4")
    p4.setStyle("bold")
    p4.setSize(8)
    p4.draw(win)

