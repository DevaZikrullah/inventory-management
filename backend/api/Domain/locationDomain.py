from api.Repositories.locationRepository import LocationRepository
from api.Repositories.productRepository import ProductRepository

class locationDomain:

    def createLocation(data):
        if hasattr(data, 'parent_location_id'):
            if LocationRepository.getById(data.parent_location_id):
                raise Exception('not found parent_id')
        LocationRepository.post(data.dict())

        
        