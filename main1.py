from db_tables import *
from db_fonk import *
from semester_class import*
from course_class import*
from student_section import*




create_entity_tables()
create_relation_tables()

section = Section()
announcement = Announcement()
subject = Subject()
grade = Grade()
student = Student()
notee = Note()
from NewGUI import *


