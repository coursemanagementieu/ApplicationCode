from db_tables import *
from db_fonk import *
from semester_class import*
from course_class import*
from student_section import*


create_entity_tables()
create_relation_tables()

semester = Semester()
course = Course()
section = Section()
announcement = Announcement()
subject = Subject()
# course_evaluation = Grade()
# student = Student()
# note = Note()

page = ("1-) Insert\n"
        "2-) Edit\n" 
        "3-) Find\n"
        "4-) Delete\n"
        "5-) View all\n")


def semester_management():
    secim = int(input(page))
    if secim is 1:
        name = input("Semester Name: ")
        semester.setSemesterName(name)
        week = input("Week number: ")
        semester.setSemesterWeek(week)
        semester.insertSemesterIntoDatabase()
    elif secim is 2:
        info = semester.get_all_semester()
        for cell in info:
            semester.setSemesterName(cell[0])
            semester.get_info_from_database()
            print(semester.getSemesterName())
        name = input("Birini sec")
        semester.setSemesterName(name)
        semester.get_info_from_database()
        print("Su anda : ",semester.getSemesterName(), semester.getSemesterWeek())
        week = input("Yeni week: ")
        semester.setSemesterWeek(week)
        semester.edit_semester()
        semester.get_info_from_database()
        print("Yenisi : ", semester.getSemesterName(), semester.getSemesterWeek())
    elif secim is 3:
        info = semester.get_all_semester()
        for cell in info:
            semester.setSemesterName(cell[0])
            semester.get_info_from_database()
            print(semester.getSemesterName())
        name = input("Birini sec: ")
        semester.setSemesterName(name)
        semester.get_info_from_database()
        print("Su anda : ", semester.getSemesterName(), semester.getSemesterWeek())
    elif secim is 4:
        info = semester.get_all_semester()
        for cell in info:
            semester.setSemesterName(cell[0])
            semester.get_info_from_database()
            print(semester.getSemesterName())
        name = input("Birini sec: ")
        semester.setSemesterName(name)
        semester.delete_semester()
    elif secim is 5:
        info = semester.get_all_semester()
        for cell in info:
            semester.setSemesterName(cell[0])
            semester.get_info_from_database()
            print(semester.getSemesterName())


def course_management():
    secim = int(input(page))
    if secim is 1:
        name = input("Course Name: ")
        course.setCourseName(name)
        code = input("Course code: ")
        course.setCourseCode(code)
        book = input("Course book: ")
        course.setCourseBook(book)
        refbook = input("Course reference book: ")
        course.setRefBookName(refbook)
        syllabusLink = input("Course syllabus link: ")
        course.setCourseSyllabus(syllabusLink)
        course.insertCourseInDatabase(semester.getSemesterName())
    elif secim is 2:
        info = course.get_all_course_in(semester.getSemesterName())
        for cell in info:
            course.setCourseID(cell[0])
            course.get_info_from_database()
            print(course.getCourseCode())
        code = input("Birini sec")
        course.setCourseCode(code)
        course.get_rowid_from_database(semester.getSemesterName())
        print("Su anda : ", course.getCourseName(), course.getCourseCode(), course.getCourseBook(),
              course.getRefBookName(), course.getSyllabus())
        name = input("Course Name: ")
        course.setCourseName(name)
        code = input("Course code: ")
        course.setCourseCode(code)
        book = input("Course book: ")
        course.setCourseBook(book)
        refbook = input("Course reference book: ")
        course.setRefBookName(refbook)
        syllabusLink = input("Course syllabus link: ")
        course.setCourseSyllabus(syllabusLink)
        course.edit_course()
        course.get_info_from_database()
        print("Yenisi : ", course.getCourseName(), course.getCourseCode(), course.getCourseBook(),
              course.getRefBookName(), course.getSyllabus())
    elif secim is 3:
        info = course.get_all_course_in(semester.getSemesterName())
        for cell in info:
            course.setCourseID(cell[0])
            course.get_info_from_database()
            print(course.getCourseCode())
        code = input("Birini sec: ")
        course.setCourseCode(code)
        course.get_rowid_from_database(semester.getSemesterName())
        course.get_info_from_database()
        print("Name : ", course.getCourseName())
        print("Code : ", course.getCourseCode())
        print("Book : ", course.getCourseBook())
        print("Reference book : ", course.getRefBookName())
        print("Syllabus link : ", course.getSyllabus())
    elif secim is 4:
        info = course.get_all_course_in(semester.getSemesterName())
        for cell in info:
            course.setCourseID(cell[0])
            course.get_info_from_database()
            print(course.getCourseCode())
        code = input("Birini sec: ")
        course.setCourseCode(code)
        course.get_rowid_from_database(semester.getSemesterName())
        course.delete_course(semester.getSemesterName())
    elif secim is 5:
        info = course.get_all_course_in(semester.getSemesterName())
        for cell in info:
            course.setCourseID(cell[0])
            course.get_info_from_database()
            print(course.getCourseCode())

def section_management():
    secim =  int(input(page))
    if secim is 1:
        name = input("Name: ")
        section.setSectionName(name)
        classrom = input("Classroom: ")
        section.setClassRoom(classrom)
        hour = input("Hour: ")
        section.setHour(hour)
        day = input("Day: ")
        section.setDay(day)
        section.insertSectionInDatabase(semester.getSemesterName(), course.get_courseID())
    elif secim is 2:
        info = section.get_all_section_in(semester.getSemesterName(), course.get_courseID())
        for cell in info:
            section.setSectionID(cell[0])
            section.get_info_from_database()
            print(section.getSectionName())
        name = input("Sec birini: ")
        section.setSectionName(name)
        section.get_rowid_from_database(semester.getSemesterName(), course.get_courseID())
        name = input("Name: ")
        section.setSectionName(name)
        classrom = input("Classroom: ")
        section.setClassRoom(classrom)
        hour = input("Hour: ")
        section.setHour(hour)
        day = input("Day: ")
        section.setDay(day)
        section.edit_section()
    elif secim is 3:
        info = section.get_all_section_in(semester.getSemesterName(), course.get_courseID())
        for cell in info:
            section.setSectionID(cell[0])
            section.get_info_from_database()
            print(section.getSectionName())
        name = input("Sec birini: ")
        section.setSectionName(name)
        section.get_rowid_from_database(semester.getSemesterName(), course.get_courseID())
        section.get_info_from_database()
        print("Name: ", section.getSectionName())
        print("Classroom: ", section.getClassRoom())
        print("Hour: ", section.getHour())
        print("Day: ", section.getDay())
    elif secim is 4:
        info = section.get_all_section_in(semester.getSemesterName(), course.get_courseID())
        for cell in info:
            section.setSectionID(cell[0])
            section.get_info_from_database()
            print(section.getSectionName())
        name = input("Sec birini: ")
        section.setSectionName(name)
        section.get_rowid_from_database(semester.getSemesterName(), course.get_courseID())
        section.delete_section()
    elif secim is 5:
        info = section.get_all_section_in(semester.getSemesterName(), course.get_courseID())
        for cell in info:
            section.setSectionID(cell[0])
            section.get_info_from_database()
            print(section.getSectionName())

def announcement_management():
    secim = int(input(page))
    if secim is 1:
        date = input("Enter date: ")
        announcement.setDate(date)
        head = input("Enter head: ")
        announcement.setHead(head)
        ann = input("Enter announcement: ")
        announcement.setAnnouncement(ann)
        announcement.insertAnnouncementInDatabase(semester.getSemesterName(), course.get_courseID())
    elif secim is 2:
        info = announcement.get_all_announcement_in(semester.getSemesterName(), course.get_courseID())
        for cell in info:
            announcement.setID(cell[0])
            announcement.get_info_from_database()
            print(announcement.getHead())
        head = input("Sec birini: ")
        announcement.setHead(head)
        announcement.get_rowid_from_database(semester.getSemesterName(), course.get_courseID())
        date = input("Enter date: ")
        announcement.setDate(date)
        head = input("Enter head: ")
        announcement.setHead(head)
        ann = input("Enter announcement: ")
        announcement.setAnnouncement(ann)
        announcement.edit_announcement()
    elif secim is 3:
        info = announcement.get_all_announcement_in(semester.getSemesterName(), course.get_courseID())
        for cell in info:
            announcement.setID(cell[0])
            announcement.get_info_from_database()
            print(announcement.getHead())
        head = input("Sec birini: ")
        announcement.setHead(head)
        announcement.get_rowid_from_database(semester.getSemesterName(), course.get_courseID())
        announcement.get_info_from_database()
        print("Date: ", announcement.getDate())
        print("Head: ", announcement.getHead())
        print("Announcement", announcement.getAnnouncement())
    elif secim is 4:
        info = announcement.get_all_announcement_in(semester.getSemesterName(), course.get_courseID())
        for cell in info:
            announcement.setID(cell[0])
            announcement.get_info_from_database()
            print(announcement.getHead())
        head = input("Sec birini: ")
        announcement.setHead(head)
        announcement.get_rowid_from_database(semester.getSemesterName(), course.get_courseID())
        announcement.delete_announcement()
    elif secim is 5:
        info = announcement.get_all_announcement_in(semester.getSemesterName(), course.get_courseID())
        for cell in info:
            announcement.setID(cell[0])
            announcement.get_info_from_database()
            print(announcement.getHead())

def subject_management():
    secim = int(input(page))
    if secim is 1:
        sub = input("Subject: ")
        subject.setSubject(sub)
        ref = input("Reference: ")
        subject.setReference(ref)
        w = input("Week: ")
        subject.setWeek(w)
        subject.insertSubjectInDatabase(semester.getSemesterName(), course.get_courseID())
    elif secim is 2:
        info = subject.get_all_subject_in(semester.getSemesterName(), course.get_courseID())
        for cell in info:
            subject.setID(cell[0])
            subject.get_info_from_database()
            print("Week: ", subject.getWeek())
        week = input("Sec birini: ")
        subject.setWeek(week)
        subject.get_rowid_from_database(semester.getSemesterName(), course.get_courseID())
        sub = input("Subject: ")
        subject.setSubject(sub)
        ref = input("Reference: ")
        subject.setReference(ref)
        w = input("Week: ")
        subject.setWeek(w)
        subject.edit_subject()
    elif secim is 3:
        info = subject.get_all_subject_in(semester.getSemesterName(), course.get_courseID())
        for cell in info:
            subject.setID(cell[0])
            subject.get_info_from_database()
            print("Week: ", subject.getWeek())
        week = input("Sec birini: ")
        subject.setWeek(week)
        subject.get_rowid_from_database(semester.getSemesterName(), course.get_courseID())
        subject.get_info_from_database()
        print("Subject: ", subject.getSubject())
        print("Reference: ", subject.getReference())
        print("Week: ", subject.getWeek())
    elif secim is 4:
        info = subject.get_all_subject_in(semester.getSemesterName(), course.get_courseID())
        for cell in info:
            subject.setID(cell[0])
            subject.get_info_from_database()
            print("Week: ", subject.getWeek())
        week = input("Sec birini: ")
        subject.setWeek(week)
        subject.get_rowid_from_database(semester.getSemesterName(), course.get_courseID())
        subject.delete_subject()
    elif secim is 5:
        info = subject.get_all_subject_in(semester.getSemesterName(), course.get_courseID())
        for cell in info:
            subject.setID(cell[0])
            subject.get_info_from_database()
            print("Subject: ", subject.getSubject())
            print("Reference: ", subject.getReference())
            print("Week: ", subject.getWeek())


# def course_grade_management:
#
# def student_management()
#
# def note_management:

while True:
    karar = int(input("Islem belirt\n"
            "1-) Semester gir\n"
            "2-) Course gir\n"
            "3-) Section gir\n"
            "4-) Announcement gir\n"
            "5-) Subject gir\n"
            "6-) Course grade gir\n"
            "7-) Student gir\n"
            "8-) Student icin not al\n"))
    if karar is 1:
        semester_management()
    elif karar is 2:
        semester.setSemesterName("201401")
        course_management()
    elif karar is 3:
        semester.setSemesterName("201401")
        course.setCourseID("1")
        section_management()
    elif karar is 4:
        semester.setSemesterName("201401")
        course.setCourseID("1")
        announcement_management()
    elif karar is 5:
        semester.setSemesterName("201401")
        course.setCourseID("1")
        subject_management()
    # elif karar is 6:
    #     course_grade_management()
    # elif karar is 7:
    #     student_management()
    # elif karar is 8:
    #     note_management()
