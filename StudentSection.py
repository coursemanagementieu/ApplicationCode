from sqlite3 import *
import db_fonk
import csv

connectDatabase = connect("cms.db")
db_cursor = connectDatabase.cursor()


class grade:

    def __init__(self, name, percentage, courseName,semesterName):
        self.name = name
        self.courseName = courseName
        self.percentage = percentage
        self.semesterName=semesterName
        

    def setGradeName(self, name):
        self.name = name

    def setCourseName(self, name):
        self.courseName = name

    def setPercentage(self, percentage):
        self.percentage = percentage


class Section:
    def __init__(self, Name="Empty", day="Empty", hour="Empty", room="Empty"):
        self.sectionID = None
        self.sectionName = Name
        self.day = day
        self.hour = hour
        self.classRoom = room

    def setSectionCode(self, code):
        self.sectionCode = code

    def getSectionCode(self):
        return self.sectionCode

    def setDay(self, day):
        self.day=day

    def getDay(self):
        return self.day

    def setHour(self, hour):
        self.hour=hour

    def getHour(self):
        return self.hour

    def setClassRoom(self, classRoom):
        self.classRoom = classRoom

    def getClassRoom(self):
        return self.classRoom

    def insertSectionInDatabase(self, semID, courseID):
        self.sectionID = db_fonk.insert_section(self.sectionName, self.classRoom, self.hour, self.day)
        db_fonk.insert_sectionin(semID, courseID, self.sectionID)
        db_fonk.save_changes()

    def importStudent(self,semID,courseID):
        tempStudents = []
        file = open('students.csv', "r")
        read = csv.reader(file)
        for row in read:
            for i in row:
                a = i.split(";")
                a.pop(0)
                a = tuple(a)
                tempStudents.append(a)
        for x in tempStudents:
            db_fonk.insert_student(x[0], x[1])
            db_fonk.insert_studentin(semID,courseID,self.sectionID,x[1])
            db_fonk.save_changes()


    def displaySection(self):
        print("Section Code:", self.getSectionCode())
        print("Section Day/s:")
        for i in self.getDay():
            print(i)
        print("Hours:")
        for i in self.getHour():
            print(i)
        print("Classroom:", self.getClassRoom())


class Student():
    def __init__(self, sName, sId):
        self.studentName = sName
        self.studentId = sId
        self.note = []
        self.grade = []

    def setStudentName(self, name):
        self.studentName = name

    def getStudentName(self):
        return self.studentName

    def setStudentId(self, id):
        self.studentId = id

    def getStudentId(self):
        return self.studentId

    def setNote(self, note):
        self.note.append(note)

    def getNote(self):
        return self.note

    def setGrade(self, grade):
        self.grade = grade

    def getGrade(self):
        return self.grade

    def getTotalGrade(self):
        pass

    def getLetterGrade(self):
        pass

    def insertStudentInDatabase(self):
        db_fonk.insert_student(self.studentId, self.studentName)
        db_fonk.save_changes()
        

    def display(self):
        print("Name:", self.getStudentName())
        print("Id:", self.getStudentId())
        print("Notes:")
        counter = 1
        for i in self.getNote():
            print(counter, ":", i)
            counter = counter + 1

