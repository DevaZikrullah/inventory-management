from api.Repositories.purchaseRepository import PurchaseRepository
from api.Repositories.uomRepository import UomRepository

class purchaseDomain:

    def createItem(data_purhcase,data_purchase_line):
        print(data_purchase_line)
        if not UomRepository.getById(data_purhcase.get("purchase_uom_id")) or not UomRepository.getById(data_purhcase.get("sale_uom_id")):
            raise Exception('uom id not exist')
        
        if PurchaseRepository.getByNumber(data_purhcase.get("purchase_number")):
            raise Exception('name already exsist')
        else:    
            return PurchaseRepository.post(data_purhcase)
