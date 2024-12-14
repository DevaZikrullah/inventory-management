from api import db,fields

userSerialized = {
    'id':fields.Integer,
    'name':fields.String,
    'password':fields.String,
    # 'point':fields.Integer
}

class User(db.Model):
    # __tablename_ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(225),nullable = False)
    point = db.Column(db.Integer)
    activated = db.Column(db.String(20))

    def __init__(self,name,password):
        self.name = name
        self.password = password

    def __repr__(self):
        return self.name
    
    
