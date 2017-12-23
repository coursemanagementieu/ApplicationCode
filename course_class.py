import db_fonk


class Course:

    def __init__(self):
        self.courseName = None
        self.courseCode = None
        self.courseID = None
        self.courseBook = None
        self.refBookName = None
        self.syllabus = None
        self.htmlfile="""<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		
		<link href="https://fonts.googleapis.com/css?family=Work+Sans:400,600&subset=latin-ext" rel="stylesheet">
		
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
		<!-- Latest compiled and minified CSS -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
		<!-- Optional theme -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
		<!-- Latest compiled and minified JavaScript -->
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
		<script src="https://use.fontawesome.com/6cba04d2b9.js"></script>
		<style>
			body {{
				font-family: 'Work Sans';
			}}
		</style>
		<title>{derskodu} - {dersadi}</title>
	</head>
	
	<body>
		<div class="container">
			<div class="page-header">
				<h3>{derskodu} - {dersadi}</h3>
				<h4>Kaya Oğuz, {semesteradi}</h4>
			</div>
		</div>
		
		<div class="container">
			<div class="col-xs-12 col-sm-6">
				<div class="panel panel-info">
					<div class="panel-heading">Course Information</div>
					<table class="table">
						<tbody>
							<tr><td>Syllabus</td><td>:</td><td><a href="{sylubuslinki}">Link</a></td></tr>
							<tr><td>Classroom</td><td>:</td><td>{sınıf}</td></tr>
							<tr><td>Hours</td><td>:</td><td>{gun}, {saat}</td></tr>
							<tr><td>Textbook</td><td>:</td><td>{textbook}</td></tr>
							<!-- <tr><td>Course Slides</td><td>:</td><td><a href="#">Link</a></td></tr>
							<tr><td>Other course material</td><td>:</td><td><a href="files/">Link</a></td></tr>-->
							
						</tbody>
					</table>
				</div>
				<div class="panel panel-info">
					<div class="panel-heading">Lecturer Information</div>
					<table class="table">
						<tbody>
							<tr><td>E-mail</td><td>:</td><td>kayaoguz /a/ gmail.com</td></tr>
							<tr><td>Address</td><td>:</td><td>Izmir University of Economics
Faculty of Engineering
Department of Computer Engineering
Sakarya Cad. No:156, 35330, Balçova, İzmir</td></tr>
							<tr><td>Office Hours</td><td>:</td><td>Mondays 15:00-15:50 and Wednesdays 11:00-11:50</td></tr>
							<tr><td>Home URL</td><td>:</td><td><a href="http://homes.ieu.edu.tr/koguz/">Link</a></td></tr>
						</tbody>
					</table>
				</div>
			</div>
			<div class="col-xs-12 col-sm-6">
				<div class="panel panel-info">
					<div class="panel-heading">Lectures</div>
					<div class="panel-body">
						<table class="table table-striped">
							<thead>
								<tr><th>Date</th><th>Topic</th></tr>
							</thead>
							<tbody>
								<tr>
									<td>Week 1<br />2016.09.30</td>
									<td>Chapter 01: Introduction<br />
									<a href="https://www.dropbox.com/s/2tv5z1g3vah8xq2/Ch01.pptx?dl=0">Presentation</td>
								</tr>
								<tr>
									<td>Week 2<br />2016.10.07</td>
									<td>Chapter 02: Software Processes<br />
									<a href="https://www.dropbox.com/s/5u4fos77na9bvit/Ch02.pptx?dl=0">Presentation</td>
								</tr>
								<tr>
									<td>Week 3<br />2016.10.14</td>
									<td>Chapter 03: Agile Software Development<br />
									<a href="https://www.dropbox.com/s/u4k0hrzgwy8jj4i/Ch03.pptx?dl=0">Presentation</td>
								</tr>
								<tr>
									<td>Week 4<br />2016.10.21</td>
									<td>Chapter 04: Requirements Engineering<br />
									<a href="https://www.dropbox.com/s/pklwjh49zflheth/Ch04.pptx?dl=0">Presentation</td>
								</tr>
                                <tr>
									<td>Week 5<br />2016.11.04</td>
									<td>Chapter 05: System Modeling<br />
									<a href="https://www.dropbox.com/s/xv6a3wia6vf0si8/Ch05.pptx?dl=0">Presentation</td>
								</tr>
								<tr>
									<td>Week 6<br />2016.11.11</td>
									<td>Chapter 06: Architectural Design<br />
									<a href="https://www.dropbox.com/s/4f0sxsrfy0wcz4j/Ch06.pptx?dl=0">Presentation</td>
								</tr>
                                <tr>
									<td>Week 7<br />2016.11.18</td>
									<td>MIDTERM</td>
								</tr>
								<tr>
									<td>Week 8<br />2016.11.25</td>
									<td>Chapter 07: Design and Implementation<br />
									<a href="https://www.dropbox.com/s/3vo5cqk4q9qv8jz/Ch07.pptx?dl=0">Presentation</td>
								</tr>
								<tr>
									<td>Week 9<br />2016.12.02</td>
									<td>Practice with new Project<br />Project Meetings
									</td>
								</tr>
								<tr>
									<td>Week 10<br />2016.12.09</td>
									<td>Chapter 08: Software Testing<br />
									<a href="https://www.dropbox.com/s/40wk47mq3idlsal/Ch08.pptx?dl=0">Presentation</td>
								</tr>
								<tr>
									<td>Week 11<br />2016.12.16</td>
									<td>Chapter 09: Software Evolution<br />
									<a href="https://www.dropbox.com/s/cj9dgun1x4lgmrq/Ch09.pptx?dl=0">Presentation</td>
								</tr>
                                <tr>
									<td>Week 12<br />2016.12.23</td>
									<td>Chapter 10: Software Engineering<br />
									<a href="https://drive.google.com/open?id=1j9JIpKqDWVv_kcL5vhP95i_6DRdHz70Q_4EBi4N0IXI">Presentation</td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>
				<div class="panel panel-info">
					<div class="panel-heading">Announcements</div>
					<div class="panel-body">
						<table class="table table-striped">
							<thead>
								<tr><th>Date</th><th>Announcement</th></tr>
							</thead>
							<tbody>
								<tr>
									<td>2016.09.30, 09:11</td>
									<td>Midterm: Midterm will be on 18th of November.</td>
								</tr>
								<tr>
									<td>2016.19.22, 16:26</td>
									<td>Just for this week, our lecture will be at M201. Please tell your friends.</td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>"""


    def setCourseName(self, name):
        self.courseName = name

    def setCourseCode(self, code):
        self.courseCode = code

    def setCourseSyllabus(self, syllabus):
        self.syllabus = syllabus

    def setCourseBook(self, book):
        self.courseBook = book

    def setRefBookName(self, refbook):
        self.refBookName = refbook

    def setCourseID(self, rowid):
        self.courseID = rowid

    def getCourseName(self):
        return self.courseName

    def getCourseCode(self):
        return self.courseCode

    def getCourseBook(self):
        return self.courseBook

    def getRefBookName(self):
        return self.refBookName

    def getSyllabus(self):
        return self.syllabus

    def get_courseID(self):
        return self.courseID

    def generatehtml(self,semester,classroom,day,hour):
        self.htmlfile.format(derskodu=self.getCourseCode(),dersadi=self.getCourseName(),semesteradi=semester,sylubuslinki=self.getSyllabus(),sınıf=classroom,gun=day,saat=hour,textbook=self.getCourseBook())
        temp=open("file.html","w")
        temp.write(self.htmlfile)
        temp.close()



    # These functions is related with database
    def insertCourseInDatabase(self, semesterName):
        self.courseID = db_fonk.insert_course(self.courseName, self.courseCode, self.courseBook,
                                              self.refBookName, self.syllabus)
        db_fonk.insert_coursein(semesterName, self.courseID)

    # Before using this function we need to know courseID(rowid)
    def edit_course(self):
        db_fonk.edit_course(self.courseID, self.courseName, self.courseCode, self.courseBook,
                            self.refBookName, self.syllabus)

    # Before using this function we need to know courseCode
    def get_rowid_from_database(self, semesterName):
        self.courseID = db_fonk.select_course_rowid(semesterName, self.courseCode)

    # This function will be using since we know the rowid
    def get_info_from_database(self):
        info = db_fonk.select_specific_course(self.courseID)
        self.setCourseName(info[0])
        self.setCourseCode(info[1])
        self.setCourseBook(info[2])
        self.setRefBookName(info[3])
        self.setCourseSyllabus(info[4])

    # Display all of the courses in specific semester
    def get_all_course_in(self, semesterName):
        return db_fonk.select_all_course_in_semester(semesterName)

    def delete_course(self, semesterName):
        self.courseID = db_fonk.select_course_rowid(semesterName, self.courseCode)
        db_fonk.delete_course(self.courseID)


class Announcement:
    def __init__(self):
        self.date = None
        self.head = None
        self.announcement = None
        self.ID = None

    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date

    def setHead(self, head):
        self.head = head

    def setID(self, rowid):
        self.ID = rowid

    def getHead(self):
        return self.head

    def setAnnouncement(self, announcement):
        self.announcement = announcement

    def getAnnouncement(self):
        return self.announcement

    # These functions are related with database
    def insertAnnouncementInDatabase(self, semesterName, courseID):
        self.ID = db_fonk.insert_announcement(self.date, self.head, self.announcement)
        db_fonk.insert_announcementin(semesterName, courseID, self.ID)

    # Before using this function we need to know head of announcement
    def get_rowid_from_database(self, semesterName, courseID):
        self.ID = db_fonk.select_announcement_rowid(semesterName, courseID, self.head)

    # Before using this function we need to know announcementID
    def get_info_from_database(self):
        info = db_fonk.select_specific_announcement(self.ID)
        self.setDate(info[0])
        self.setHead(info[1])
        self.setAnnouncement(info[2])

    def edit_announcement(self):
        db_fonk.edit_announcement(self.ID, self.date, self.head, self.announcement)

    # These function returns array of announcementID
    def get_all_announcement_in(self, semesterName, courseID):
        return db_fonk.select_all_announcement_in(semesterName, courseID)

    # Before using this function we need to know announcementID
    def delete_announcement(self):
        db_fonk.delete_announcement(self.ID)


class Subject:
    def __init__(self):
        self.subject = None
        self.reference = None
        self.week = None
        self.ID = None

    def setSubject(self, subject):
        self.subject = subject

    def getSubject(self):
        return self.subject

    def setReference(self, reference):
        self.reference = reference

    def getReference(self):
        return self.reference

    def setWeek(self, week):
        self.week = week

    def getWeek(self):
        return self.week

    def setID(self, rowid):
        self.ID = rowid

    # These functions are related with database
    def insertSubjectInDatabase(self, semesterName, courseID):
        self.ID = db_fonk.insert_subject(self.subject, self.reference, self.week)
        db_fonk.insert_subjectin(semesterName, courseID, self.ID)

    def get_rowid_from_database(self, semesterName, courseID):
        self.ID = db_fonk.select_subject_rowid(semesterName, courseID, self.week)

    def get_info_from_database(self):
        info = db_fonk.select_specific_subject(self.ID)
        self.setSubject(info[0])
        self.setReference(info[1])
        self.setWeek(info[2])

    def edit_subject(self):
        db_fonk.edit_subject(self.ID, self.subject, self.reference, self.week)

    def delete_subject(self):
        db_fonk.delete_subject(self.ID)

    def get_all_subject_in(self, semesterName, courseID):
        return db_fonk.select_all_subject_in(semesterName, courseID)


