from api.Repositories.uomRepository import UomRepository

class uomDomain:

    def createUom(name):
        if UomRepository.getByName(name):
            raise Exception('name already exsist')
        else:    
            return UomRepository.post(name)
