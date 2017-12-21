
import db_fonk
import csv


class Grade:

    def __init__(self,  semesterName, courseID, gradeName="Empty", percentage=0):
        self.name = gradeName
        self.percentage = percentage
        self.ID = None
        self.insertGradeInDB(semesterName, courseID)


    def setGradeName(self, name):
        self.name = name

    def setPercentage(self, percentage):
        self.percentage = percentage

    def getGradeName(self):
        return self.name

    def getPercentage(self):
        return self.percentage

    def get_ID(self):
        return self.ID

    # These function will be related with database
    def insertGradeInDB(self, semesterName, courseID):
        self.ID = db_fonk.insert_evaluation(self.name, self.percentage)
        db_fonk.insert_evaluationin(semesterName, courseID, self.ID)

    def get_info_from_database(self, semesterName, courseID, evaluationName):
        self.ID = db_fonk.select_evaluiaton_rowid(semesterName, courseID, evaluationName)
        self.get_info_from_database_with_rowid(self.ID)

    def get_info_from_database_with_rowid(self, rowid):
        self.ID = rowid
        info = db_fonk.select_specific_evaluation(self.ID)
        self.setGradeName(info[0])
        self.setPercentage(info[1])

    def edit_evaluation(self, semesterName, courseID, evaluationName):
        self.get_info_from_database(semesterName, courseID, evaluationName)
        self.get_info_from_database_with_rowid(self.ID)
        # Here system waits for user to make any change
        db_fonk.edit_evaluation(self.ID, self.name, self.percentage)

    def delete_evaluation(self, semesterName, courseID, evaluationName):
        self.ID = db_fonk.select_evaluiaton_rowid(semesterName, courseID, evaluationName)
        db_fonk.delete_evaluation(self.ID)

    # This function return rowid of evaluations which are in given semester and course
    def select_all_evaluation_in(self, semesterName, courseID):
        return db_fonk.select_all_evaluation_in(semesterName, courseID)


class Section:
    def __init__(self, semesterName, courseID,name="Empty", day="Empty", hour="Empty", room="Empty"):
        self.sectionID = None
        self.sectionName = name
        self.day = day
        self.hour = hour
        self.classRoom = room
        self.insertSectionInDatabase(semesterName, courseID)

    def setSectionName(self, name):
        self.sectionName = name

    def getSectionName(self):
        return self.sectionName

    def setDay(self, day):
        self.day = day

    def getDay(self):
        return self.day

    def setHour(self, hour):
        self.hour = hour

    def getHour(self):
        return self.hour

    def setClassRoom(self, classRoom):
        self.classRoom = classRoom

    def getClassRoom(self):
        return self.classRoom

# These functions is related with database
    def insertSectionInDatabase(self, semID, courseID):
        self.sectionID = db_fonk.insert_section(self.sectionName, self.classRoom, self.hour, self.day)
        db_fonk.insert_sectionin(semID, courseID, self.sectionID)

    def get_info_from_databe(self, semesterName, courseID, name):
        self.sectionID = db_fonk.select_section_rowid(semesterName, courseID, name)

    # Return of the sectionin table gives us rowid and we can find information of it with using this function
    def get_info_from_database_with_rowid(self, rowid):
        self.sectionID = rowid
        info = db_fonk.select_specific_section(self.sectionID)
        self.setSectionName(info[0])
        self.setClassRoom(info[1])
        self.setHour(info[2])
        self.setDay(info[3])

    def edit_section(self, semesterName, courseID, name):
        self.get_info_from_databe(semesterName, courseID, name)
        self.get_info_from_database_with_rowid(self.sectionID)
        # Here system waits for user to make any change
        db_fonk.edit_section(self.sectionID, self.sectionName, self.classRoom, self.hour, self.day)

    def delete_section(self, semesterName, courseID, name):
        self.get_info_from_databe(semesterName, courseID, name)
        db_fonk.delete_section(self.sectionID)

    def select_all_section_in(self, semesterName, courseID):
        return db_fonk.select_all_section_in(semesterName, courseID)

    # This function is working ok, but how do you know that these student which are added is in this semester, course
    # and section?
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
        print("Section Code:", self.getSectionName())
        print("Section Day/s:")
        for i in self.getDay():
            print(i)
        print("Hours:")
        for i in self.getHour():
            print(i)
        print("Classroom:", self.getClassRoom())


class Student():
    def __init__(self, semesterName, courseID, sectionID, sName, sId):
        self.studentName = sName
        self.studentId = sId
        self.ID = None
        self.insertStudentInDatabase(semesterName, courseID, sectionID)
        self.grade = None

    def setStudentName(self, name):
        self.studentName = name

    def getStudentName(self):
        return self.studentName

    def setStudentId(self, id):
        self.studentId = id

    def getStudentId(self):
        return self.studentId

    def setStudentGrade(self, evaluation):
        self.grade = evaluation

    def getStudentGrade(self):
        return self.grade

    # def getTotalGrade(self):
    #     pass
    #
    # def getLetterGrade(self):
    #     pass

    def insertStudentInDatabase(self, semesterName, courseID, sectionID):
        self.ID = db_fonk.insert_student(self.studentId, self.studentName)
        db_fonk.insert_studentin(semesterName, courseID, sectionID, self.ID)

    def get_info_from_database(self, studentID):
        info = db_fonk.select_specific_student(studentID)
        self.setStudentName(info[0])

    def edit_student(self, studentID):
        self.get_info_from_database(studentID)
        # Here system waits for user to make any change
        db_fonk.edit_student(self.studentId, self.studentName)

    def delete_student(self, studentID):
        db_fonk.delete_student(studentID)

    def get_all_student_in(self, semesterName, courseID, sectionID):
        return db_fonk.select_all_student_in(semesterName, courseID, sectionID)

    def insert_student_grade_in_database(self, semesterName, courseID, evaluationID, studentID, evaluation):
        db_fonk.insert_student_evaluationin(semesterName, courseID, evaluationID, studentID, evaluation)

    def edit_student_evaluation(self, semesterName, courseID, evaluationID, studentID, evaluation):
        db_fonk.edit_studentEvaluation_in(semesterName, courseID, evaluationID, studentID, evaluation)

    def get_student_evaluation_info_from_database(self, semesterName, courseID, evaluationID, studentID):
        self.grade = db_fonk.select_studentEvaluation_in(semesterName, courseID, evaluationID, studentID)

    def display(self):
        print("Name:", self.getStudentName())
        print("Id:", self.getStudentId())
        print("Notes:")
        counter = 1
        for i in self.getNote():
            print(counter, ":", i)
            counter = counter + 1


class Note:
    def __init__(self, semesterName, courseID, studentID, head="Empty", note="Empty", date="Empty"):
        self.head = head
        self.note = note
        self.date = date
        self.ID = None
        self.insertNoteInDatabase(semesterName, courseID, studentID)

    def setHead(self, head):
        self.head = head

    def getHead(self):
        return self.head

    def setNote(self, note):
        self.note = note

    def getNote(self):
        return self.note

    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date

    def insertNoteInDatabase(self, semesterName, courseID, studentID):
        self.ID = db_fonk.insert_note(self.head, self.note, self.date)
        db_fonk.insert_notein(semesterName, courseID, studentID, self.ID)

    def get_info_from_database(self, semesterName, courseID, studentID, head):
        self.ID = db_fonk.select_note_rowid(semesterName, courseID, studentID, head)

    def get_info_from_database_with_rowid(self, rowid):
        self.ID = rowid
        info = db_fonk.select_specific_note(self.ID)
        self.setHead(info[0])
        self.setNote(info[1])
        self.setDate(info[2])

    def edit_note(self, semesterName, courseID, studentID, head):
        self.get_info_from_database(semesterName, courseID, studentID, head)
        self.get_info_from_database_with_rowid(self.ID)
        # Here system waits for user to make any change
        db_fonk.edit_note(self.ID, self.head, self.note, self.date)

    def delete_note(self, semesterName, courseID, studentID, head):
        self.get_info_from_database(semesterName, courseID, studentID, head)
        db_fonk.delete_note(self.ID)

    def get_all_note_in(self, semesterName, courseID, studentID):
        return db_fonk.select_all_note_in(semesterName, courseID, studentID)