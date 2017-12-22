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
grade = Grade()
student = Student()
notee = Note()

page = ("1-) Insert\n"
        "2-) Edit\n" 
        "3-) Find\n"
        "4-) Delete\n"
        "5-) View all\n"
        "6-) Grade student")


def arrange(text):
    newtext = ""
    for i in text:
        if i is (text[len(text) - 1]):
            newtext = newtext + i
        else:
            newtext = newtext + i
            newtext = newtext + " "
    return newtext


def semester_management():
    secim = int(input(page))
    if secim is 1:
        name = arrange((input("Semester Name: ").split()))
        semester.setSemesterName(name)
        week = arrange(input("Week number: ").split())  # Here may be we can take integer from user
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
        print("ID: ", section.getSectionID())
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


def course_grade_management():
    secim = int(input(page))
    if secim is 1:
        name = input("Grade name: ")
        grade.setGradeName(name)
        percentage = input("Percentage: ")
        grade.setPercentage(percentage)
        grade.insertGradeInDB(semester.getSemesterName(), course.get_courseID())
    elif secim is 2:
        info = grade.gel_all_evaluation_in(semester.getSemesterName(), course.get_courseID())
        for cell in info:
            grade.setID(cell[0])
            grade.get_info_from_database()
            print("Name: ", grade.getGradeName())
            print("Percentage: ", grade.getPercentage())
        name = input("Sec birini")
        grade.setGradeName(name)
        grade.get_rowid_from_database(semester.getSemesterName(), course.get_courseID())
        name = input("Grade name: ")
        grade.setGradeName(name)
        percentage = input("Percentage: ")
        grade.setPercentage(percentage)
        grade.edit_evaluation()
    elif secim is 3:
        info = grade.gel_all_evaluation_in(semester.getSemesterName(), course.get_courseID())
        for cell in info:
            grade.setID(cell[0])
            grade.get_info_from_database()
            print("Name: ", grade.getGradeName())
            print("Percentage: ", grade.getPercentage())
    elif secim is 4:
        info = grade.gel_all_evaluation_in(semester.getSemesterName(), course.get_courseID())
        for cell in info:
            grade.setID(cell[0])
            grade.get_info_from_database()
            print("Name: ", grade.getGradeName())
            print("Percentage: ", grade.getPercentage())
        name = input("Sec birini")
        grade.setGradeName(name)
        grade.get_rowid_from_database(semester.getSemesterName(), course.get_courseID())
        grade.delete_evaluation()
    elif secim is 5:
        info = grade.gel_all_evaluation_in(semester.getSemesterName(), course.get_courseID())
        for cell in info:
            grade.setID(cell[0])
            grade.get_info_from_database()
            print("ID: ", grade.get_ID())
            print("Name: ", grade.getGradeName())
            print("Percentage: ", grade.getPercentage())

def student_management():
    secim = int(input(page))
    if secim is 1:
        name = input("Name: ")
        student.setStudentName(name)
        id = input("ID: ")
        student.setStudentId(id)
        student.insertStudentInDatabase(semester.getSemesterName(), course.get_courseID(), section.getSectionID())
    elif secim is 2:
        info = student.get_all_student_in(semester.getSemesterName(), course.get_courseID(), section.getSectionID())
        for cell in info:
            student.setStudentId(cell[0])
            student.get_info_from_database()
            print("Name: ", student.getStudentName())
            print("ID: ", student.getStudentId())
        id = input("Sec birini: ")
        student.setStudentId(id)
        name = input("Name: ")
        student.setStudentName(name)
        student.edit_student()
    elif secim is 3:
        info = student.get_all_student_in(semester.getSemesterName(), course.get_courseID(), section.getSectionID())
        for cell in info:
            student.setStudentId(cell[0])
            student.get_info_from_database()
            print("Name: ", student.getStudentName())
            print("ID: ", student.getStudentId())
        id = input("Sec birini: ")
        student.setStudentId(id)
        student.get_info_from_database()
        print("Name: ", student.getStudentName())
        print("ID: ", student.getStudentId())

    elif secim is 4:
        info = student.get_all_student_in(semester.getSemesterName(), course.get_courseID(), section.getSectionID())
        for cell in info:
            student.setStudentId(cell[0])
            student.get_info_from_database()
            print("Name: ", student.getStudentName())
            print("ID: ", student.getStudentId())
        id = input("Sec birini: ")
        student.setStudentId(id)
        student.delete_student()
    elif secim is 5:
        info = student.get_all_student_in(semester.getSemesterName(), course.get_courseID(), section.getSectionID())
        for cell in info:
            student.setStudentId(cell[0])
            student.get_info_from_database()
            print("Name: ", student.getStudentName())
            print("ID: ", student.getStudentId())
    elif secim is 6:
        student.setStudentId("2014010101")
        sec = int(input("1-) Insert\n"
                    "2-) Edit\n"
                    "3-) View\n"))
        if sec is 1:
            stugra = int(input("Grade: "))
            student.setStudentGrade(stugra)
            student.insert_student_grade_in_database(semester.getSemesterName(),
                                                     course.get_courseID(), grade.get_ID())
        elif sec is 2:
            stugra = input("Grade: ")
            student.setStudentGrade(stugra)
            student.edit_student_evaluation(semester.getSemesterName(),
                                                     course.get_courseID(), grade.get_ID())
        elif sec is 3:
            student.get_student_evaluation_info_from_database(semester.getSemesterName(),
                                                     course.get_courseID(), grade.get_ID())
            print("Name: ", student.getStudentName())
            print("ID: ", student.getStudentId())
            grade.get_info_from_database()
            print("Evoluation name: ", grade.getGradeName())
            print("Percentage: ", grade.getPercentage())
            print("Grade: ", student.getStudentGrade())

def note_management():
    secim = int(input(page))
    if secim is 1:
        head = input("Head: ")
        notee.setHead(head)
        note = input("Note: ")
        notee.setNote(note)
        date = input("Date: ")
        notee.setDate(date)
        notee.insertNoteInDatabase(semester.getSemesterName(), course.get_courseID(),
                                   student.getStudentId())
    elif secim is 2:
        info = notee.get_all_note_in(semester.getSemesterName(), course.get_courseID(),
                                   student.getStudentId())
        for cell in info:
            notee.setID(cell[0])
            notee.get_info_from_database()
            print("Head: ", notee.getHead())
            print("Note", notee.getHead())
            print("Date: ", notee.getDate())
        head = input("Sec birini")
        notee.setHead(head)
        notee.get_rowid_from_database(semester.getSemesterName(), course.get_courseID(),
                                   student.getStudentId())
        head = input("Head: ")
        notee.setHead(head)
        note = input("Note: ")
        notee.setNote(note)
        date = input("Date: ")
        notee.setDate(date)
        notee.edit_note()

    elif secim is 3:
        info = notee.get_all_note_in(semester.getSemesterName(), course.get_courseID(),
                                   student.getStudentId())
        for cell in info:
            notee.setID(cell[0])
            notee.get_info_from_database()
            print("Head: ", notee.getHead())
            print("Note", notee.getHead())
            print("Date: ", notee.getDate())
        head = input("Sec birini")
        notee.setHead(head)
        notee.get_rowid_from_database(semester.getSemesterName(), course.get_courseID(),
                                   student.getStudentId())
        print("Head: ", notee.getHead())
        print("Note", notee.getHead())
        print("Date: ", notee.getDate())

    elif secim is 4:
        info = notee.get_all_note_in(semester.getSemesterName(), course.get_courseID(),
                                   student.getStudentId())
        for cell in info:
            notee.setID(cell[0])
            notee.get_info_from_database()
            print("Head: ", notee.getHead())
            print("Note", notee.getHead())
            print("Date: ", notee.getDate())
        head = input("Sec birini")
        notee.setHead(head)
        notee.get_rowid_from_database(semester.getSemesterName(), course.get_courseID(),
                                   student.getStudentId())
        notee.delete_note()
    elif secim is 5:
        info = notee.get_all_note_in(semester.getSemesterName(), course.get_courseID(),
                                   student.getStudentId())
        for cell in info:
            notee.setID(cell[0])
            notee.get_info_from_database()
            print("Head: ", notee.getHead())
            print("Note", notee.getNote())
            print("Date: ", notee.getDate())


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
    elif karar is 6:
        semester.setSemesterName("201401")
        course.setCourseID("1")
        course_grade_management()
    elif karar is 7:
        semester.setSemesterName("201401")
        course.setCourseID("1")
        section.setSectionID("2")
        grade.setID("1")
        student_management()
    elif karar is 8:
        semester.setSemesterName("201401")
        course.setCourseID("1")
        section.setSectionID("2")
        student.setStudentId("2014010101")
        note_management()
