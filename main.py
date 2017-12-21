from db_tables import *
from db_fonk import *
from semester_class import*
from course_class import*
from student_section import*


create_entity_tables()
create_relation_tables()

semester = Semester()
course = Course()
# section = Section("Default")
# announcement = Announcement()
# subject = Subject()
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
            course.get_rowid_from_database(semester.getSemesterName())
            print(course.getCourseCode())
        code = input("Birini sec: ")
        course.setCourseCode(code)
        course.get_rowid_from_database(semester.getSemesterName())
        semester.delete_semester()
    elif secim is 5:
        info = course.get_all_course_in(semester.getSemesterName())
        for cell in info:
            course.setCourseID(cell[0])
            course.get_rowid_from_database(semester.getSemesterName())
            print(course.getCourseCode())

# def section_management:
#
# def announcement_management:
#
# def subject_management:
#
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
    # elif karar is 3:
    #     section_management()
    # elif karar is 4:
    #     announcement_management()
    # elif karar is 5:
    #     subject_management()
    # elif karar is 6:
    #     course_grade_management()
    # elif karar is 7:
    #     student_management()
    # elif karar is 8:
    #     note_management()
