

from app import db
#create the database file, if it doesn't exist. 
db.create_all()

# import db models
from app.models import Class
from app.models import Major
from app.models import enrolled


c1 = Class.query.filter_by(coursenum = '321').filter_by(major='CptS').first()
c2 = Class.query.filter_by(coursenum = '322').filter_by(major='CptS').first()
c3 = Class.query.filter_by(coursenum = '355').filter_by(major='CptS').first()
c4 = Class.query.filter_by(coursenum = '451').filter_by(major='CptS').first()

s1 = Student.query.filter_by(username='sakire').first()

#Enroll student s1 in c2,c3,c4
s1.classes.append(c2)
s1.classes.append(c3)
s1.classes.append(c4)
db.session.commit()

#Unenroll student s1 from c4
s1.classes.remove(c4)
db.session.commit()

#all classes a given student is enrolled in
#alternative1:
for c in s1.classes:
    print(c)

#alternative2:
enrolledClasses = Class.query.join(enrolled, (enrolled.c.classid == Class.id)).filter(enrolled.c.studentid == s1.id).order_by(Class.coursenum).all()

#Check if student is enrolled in given class
s1.classes.filter(enrolled.c.classid == c2.id).count() > 0

#we can also add students to a classes roster
s2 = Student.query.filter_by(username='john').first()
c2.roster.append(s2)
db.session.commit()

for c in s2.classes:
    print(c)

for s in c2.roster:
    print(s)





#Create a major
newMajor = Major(name='CptS',department='School of EECS')
db.session.add(newMajor)
newMajor = Major(name='CE',department='Civil Engineering')
db.session.add(newMajor)
db.session.commit()
Major.query.all()
for m in Major.query.all():
    print(m)

#create class objects and write them to the database
newClass = Class(coursenum='322',major='CptS', title='Software Engineering')
db.session.add(newClass)
newClass = Class(coursenum='355',major='CE', title='Fluid Mechanics')
db.session.add(newClass)
db.session.commit()

# query and print classes
Class.query.all()
Class.query.filter_by(coursenum='322').all()
Class.query.filter_by(coursenum='322').first()
myclasses = Class.query.order_by(Class.coursenum.desc()).all()
for c in myclasses:
    print(c.coursenum)
