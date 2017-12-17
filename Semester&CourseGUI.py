# !/usr/bin/python3
from tkinter import *



root=Tk()
menubar = Menu(root)

#MainButtonFrame=Frame(width=650, height=250, bg='white')
#MainButtonFrame.pack_propagate(0)
#MainButtonFrame.pack(fill=BOTH, side= TOP)


TestFrame = Frame(width=300, height=500, bg='white')
TestFrame.pack_propagate(0)
TestFrame.pack(fill=BOTH,expand=TRUE)

TestFrame2 = Frame(width=300, height=500, bg='white')
TestFrame2.pack_propagate(0)
TestFrame2.pack(fill=BOTH,expand=TRUE)

FirstFrame = Frame(width=300, height=500, bg='white')

SecondFrame = Frame(width=300, height=500, bg='white')

HTMLFrame = Frame(width=450, height=50,bg='white')
HTMLFrame.pack_propagate(0)
HTMLFrame.pack(fill=BOTH,side= BOTTOM)

def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height,x, y))

def SemTlevelPos(width=300, height=200):
    # get screen width and height
    screen_width = CreateSemTlevel.winfo_screenwidth()
    screen_height = CreateSemTlevel.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    CreateSemTlevel.geometry('%dx%d+%d+%d' % (width, height,250,y))

def CourseTlevelPos(width=300, height=200):
    # get screen width and height
    screen_width = CreateCoTlevel.winfo_screenwidth()
    screen_height = CreateCoTlevel.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    CreateCoTlevel.geometry('%dx%d+%d+%d' % (width, height,x, y))
def setActive(self):
        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()

def Buttons():#MainButtons{
    global Semester,Course,HTMLButton

    Semester = Button(root, text='Add/Select a Semester',command = Semesters)
    #Course = Button(root,text='Course',command = Courses)

    HTMLButton = Button(root,text='HTML File')
    #}

def Activee(x):
    x.config(state='disabled')
def Diactive(x):
    x.config(state='normal')

#Semester Functions{
def CreateSemTlevell():
    global CreateSemTlevel
    CreateSemTlevel = Toplevel(width = 450,height= 580,bg='white')
def AddNewSmesterBttn():
    global AddNewSemesterButton
    AddNewSemesterButton = Button(CreateSemTlevel,text= 'Add Semester',command=AddingSemFunc)
def SemesterEntrys():
    global SemNameEntry,WeekEntry
    SemNameEntry=Entry(CreateSemTlevel)
    WeekEntry=Entry(CreateSemTlevel)
def AddingSemFunc():
    SemesterListInsert()
    SemesterList.place(relx=.1,rely=.25,height=250, width=200)
    CreateSemTlevel.destroy()
def SemesterListBox(x):
    global SemesterList
    SemesterList = Listbox(x)
def SemesterListInsert():
    SemesterList.insert(0, " "+ SemNameEntry.get())
# }

#Course Functions{
def CreateNewCoTlevell():
    global CreateCoTlevel
    CreateCoTlevel = Toplevel(width=450, height=580, bg='white')
def AddNewCourseBttn():
    global AddNewCourseButton
    AddNewCourseButton = Button(CreateCoTlevel,text= 'Add Course',command=AddingCourseFunc)
def CourseEntrys():
    global CoNameEntry,CoCodeEntry,CoBookEntry,CoRefBookEntry,SyllabusEntry
    CoNameEntry=Entry(CreateCoTlevel)
    CoCodeEntry=Entry(CreateCoTlevel)
    CoBookEntry=Entry(CreateCoTlevel)
    CoRefBookEntry=Entry(CreateCoTlevel)
    SyllabusEntry=Entry(CreateCoTlevel)
def CourseListBox():
    global CourseList
    CourseList = Listbox(CreateCoTlevel)
def AddingCourseFunc():
    CourseListInsert()
    CourseList.place(relx=.1,rely=.25,height=250, width=200)
    CreateCoTlevel.destroy()
def CourseListInsert():
    CourseList.insert(0, "" +CoCodeEntry.get())
#}

def CallCreateNewCourse():

   CreateNewCoTlevell()
   CreateCoTlevel.grab_set()
   CourseEntrys()

   CoNameLabel = Label(CreateCoTlevel, text ="*Course Name :")
   CoNameLabel.pack(padx=350,pady=20)

   CoNameEntry.pack(padx=350,pady=20)

   CoCodeLabel = Label(CreateCoTlevel, text ="*Course Code :")
   CoCodeLabel .pack(padx=350,pady=20)

   CoCodeEntry.pack(padx=350,pady=20)

   CoBookLabel = Label(CreateCoTlevel, text ="*Course Book :")
   CoBookLabel.pack(padx=350,pady=20)

   CoBookEntry.pack(padx=350,pady=20)

   CoRefBookLabel = Label(CreateCoTlevel, text ="*Course Reference Book :")
   CoRefBookLabel.pack(padx=350,pady=20)

   CoRefBookEntry.pack(padx=350,pady=20)

   SyllabusLabel = Label(CreateCoTlevel, text ="*Syllabus :")
   SyllabusLabel.pack(padx=350,pady=20)

   SyllabusEntry.pack(padx=350,pady=20)

   AddNewCourseBttn()
   AddNewCourseButton.pack(side=BOTTOM,padx=350,pady=40)

   CreateCoTlevel.resizable(0,0)

def CallCreateNewSemester():

   CreateSemTlevell()
   CreateSemTlevel.grab_set()
   SemesterEntrys()
   SelectSem.config(state='normal')

   SemNameLabel = Label(CreateSemTlevel, text ="*Semester Name : ",font='Arial')
   SemNameLabel.pack(padx=350,pady=20)

   SemNameEntry.pack(padx=350,pady=20)

   WeekLabel = Label(CreateSemTlevel, text ="*Week :" ,font='Arial')
   WeekLabel.pack(padx=350,pady=20)

   WeekEntry.pack(padx=350,pady=20)
   CreateSemTlevel.resizable(0,0)

   AddNewSmesterBttn()
   AddNewSemesterButton.pack(side=BOTTOM,padx=350,pady=40)
   CreateSemTlevel.resizable(0,0)


def Semesters():
     global SelectSem
     #FirstFrame.pack_propagate(0)
     #FirstFrame.place( anchor="e", relx=.5, rely=.63)
     CreateSemTlevell()
     CreateSemTlevel.grab_set()
     SemTlevelPos(450,580)
     SemesterListBox(CreateSemTlevel)

     CreatedSemesters = Text(CreateSemTlevel,borderwidth=0,font='Arial')
     CreatedSemesters.insert(INSERT,"Created Semesters")
     CreatedSemesters.place(relx=.1,rely=.18,height=30, width=150)


     Add = Button(CreateSemTlevel,text='Add Semester ',command = CallCreateNewSemester)
     Add.place(relx=.8, rely=.5, anchor="center", height=40, width=95)

     SelectSem = Button(CreateSemTlevel,text='Select Semester',command= Courses)
     SelectSem.place(relx=.8, rely=.4, anchor="center", height=40, width=95)
     SelectSem.config(state='disabled')

     CreateSemTlevel.resizable(0,0)

def Courses():

     CreateNewCoTlevell()
     CreateCoTlevel.grab_set()
     CourseTlevelPos(450,580)
     CourseListBox()
     index = SemesterList.curselection()[0]

     #SecondFrame.pack_propagate(0)
     #SecondFrame.place( anchor="w", relx=.5, rely=.63)

     CreatedCourses1 = Text(CreateCoTlevel,borderwidth=0,font='Arial',fg="black")
     CreatedCourses1.insert(INSERT,"Please \nAdd or Select a Course for : \n ")
     CreatedCourses1.place(relx=.1,rely=.05,height=60, width=400)
     CreatedCourses = Text(CreateCoTlevel,borderwidth=0,font='Arial 16',fg="blue")
     CreatedCourses.insert(INSERT,""+SemesterList.get(index))
     CreatedCourses.place(relx=.1,rely=.135,height=50, width=100)


     Add = Button(CreateCoTlevel,text='Add Course',command=CallCreateNewCourse)
     Add.place(relx=.8, rely=.5, anchor="center", height=40, width=95)

     Add = Button(CreateCoTlevel,text='Select Course')
     Add.place(relx=.8, rely=.4, anchor="center", height=40, width=95)

     CreateCoTlevel.resizable(0,0)



def Section():
     toplevel = Toplevel(width=450,height=580,bg='white')

     #SecondFrame.pack_propagate(0)
     #SecondFrame.place( anchor="w", relx=.5, rely=.63)

     CreatedCourses = Text(toplevel,borderwidth=0)
     CreatedCourses.insert(INSERT,"Created Courses")
     CreatedCourses.place(relx=.1,rely=.18,height=30, width=150)

     Lb1 = Listbox(toplevel)
     Lb1.insert(1, "")
     Lb1.insert(2, "")
     Lb1.insert(3, "")
     Lb1.insert(4, "")
     Lb1.insert(5, "")
     Lb1.insert(6, "")
     Lb1.place(relx=.1,rely=.25,height=250, width=200)

     Add = Button(toplevel,text='Add Section',command=CallCreateNewCourse)
     Add.place(relx=.8, rely=.5, anchor="center", height=35, width=95)

     Add = Button(toplevel,text='Select Section')
     Add.place(relx=.8, rely=.4, anchor="center", height=35, width=95)
     toplevel.resizable(0,0)



#Main

Buttons()

Semester.place(relx=.5, rely=.45, anchor="center", height=50, width=140)
#Course.place(relx=.5, rely=.5, anchor="center", height=50, width=95)

HTMLButton.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE,height=50,width=95)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)


root.winfo_x()
root.winfo_y()
root.config(menu=menubar)
center_window(400, 500)
#root.resizable(0,0)
root.mainloop()

