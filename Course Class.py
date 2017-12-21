import db_fonk


class Course:

    def __init__(self, semesterName, courseName="Empty", courseCode="Empty", courseBook="Empty", refBookName="Empty",
                 syllabus="Empty"):
        self.courseName = courseName
        self.courseCode = courseCode
        self.courseID = None
        self.courseBook = courseBook
        self.refBookName = refBookName
        self.syllabus = syllabus
        self.insertCourseInDatabase(semesterName)

    def setCourseName(self, name):
        self.courseName = name

    def setCourseCode(self, code):
        self.courseCode = code

    def setCourseSyllabus(self, syllabus):
        self.syllabus = syllabus

    def setCourseBook(self, book):
        self.courseBook = book

    def setRefBookName(self, refbook):
        self.refBookName = refbook

    def getCourseName(self):
        return self.courseName

    def getCourseCode(self):
        return self.courseCode

    def getCourseBook(self):
        return self.courseBook

    def getRefBookName(self):
        return self.refBookName

    def getsyllabus(self):
        return self.syllabus

    def get_courseID(self):
        return self.courseID

    # These functions is related with database
    def insertCourseInDatabase(self,semesterName):
        self.courseID = db_fonk.insert_course(self.courseName, self.courseCode, self.courseBook,
                                              self.refBookName, self.syllabus)
        db_fonk.insert_coursein(semesterName, self.courseID)

    def edit_course(self, semesterName, courseCode):
        self.get_info_from_database(semesterName, courseCode)
        # Here system waits for user to make any change
        db_fonk.edit_course(self.courseID, self.courseName, self.courseCode, self.courseBook,
                            self.refBookName, self.syllabus)

    def get_info_from_database(self, semesterName, courseCode):
        self.courseID = db_fonk.select_course_rowid(semesterName, courseCode)
        self.get_info_from_database_with_rowid(self.courseID)

    # This function will be using since we know the rowid
    def get_info_from_database_with_rowid(self, rowid):
        self.courseID = rowid
        info = db_fonk.select_specific_course(self.courseID)
        self.setCourseName(info[0])
        self.setCourseCode(info[1])
        self.setCourseBook(info[2])
        self.setRefBookName(info[3])
        self.setCourseSyllabus(info[4])

    # Display all of the courses in specific semester
    def display_all_course_in(self, semesterName):
        # This return will be handled in the gui part and since knowing rowid it calls get_info_from_database_with_rowid
        # to get the data
        return db_fonk.select_all_course_in_semester(semesterName)

    def delete_course(self, semesterName, courseCode):
        self.courseID = db_fonk.select_course_rowid(semesterName, courseCode)
        db_fonk.delete_course(self.courseID)
        

class Announcement:
    def __init__(self, semesterName, courseID, date="Empty", head="Empty", announcement="Empty"):
        self.date = date
        self.head = head
        self.announcement = announcement
        self.ID = None
        self.insertAnnouncementInDatabase(semesterName,courseID)

    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date

    def setHead(self, head):
        self.head = head

    def getHead(self):
        return self.head

    def setAnnouncement(self, announcement):
        self.announcement = announcement

    def getAnnouncement(self):
        return self.announcement

    # These functions are related with database
    def insertAnnouncementInDatabase(self, semesterName, courseID):
        self.ID = db_fonk.insert_announcement(self.date, self.head, self.announcement)
        db_fonk.insert_announcementin(semesterName, courseID, self.ID)

    def get_rowid_from_database(self, semesterName, courseID, head):
        self.ID = db_fonk.select_announcement_rowid(semesterName, courseID, head)

    def get_info_from_database(self):
        info = db_fonk.select_specific_announcement(self.ID)
        self.setDate(info[0])
        self.setHead(info[1])
        self.setAnnouncement(info[2])

    def edit_announcement(self, semesterName, courseID, head):
        self.get_rowid_from_database(semesterName, courseID, head)
        self.get_info_from_database()
        # Here system waits for user to make any change
        db_fonk.edit_announcement(self.ID, self.date, self.head, self.announcement)


    def get_all_announcement_in(self, semesterName, courseID):
        return db_fonk.select_all_announcement_in(semesterName, courseID)

    def delete_announcement(self, semesterName, courseID, head):
        self.get_rowid_from_database(semesterName, courseID, head)
        db_fonk.delete_announcement(self.ID)


class Subject:
    def __init__(self, semesterName, courseID, subject="Empty", reference="Empty", week="Empty"):
        self.subject = subject
        self.reference = reference
        self.week = week
        self.ID = None
        self.insertSubjectInDatabase(semesterName, courseID)

    def setSubject(self, subject):
        self.subject = subject

    def getSubject(self):
        return self.subject

    def setReference(self, reference):
        self.reference = reference

    def getReference(self):
        return self.reference

    def setWeek(self, week):
        self.week = week

    def getWeek(self):
        return self.week

    def getID(self):
        return self.ID

    # These functions are related with database
    def insertSubjectInDatabase(self, semesterName, courseID):
        self.ID = db_fonk.insert_subject(self.subject, self.reference, self.week)
        db_fonk.insert_sectionin(semesterName, courseID, self.ID)

    def get_rowid_from_database(self, semesterName, courseID, week):
        self.ID = db_fonk.select_subject_rowid(semesterName, courseID, week)

    def get_info_from_database(self):
        info = db_fonk.select_specific_subject(self.ID)
        self.setSubject(info[0])
        self.setReference(info[1])
        self.setWeek(info[2])

    def edit_subject(self):
        db_fonk.edit_subject(self.ID, self.subject, self.reference, self.week)

    def delete_subject(self):
        db_fonk.delete_subject(self.ID)

    def get_all_subject_in(self, semesterName, courseID):
        return db_fonk.select_all_subject_in(semesterName, courseID)
