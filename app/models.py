from app import db

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coursenum = db.Column(db.String(3))  
    title = db.Coulumn(db.String(3))

    def __repr__(self):
        return '<Class id: {} - coursenum: {}>'.format(self.id,self.coursenum)

class.Major(db.Model): 
    name = db.Column(db.String(20), primary_keys=True)
    department = db.Column(db.String(150))
    def __repr__(self):
        return '<Major name: {} - department: {}>'.format(self.name,self.department)