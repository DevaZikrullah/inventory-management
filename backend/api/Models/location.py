from api import db,fields
from api.Models.base import Base


locationSerialized = {
    'id':fields.Integer,
    'name_location':fields.String,
    'short_name':fields.Integer,
}

class Location(Base):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(50))
    short_name = db.Column(db.String(3), nullable=False)
    is_warehouse = db.Column(db.Boolean)


    parent_location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    parent_location = db.relationship('Location', backref=db.backref('parent', remote_side=[id]))
    

    def __init__(self, location_name, short_name):
        self.location_name = location_name
        self.short_name = short_name
