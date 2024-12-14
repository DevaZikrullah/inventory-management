from api.Domain.productDomain import *
from api import request,jsonify,Blueprint

productRoute = Blueprint('item_route_controller',__name__)

class ProductController:
    
    @productRoute.route('/create-product', methods=['POST'])
    def create():
        try:
            name = request.json['name']
            purchase_uom_id = request.json['purchase_uom_id']
            sale_uom_id = request.json['sale_uom_id']

            productDomain.createItem({
                'name': name,
                'purchase_uom_id': purchase_uom_id,
                'sale_uom_id': sale_uom_id
            })
            return jsonify(status=200, message='Item created successfully')
        except Exception as e:
            return jsonify(status=500, message=f"Error: {str(e)}")
