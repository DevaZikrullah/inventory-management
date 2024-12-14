from api import db,fields
from api.Models.base import Base


uomSerialized = {
    'id':fields.Integer,
    'name':fields.String
}

class Uom(Base):
    __tablename__ = 'uom'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return self.name
