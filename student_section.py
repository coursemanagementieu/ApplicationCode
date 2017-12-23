
import db_fonk
import csv


class Grade:

    def __init__(self):
        self.name = None
        self.percentage = None
        self.ID = None

    def setGradeName(self, name):
        self.name = name

    def setPercentage(self, percentage):
        self.percentage = percentage

    def setID(self, rowid):
        self.ID = rowid

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

    def get_rowid_from_database(self, semesterName, courseID):
        self.ID = db_fonk.select_evaluiaton_rowid(semesterName, courseID, self.name)

    def get_info_from_database(self):
        info = db_fonk.select_specific_evaluation(self.ID)
        self.setGradeName(info[0])
        self.setPercentage(info[1])

    def edit_evaluation(self):
        db_fonk.edit_evaluation(self.ID, self.name, self.percentage)

    def delete_evaluation(self):
        db_fonk.delete_evaluation(self.ID)

    # This function return rowid of evaluations which are in given semester and course
    def get_all_evaluation_in(self, semesterName, courseID):
        return db_fonk.select_all_evaluation_in(semesterName, courseID)


class Section:
    def __init__(self):
        self.sectionID = None
        self.sectionName = None
        self.day = None
        self.hour = None
        self.classRoom = None

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

    def setSectionID(self, rowid):
        self.sectionID = rowid

    def getSectionID(self):
        return self.sectionID

# These functions is related with database
    def insertSectionInDatabase(self, semID, courseID):
        self.sectionID = db_fonk.insert_section(self.sectionName, self.classRoom, self.hour, self.day)
        db_fonk.insert_sectionin(semID, courseID, self.sectionID)

    # Before using this function we need to know sectionName
    def get_rowid_from_database(self, semesterName, courseID):
        self.sectionID = db_fonk.select_section_rowid(semesterName, courseID, self.sectionName)

    # Return of the sectionin table gives us rowid and we can find information of it with using this function
    def get_info_from_database(self):
        info = db_fonk.select_specific_section(self.sectionID)
        self.setSectionName(info[0])
        self.setClassRoom(info[1])
        self.setHour(info[2])
        self.setDay(info[3])

    def edit_section(self):
        db_fonk.edit_section(self.sectionID, self.sectionName, self.classRoom, self.hour, self.day)

    def delete_section(self):
        db_fonk.delete_section(self.sectionID)

    def get_all_section_in(self, semesterName, courseID):
        return db_fonk.select_all_section_in(semesterName, courseID)

    # This function is working ok, but how do you know that these student which are added is in this semester, course
    # and section?
    def importStudent(self, semID, courseID):
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


class Student():
    def __init__(self):
        self.studentName = None
        self.studentId = None
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
        db_fonk.insert_student(self.studentId, self.studentName)
        db_fonk.insert_studentin(semesterName, courseID, sectionID, self.studentId)

    def get_info_from_database(self):
        info = db_fonk.select_specific_student(self.studentId)
        self.setStudentName(info[0])

    def edit_student(self):
        db_fonk.edit_student(self.studentId, self.studentName)

    def delete_student(self):
        db_fonk.delete_student(self.studentId)

    def get_all_student_in(self, semesterName, courseID, sectionID):
        return db_fonk.select_all_student_in(semesterName, courseID, sectionID)

    def insert_student_grade_in_database(self, semesterName, courseID, evaluationID):
        db_fonk.insert_student_evaluationin(semesterName, courseID, evaluationID, self.studentId, self.grade)

    def edit_student_evaluation(self, semesterName, courseID, evaluationID):
        db_fonk.edit_studentEvaluation_in(semesterName, courseID, evaluationID, self.studentId, self.grade)

    def get_student_evaluation_info_from_database(self, semesterName, courseID, evaluationID):
        self.grade = db_fonk.select_studentEvaluation_in(semesterName, courseID, evaluationID, self.studentId)

    def get_evaluationID_from_studentGrade_in(self, semesterName, courseID):
        return db_fonk.select_evaluationID_studentEvaluation_in(semesterName, courseID, self.studentId)


class Note:
    def __init__(self):
        self.head = None
        self.note = None
        self.date = None
        self.ID = None

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

    def setID(self, rowid):
        self.ID = rowid

    def getID(self):
        return self.ID

    def insertNoteInDatabase(self, semesterName, courseID, studentID):
        self.ID = db_fonk.insert_note(self.head, self.note, self.date)
        db_fonk.insert_notein(semesterName, courseID, studentID, self.ID)

    def get_rowid_from_database(self, semesterName, courseID, studentID):
        self.ID = db_fonk.select_note_rowid(semesterName, courseID, studentID, self.head)

    def get_info_from_database(self):
        info = db_fonk.select_specific_note(self.ID)
        self.setHead(info[0])
        self.setNote(info[1])
        self.setDate(info[2])

    def edit_note(self):
        db_fonk.edit_note(self.ID, self.head, self.note, self.date)

    def delete_note(self):
        db_fonk.delete_note(self.ID)

    def get_all_note_in(self, semesterName, courseID, studentID):
        return db_fonk.select_all_note_in(semesterName, courseID, studentID)