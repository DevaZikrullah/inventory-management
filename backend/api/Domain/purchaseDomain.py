from api.Repositories.purchaseRepository import PurchaseRepository
from api.Repositories.uomRepository import UomRepository

class purchaseDomain:

    def createItem(data_purhcase,data_purchase_line):
        
        if PurchaseRepository.getByNumber(data_purhcase.get("purchase_number")):
            raise Exception('Number already exsist')
        
        purchase = PurchaseRepository.post_purchase(data_purhcase)
        # print(purchase_id.id)
        # exit()
        for value_purchase_line in data_purchase_line:
            if not UomRepository.getById(value_purchase_line.get("uom_id")):
                raise Exception('uom id not exist')
            PurchaseRepository.post_purchase_line(value_purchase_line,purchase.id)  