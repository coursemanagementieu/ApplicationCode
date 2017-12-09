class Section:
    def __init__(self):
        self.sectionCode=""
        self.day=[]
        self.hour=[]
        self.classRoom=[]
        self.Students=[]

    def setSectionCode(self,code):
        self.sectionCode=code

    def getSectionCode(self):
        return self.sectionCode

    def setDay(self,day):
        self.day.append(day)

    def getDay(self):
        return self.day

    def setHour(self,hour):
        self.hour.append(hour)

    def getHour(self):
        return self.hour

    def setClassRoom(self,classRoom):
        self.classRoom=classRoom

    def getClassRoom(self):
        return self.classRoom

    def setStudent(self):
        pass

    def getStudent(self):
        pass

    def displaySection(self):
        print("Section Code:",self.getSectionCode())
        print("Section Day/s:")
        for i in self.getDay():
            print(i)
        print("Hours:")
        for i in self.getHour():
            print(i)
        print("Classroom:",self.getClassRoom())


class Student(Section):
    def __init__(self):
        super().__init__()
        self.studentName=""
        self.studentId=""
        self.note=[]
        self.grade=[]

    def setStudentName(self,name):
        self.studentName=name

    def getStudentName(self):
        return self.studentName

    def setStudentId(self,id):
        self.studentId=id

    def getStudentId(self):
        return self.studentId

    def setNote(self,note):
        self.note.append(note)

    def getNote(self):
        return self.note

    def setGrade(self,grade):
        self.grade=grade

    def getGrade(self):
        return self.grade

    def getTotalGrade(self):
        pass
    def getLetterGrade(self):
        pass

    def display(self):
        print("Name:",self.getStudentName())
        print("Id:",self.getStudentId())
        print("Notes:")
        counter=1
        for i in self.getNote():
            print(counter,":",i)
            counter=counter+1






