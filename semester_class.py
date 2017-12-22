import db_fonk


class Semester:
    def __init__(self):
        self.name = None
        self.week = None

    # Semester Name
    def setSemesterName(self, name):
        self.name = name

    def getSemesterName(self):
        return self.name

    # Semester week
    def setSemesterWeek(self, week):
        self.week = week

    def getSemesterWeek(self):
        return self.week

    # Database relation functions
    def insertSemesterIntoDatabase(self):
        db_fonk.insert_semester(self.name, self.week)

    def get_info_from_database(self):
        info = db_fonk.select_specific_semester(self.name)
        self.setSemesterName(info[0])
        self.setSemesterWeek(info[1])

    def get_all_semester(self):
        return db_fonk.select_all_semester()

    def edit_semester(self):
        db_fonk.edit_semester(self.name, self.week)

    def delete_semester(self):
        db_fonk.delete_semester(self.name)

semester = Semester()
