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

FirstFrame = Frame(width=300, height=500, bg='white')

SecondFrame = Frame(width=300, height=500, bg='white')

HTMLFrame = Frame(width=450, height=50,bg='white')
HTMLFrame.pack_propagate(0)
HTMLFrame.pack(fill=BOTH,side= BOTTOM)


def Create():

    CreateButton.destroy()

    CreateCourseButton.place(relx=.285, rely=.7, anchor="center", height=50, width=95)
    CreateSemesterButton.place(relx=.5, rely=.7, anchor="center", height=50, width=95)


def CallCreateNewCourse():

   toplevel = Toplevel(width=450, height=580, bg='white')

   S1 = Label(toplevel, text ="Course Name :")
   S1.pack(padx=350,pady=20)
   SeCode=Entry(toplevel)
   SeCode.pack(padx=350,pady=20)

   S1 = Label(toplevel, text ="Course Code :")
   S1.pack(padx=350,pady=20)
   SeCode=Entry(toplevel)
   SeCode.pack(padx=350,pady=20)

   S1 = Label(toplevel, text ="Course Book :")
   S1.pack(padx=350,pady=20)
   SeCode=Entry(toplevel)
   SeCode.pack(padx=350,pady=20)

   S1 = Label(toplevel, text ="Course Reference Book :")
   S1.pack(padx=350,pady=20)
   SeCode=Entry(toplevel)
   SeCode.pack(padx=350,pady=20)

   S1 = Label(toplevel, text ="Syllabus :")
   S1.pack(padx=350,pady=20)
   SeCode=Entry(toplevel)
   SeCode.pack(padx=350,pady=20)

   AddCourseButton = Button(toplevel,text= 'Add Course')
   AddCourseButton.pack(side=BOTTOM,padx=350,pady=40)

   toplevel.resizable(0,0)



def CallCreateNewSemester():

   toplevel = Toplevel(width=450, height=580, bg='white')


   S1 = Label(toplevel, text ="Semester Name :")
   S1.pack(padx=350,pady=20)
   SeCode=Entry(toplevel)
   SeCode.pack(padx=350,pady=20)

   S1 = Label(toplevel, text ="Week :")
   S1.pack(padx=350,pady=20)
   SeCode=Entry(toplevel)
   SeCode.pack(padx=350,pady=20)
   toplevel.resizable(0,0)

   AddSemesterButton = Button(toplevel,text= 'Add Semester')
   AddSemesterButton.pack(side=BOTTOM,padx=350,pady=40)







def CreateSemesters():
     toplevel = Toplevel(width = 450,height= 580,bg='white')

     #FirstFrame.pack_propagate(0)
     #FirstFrame.place( anchor="e", relx=.5, rely=.63)


     CreatedSemesters = Text(toplevel,borderwidth=0)
     CreatedSemesters.insert(INSERT,"Created Semesters")
     CreatedSemesters.place(relx=.1,rely=.18,height=30, width=150)

     Lb1 = Listbox(toplevel)
     Lb1.insert(1, "")
     Lb1.insert(2, "")
     Lb1.insert(3, "")
     Lb1.insert(4, "")
     Lb1.insert(5, "")
     Lb1.insert(6, "")
     Lb1.place(relx=.1,rely=.25,height=250, width=200)

     Add = Button(toplevel,text='Add Semester ',command = CallCreateNewSemester)
     Add.place(relx=.8, rely=.5, anchor="center", height=35, width=95)

     Add = Button(toplevel,text='Select Semester ')
     Add.place(relx=.8, rely=.4, anchor="center", height=35, width=95)



def Courses():
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

     Add = Button(toplevel,text='Add Course',command=CallCreateNewCourse)
     Add.place(relx=.8, rely=.5, anchor="center", height=35, width=95)

     Add = Button(toplevel,text='Select Course')
     Add.place(relx=.8, rely=.4, anchor="center", height=35, width=95)
     toplevel.resizable(0,0)



#Main


Semester = Button(root, text='Semester',command = CreateSemesters)
Semester.place(relx=.5, rely=.4, anchor="center", height=50, width=95)

Course = Button(root,text='Course',command = Courses)
Course.place(relx=.5, rely=.5, anchor="center", height=50, width=95)

HTMLButton = Button(root,text='HTML File')
HTMLButton.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE,height=50,width=95)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)

root.winfo_x()
root.winfo_y()
root.config(menu=menubar)
#root.resizable(0,0)
root.mainloop()

