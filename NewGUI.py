from tkinter import *
from tkinter import ttk
from student_section import *
from semester_class import *
from course_class import *
from db_fonk import *
from db_tables import *

root= Tk()
menubar = Menu(root)
s = ttk.Style()
s.theme_names()
('aqua', 'step', 'clam', 'alt', 'default', 'classic','vista')
s.theme_use('vista')
x = root.winfo_screenwidth()/5
y = root.winfo_screenheight()/3

semester = Semester()
course = Course()
section = Section()
announcement = Announcement()
subject = Subject()
grade = Grade()
student = Student()
note = Note()
global Sem

def get_all_semester_name():
    global Sem
    info = semester.get_all_semester()
    for cell in info:
        semester.setSemesterName(cell[0])
        semester.get_info_from_database()
        Sem = tree.insert('', 'end', 0, text='' + semester.getSemesterName(),tag=('semester'))  # tag eklendi
        get_all_course()
def get_all_course():
    global Course
    info = course.get_all_course_in(semester.getSemesterName())
    for cell in info:
        course.setCourseID(cell[0])
        course.get_info_from_database()
        Course = tree.insert(Sem, "end", text='' + course.getCourseCode(),tag=('course'))
        get_all_section()
        get_all_announcement()
        get_all_grade()
def get_all_section():
    global Section
    info = section.get_all_section_in(semester.getSemesterName(), course.get_courseID())
    for cell in info:
        section.setSectionID(cell[0])
        section.get_info_from_database()
        Section = tree.insert(Course, "end", text = section.getSectionName(), tag=('section'))
        # get_all_student()
def get_all_announcement():
    info = announcement.get_all_announcement_in(semester.getSemesterName(), course.get_courseID)
    for cell in info:
        announcement.setID(cell[0])
        announcement.get_info_from_database()
        tree.insert(Course, "end", text = announcement.getHead(), tag = ('announcement'))
def get_all_grade():
    info = grade.get_all_evaluation_in(semester.getSemesterName(), course.get_courseID)
    for cell in info:
        grade.setID(cell[0])
        grade.get_info_from_database()
        tree.insert(Course, "end", text = grade.getGradeName(), tag = ('grade'))

# def get_all_student():
# def get_all_note():

#-----------------FULLSCREEN-----------------------------
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        padx=0
        pady=95
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-padx, master.winfo_screenheight()-pady))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
#--------------------------------------------------------


#--------------------FIRST_FRAME--------------------------
FirstFrame = Frame(root,width=x, height=y*3, bg='white')
FirstFrame.propagate(0)
FirstFrame.pack(expand=0,side=LEFT)

#---------------------------------------------------------

#---------------------SECOND_FRAME------------------------
SecondFrame = Frame(root,width=x*2, height=y*3, bg='gray91')
SecondFrame.propagate(0)
SecondFrame.place(x=x,y=0)






#---------------------------------------------------------

#---------------------THIRD_FRAME-------------------------

#---------------------------------------------------------

#---------------------SEMESTER_FUNCTIONS------------------
def CreateSemesterWindow():
    global CreateSemWindow
    CreateSemWindow = Toplevel(width = 450,height= 580,bg='white')


def AddNewSmesterBttn():
    global AddNewSemesterButton
    AddNewSemesterButton = ttk.Button(CreateSemWindow,text= 'Add Semester',command=CheckSemEntrys)


def CheckSemEntrys():
    if len(SemNameEntry.get()) != 0 and len(WeekEntry.get()) !=0 :
        AddingSemFunc()


def AddingSemFunc():
    SemesterListInsert()
    tree.place(width= x,height=y*3)
    CreateSemWindow.destroy()

def SemesterListInsert():
    tree.insert('', 'end', 0, text=SemNameEntry.get(),tag=('semester'))  # tag eklendi
    # Course = tree.insert(Sem, 'end',text='Course',tag=('course'))
    # tree.tag_bind('course','<Double-1>',CallCreateNewCourse)
    # tree.insert(Course, 'end', text='Announcements')
    # tree.insert(Course, 'end', text='Grades')
    # tree.insert(Course, 'end', text='Section')
    AddSemester()


def CallCreateNewSemester():

   global SemNameEntry,WeekEntry
   CreateSemesterWindow()


   SemNameLabel = ttk.Label(CreateSemWindow,text ="*Semester Name : ",font='Arial')
   SemNameLabel.pack(padx=250,pady=20)

   SemNameEntry=ttk.Entry(CreateSemWindow)
   SemNameEntry.pack(padx=250,pady=20)

   WeekLabel = ttk.Label(CreateSemWindow,text ="Week :" ,font='Arial')
   WeekLabel.pack(padx=250,pady=20)

   WeekEntry=ttk.Entry(CreateSemWindow)
   WeekEntry.pack(padx=250,pady=20)

   AddNewSmesterBttn()
   AddNewSemesterButton.pack(side=BOTTOM,padx=250,pady=40)


def AddSemester():
    semester.setSemesterName(SemNameEntry.get())
    semester.setSemesterWeek(WeekEntry.get())
    semester.insertSemesterIntoDatabase()


def SemesterInfo():
    SemesterNameLabel = ttk.Label(SecondFrame,text=semester.getSemesterName())
    SemesterNameLabel.config(font=("Calibri", 55),background = 'light sky blue')
    SemesterNameLabel.place(x=0,y=0,height=150,width = 1000)
    SemesterWeekLabel = ttk.Label(SecondFrame,text=" Week Number :  "+semester.getSemesterWeek())
    SemesterWeekLabel.place(x=0,y=150,height = 100 ,width = 900)
    SemesterWeekLabel.config(font=("Arial"))





#------------------------------------------------------------


#-------------------COURSE_FUNCTIONS-------------------------

def AddNewCourseBttn():
    global AddNewCourseButton
    AddNewCourseButton = ttk.Button(CreateCoursewindow,text= 'Add Course',command=CheckCourseEntrys)

def CheckCourseEntrys():
    if len(CoNameEntry.get()) != 0 and len(CoCodeEntry.get()) !=0 and len(CoBookEntry.get()) !=0 and len(CoRefBookEntry.get()) !=0 and len(SyllabusEntry.get()) !=0 :
        AddingCourseFunc()

def CreateCourseWindow():
    global CreateCoursewindow
    CreateCoursewindow= Toplevel(width=450, height=580, bg='white')


def AddingCourseFunc():
    CourseListInsert()
    CreateCoursewindow.destroy()

def CourseListInsert():
    tree.insert(Sem, 'end', text='' + CoCodeEntry.get(), tag=('course'))
    AddCourse()

def CallCreateNewCourse(event):

   global CoCodeEntry,CoBookEntry,CoNameEntry,CoRefBookEntry,SyllabusEntry

   CreateCourseWindow()

   CoNameLabel = ttk.Label(CreateCoursewindow, text ="*Course Name :")
   CoNameLabel.pack(padx=350,pady=20)

   CoNameEntry=ttk.Entry(CreateCoursewindow)
   CoNameEntry.pack(padx=350,pady=20)

   CoCodeLabel = ttk.Label(CreateCoursewindow, text ="*Course Code :")
   CoCodeLabel .pack(padx=350,pady=20)

   CoCodeEntry=ttk.Entry(CreateCoursewindow)
   CoCodeEntry.pack(padx=350,pady=20)

   CoBookLabel = ttk.Label(CreateCoursewindow, text ="*Course Book :")
   CoBookLabel.pack(padx=350,pady=20)

   CoBookEntry=ttk.Entry(CreateCoursewindow)
   CoBookEntry.pack(padx=350,pady=20)

   CoRefBookLabel = ttk.Label(CreateCoursewindow, text ="*Course Reference Book :")
   CoRefBookLabel.pack(padx=350,pady=20)

   CoRefBookEntry=ttk.Entry(CreateCoursewindow)
   CoRefBookEntry.pack(padx=350,pady=20)

   SyllabusLabel = ttk.Label(CreateCoursewindow, text ="*Syllabus :")
   SyllabusLabel.pack(padx=350,pady=20)

   SyllabusEntry=ttk.Entry(CreateCoursewindow)
   SyllabusEntry.pack(padx=350,pady=20)

   AddNewCourseBttn()
   AddNewCourseButton.pack(side=BOTTOM,padx=350,pady=40)


def AddCourse():

    course.setCourseName(CoNameEntry.get())
    course.setCourseCode(CoCodeEntry.get())
    course.setCourseBook(CoBookEntry.get())
    course.setRefBookName(CoRefBookEntry.get())
    course.setCourseSyllabus(SyllabusEntry.get())

    #semester.get_info_from_database()
    course.insertCourseInDatabase(semester.getSemesterName())


def CourseInfo():
    CourseNameLabel = ttk.Label(SecondFrame,text=" "+course.getCourseName())
    CourseNameLabel.config(font=("Courier", 45),background = 'lightblue')
    CourseNameLabel.place(x=0,y=250,height=100,width = 900)

    CourseCodeLabel = ttk.Label(SecondFrame,text="Course Code :  "+course.getCourseCode())
    CourseCodeLabel.place(x=0,y=350,height = 50 ,width = 900)
    CourseCodeLabel.config()

    CourseBookLabel = ttk.Label(SecondFrame,text="Course Book :  "+course.getCourseBook())
    CourseBookLabel.place(x=0,y=400,height = 50 ,width = 900)
    CourseBookLabel.config()

    CourseRefBookLabel = ttk.Label(SecondFrame,text="Course Referance Book :  "+course.getRefBookName())
    CourseRefBookLabel.place(x=0,y=450,height = 50 ,width = 900)
    CourseRefBookLabel.config()

    SyllabusLabel = ttk.Label(SecondFrame,text="Syllabus :  "+course.getSyllabus())
    SyllabusLabel.place(x=0,y=500,height = 50 ,width = 900)
    SyllabusLabel.config()


#------------------------------------------------------------


#-------------------SECTION_FUNCTION-------------------------

def AddNewSectionBttn():
    global AddNewSectionButton
    AddNewSectionButton = ttk.Button(CreateSectionwindow,text= 'Add Section',command=CheckSectionEntrys)

def CheckSectionEntrys():
    if len(SecNameEntry.get()) != 0 and len(SecClaEntry.get()) !=0 and len(SecHourEntry.get()) !=0 and len(SecDayEntry.get()) !=0:
        AddingSectionFunc()

def CreateSectionWindow():
    global CreateSectionwindow
    CreateSectionwindow= Toplevel(width=450, height=580, bg='white')


def AddingSectionFunc():
    SectionListInsert()
    CreateSectionwindow.destroy()

def SectionListInsert():
    tree.insert(Course, 'end', text='' + SecClaEntry.get(), tag=('section'))
    AddSection()

def CallCreateNewSection(event):

   global SecClaEntry,SecHourEntry,SecNameEntry,SecDayEntry

   CreateSectionWindow()

   SecNameLabel = ttk.Label(CreateSectionwindow, text ="*Section Name :")
   SecNameLabel.pack(padx=350,pady=20)

   SecNameEntry=ttk.Entry(CreateSectionwindow)
   SecNameEntry.pack(padx=350,pady=20)

   SecClaLabel = ttk.Label(CreateSectionwindow, text ="*Section Class :")
   SecClaLabel .pack(padx=350,pady=20)

   SecClaEntry=ttk.Entry(CreateSectionwindow)
   SecClaEntry.pack(padx=350,pady=20)

   SecHourLabel = ttk.Label(CreateSectionwindow, text ="*Section Hour :")
   SecHourLabel.pack(padx=350,pady=20)

   SecHourEntry=ttk.Entry(CreateSectionwindow)
   SecHourEntry.pack(padx=350,pady=20)

   SecDayBookLabel = ttk.Label(CreateSectionwindow, text ="*Section Day :")
   SecDayBookLabel.pack(padx=350,pady=20)

   SecDayEntry=ttk.Entry(CreateSectionwindow)
   SecDayEntry.pack(padx=350,pady=20)

   AddNewSectionBttn()
   AddNewSectionButton.pack(side=BOTTOM,padx=350,pady=40)


def AddSection():

    section.setSectionName(SecNameEntry.get())
    section.setClassRoom(SecClaEntry.get())
    section.setHour(SecHourEntry.get())
    section.setDay(SecDayEntry.get())

    #semester.get_info_from_database()
    section.insertSectionInDatabase(semester.getSemesterName(), course.get_courseID)


def SectionInfo():
    SectionNameLabel = ttk.Label(SecondFrame,text="Section Name :  " + section.getSectionName())
    SectionNameLabel.config(font=("Courier", 45),background = 'lightblue')
    SectionNameLabel.place(x=0,y=250,height=100,width = 900)

    SectionClassLabel = ttk.Label(SecondFrame,text="Section Class :  " + section.getClassRoom())
    SectionClassLabel.place(x=0,y=350,height = 50 ,width = 900)
    SectionClassLabel.config()

    SectionHourLabel = ttk.Label(SecondFrame,text="Section Hour :  "+section.getHour())
    SectionHourLabel.place(x=0,y=400,height = 50 ,width = 900)
    SectionHourLabel.config()

    SectionDayLabel = ttk.Label(SecondFrame,text="Section Day :  " + section.getDay())
    SectionDayLabel.place(x=0,y=450,height = 50 ,width = 900)
    SectionDayLabel.config()





#------------------------------------------------------------



#------------MAIN----------------------------



#-----------------MENU-----------------------------------
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Create a New Semester",command=CallCreateNewSemester)
filemenu.add_command(label="Create a New Course",command=CallCreateNewCourse,state ='disabled')
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About")
menubar.add_cascade(label="Help", menu=helpmenu)
#---------------------------------------------------------
def OnDoubleClick(event):
        item = tree.selection()[0]
        print("you clicked on", tree.item(item,"text"))
        if tree.tag_has("semester",item):
            print("Yes semester!!")
            semester.setSemesterName(tree.item(item,"text"))
            semester.get_info_from_database()
            SemesterInfo()
        elif tree.tag_has('course', item):
            print("Yess course!!")
            # Once dersin kodunu tanimlamaliyiz cunku 2. fonksyionda courseID yi bulmamız için ihtiyacımız olacak
            course.setCourseCode(tree.item(item, "text"))
            parent = tree.parent(item)
            semester.setSemesterName(tree.item(parent,"text"))
            course.get_rowid_from_database(semester.getSemesterName())
            course.get_info_from_database()
            CourseInfo()
        elif tree.tag_has('section', item):
            print("Yess section!")
            # Once section name i almamız gerekiyor, rowid icin gerekli
            section.setSectionName(tree.item(item,"text"))
            # Course a gider
            parent = tree.parent(item)
            course.setCourseCode(tree.item(parent,"text"))
            parent = tree.parent(item)
            semester.setSemesterName(tree.item(parent,"text"))
            course.get_rowid_from_database(semester.getSemesterName())
            section.get_rowid_from_database(semester.getSemesterName(), course.get_courseID())
            section.get_info_from_database()
            # do whatever want
        elif tree.tag_has('announcement', item):
            print("Yess announcement")
            announcement.setID(tree.item(item,"text"))
            # Course a gider
            parent = tree.parent(item)
            course.setCourseCode(tree.item(parent,"text"))
            parent = tree.parent(item)
            semester.setSemesterName(tree.item(parent,"text"))
            course.get_rowid_from_database(semester.getSemesterName())
            announcement.get_rowid_from_database(semester.getSemesterName(), course.get_courseID())
            announcement.get_info_from_database()
            # do what ever want
        elif tree.tag_has('grade', item):
            print("Yess grade")
            grade.setID(tree.item(item,"text"))
            # Course a gider
            parent = tree.parent(item)
            course.setCourseCode(tree.item(parent,"text"))
            parent = tree.parent(item)
            semester.setSemesterName(tree.item(parent,"text"))
            course.get_rowid_from_database(semester.getSemesterName())
            grade.get_rowid_from_database(semester.getSemesterName(), course.get_courseID())
            grade.get_info_from_database()
        elif tree.tag_has('student', item):
            print("Yeees student")
            student.setStudentId(tree.item(item,"text"))
            student.get_info_from_database()
        # elif tree.tag_has('note',item):
        #     print("Yeees note!")
        #     note.setHead(tree.item(item,"text"))
        # student grade kaldı


tree = ttk.Treeview(FirstFrame)
tree.place(x=0,y=0,width= 500,height=y*3)


tree.bind("<Double-1>", OnDoubleClick)


get_all_semester_name()
app= FullScreenApp(root)
root.config(menu=menubar)
root.resizable(0,0)
root.mainloop()