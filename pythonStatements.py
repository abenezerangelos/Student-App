

from app import db
#create the database file, if it doesn't exist. 
db.create_all()

# import db models
from app.models import Class

#Create a major
newMajor = Major(name='CptS',department='School of EECS')
db.session.add(newMajor)
newMajor = Major(name='CE',department='Civil Engineering')
db.session.add(newMajor)
db.session.commit()

#create class objects and write them to the database
newClass = Class(coursenum='322',major='CptS', title='Software Engineering')
db.session.add(newClass)
newClass = Class(coursenum='355',major='CE', title='Fluid Mechanics')
db.session.add(newClass)
db.session.commit()
for m in Major.query.all():
    print(m)
    
# query and print classes
Class.query.all()
Class.query.filter_by(coursenum='322').all()
Class.query.filter_by(coursenum='322').first()
myclasses = Class.query.order_by(Class.coursenum.desc()).all()
for c in myclasses:
    print(c.coursenum)
