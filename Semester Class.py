import db_fonk


class Semester:
    def __init__(self, name, week="Empty"):
        self.name = name
        self.week = week
        self.insertSemesterIntoDatabase()

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

    def get_info_from_database(self, name):
        info = db_fonk.select_specific_semester(name)
        self.setSemesterName(info[0])
        self.setSemesterWeek(info[1])

    def get_all_semester(self):
        return db_fonk.select_all_semester()

    def edit_semester(self, name):
        self.get_info_from_database(name)
        # Here system waits for user to make any change
        db_fonk.edit_semester(self.name, self.week)

    def delete_semester(self, name):
        db_fonk.delete_semester(name)

