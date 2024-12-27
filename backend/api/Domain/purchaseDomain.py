from api.Repositories.purchaseRepository import PurchaseRepository
from api.Repositories.uomRepository import UomRepository
from api.Repositories.productRepository import ProductRepository

class purchaseDomain:

    def createItem(data_purchase, data_purchase_line):
        if PurchaseRepository.getByNumber(data_purchase.purchase_number):
            raise Exception('Number already exists')

        purchase_data = data_purchase.dict()
        purchase_data.pop('purchase_line', None)

        purchase = PurchaseRepository.post_purchase(purchase_data)

        for value_purchase_line in data_purchase_line:
            if not UomRepository.getById(value_purchase_line.get("uom_id")):
                raise Exception('UoM ID does not exist')
            if not ProductRepository.getById(value_purchase_line.get("product_id")):
                raise Exception('Product ID does not exist')

            value_purchase_line['purchase_id'] = purchase.id

            PurchaseRepository.post_purchase_line(value_purchase_line)