from api import marshal_with,Blueprint,db,request
from api.Models.location import Location,locationSerialized


class LocationRepository:

    @marshal_with(locationSerialized)
    def get():
        location = Location.query.all()
        return location

    def post(location_data):
        location  = Location(**location_data)
        db.session.add(location)
        db.session.commit()
        return Location.query.all()

    def getByShortName(short_name):
        location = Location.query.filter_by(short_name=short_name).first()
        return location
    
    def getById(id :int):
        location = Location.query.get(id).first()
        return location
    
