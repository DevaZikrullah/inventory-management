from api.Repositories.productRepository import ProductRepository
from api.Repositories.uomRepository import UomRepository

class productDomain:

    def createItem(data):
        if not UomRepository.getById(data.get("purchase_uom_id")) or not UomRepository.getById(data.get("sale_uom_id")):
            raise Exception('uom id not exist')
        
        if ProductRepository.getByName(data.get("name")):
            raise Exception('name already exsist')
        else:    
            return ProductRepository.post(data)
