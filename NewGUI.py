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

def get_all_semester_name():
    info = semester.get_all_semester()
    for cell in info:
        semester.setSemesterName(cell[0])
        semester.get_info_from_database()
        Sem = tree.insert('', 'end', 0, text='' + semester.getSemesterName())
def get_all_course():
    info = course.get_all_course_in(semester.getSemesterName())
    for cell in info:
        course.setCourseID(cell[0])
        course.get_info_from_database()
        Course = tree.insert(Sem, 'end', text='Course',tags=('course'))

def SemesterListInsert():
    global Sem

    Sem = tree.insert('', 'end', 0, text=''+SemNameEntry.get())
    Course = tree.insert(Sem, 'end', text='Course',tags=('course'))
    tree.tag_bind('course','<Double-1>',CallCreateNewCourse)
    tree.insert(Course, 'end', text='Announcements')
    tree.insert(Course, 'end', text='Grades')
    tree.insert(Course, 'end', text='Section')


    SemesterInfo()


def CallCreateNewSemester():

   global SemNameEntry,WeekEntry
   CreateSemesterWindow()


   SemNameLabel = ttk.Label(CreateSemWindow,text ="*Semester Name : ",font='Arial')
   SemNameLabel.pack(padx=250,pady=20)

   SemNameEntry=ttk.Entry(CreateSemWindow)
   SemNameEntry.pack(padx=250,pady=20)

   WeekLabel = ttk.Label(CreateSemWindow,text ="*Week :" ,font='Arial')
   WeekLabel.pack(padx=250,pady=20)

   WeekEntry=ttk.Entry(CreateSemWindow)
   WeekEntry.pack(padx=250,pady=20)

   AddNewSmesterBttn()
   AddNewSemesterButton.pack(side=BOTTOM,padx=250,pady=40)

   get_all_course()




def SemesterInfo():
    semester.setSemesterName(SemNameEntry.get())
    semester.setSemesterWeek(WeekEntry.get())
    semester.insertSemesterIntoDatabase()

    SemesterNameLabel = ttk.Label(SecondFrame,text=" "+semester.getSemesterName())
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
    global  CreateCoursewindow
    CreateCoursewindow= Toplevel(width=450, height=580, bg='white')
def AddingCourseFunc():
    CourseListInsert()
    CreateCoursewindow.destroy()

def CourseListInsert():
    CourseList.insert(0, "" +CoCodeEntry.get())
    CourseInfo()

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


def CourseInfo():

    course.setCourseName(CoNameEntry.get())
    course.setCourseCode(CoCodeEntry.get())
    course.setCourseBook(CoBookEntry.get())
    course.setRefBookName(CoRefBookEntry.get())
    course.setCourseSyllabus(SyllabusEntry.get())

    semester.get_info_from_database()
    course.insertCourseInDatabase(semester.getSemesterName())
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



CourseList = Listbox()
SemesterList = Listbox()
tree = ttk.Treeview(FirstFrame)
tree.place(x=0,y=0,width= 500,height=y*3)


tree.bind("<Double-1>", OnDoubleClick)


get_all_semester_name()
app= FullScreenApp(root)
root.config(menu=menubar)
root.resizable(0,0)
root.mainloop()

