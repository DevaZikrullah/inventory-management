from api.Domain.locationDomain import *
from api import request,jsonify,Blueprint
from api.Schema.locationSchema import LocationSchema
from api import ValidationError


locationRoute = Blueprint('location_route',__name__)

class LocationController:
    
    @locationRoute.route('/create-location',methods = ['POST'])
    def create():
        try:
            location_data = LocationSchema(**request.json)
            
            locationDomain.createLocation(location_data)

            return jsonify(status=200, message='Location created successfully'), 200

        except ValidationError as e:
            return jsonify(status=400, message="Validation Error", errors=e.errors()), 400

        except Exception as e:
            return jsonify(status=500, message=f"Error: {str(e)}"), 500