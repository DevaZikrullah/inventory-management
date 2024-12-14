from api.Domain.purchaseDomain import *
from api import request,jsonify,Blueprint

purchaseRoute = Blueprint('purchase_route_controller',__name__)

class PurchaseController:
    
    @purchaseRoute.route('/create-purchase', methods=['POST'])
    def create():
        try:
            purchase_number = request.json['purchase_number']
            vendor_name = request.json['vendor_name']
            order_date = request.json['order_date']
            purchase_lines = request.json.get('purchase_line', [])

            if not isinstance(purchase_lines, list):
                return jsonify(status=400, message="Invalid format for purchase_line; expected a list")

            purchaseDomain.createItem({
                'purchase_number': purchase_number,
                'vendor_name': vendor_name,
                'order_date': order_date
            },purchase_lines)
            return jsonify(status=200, message='purchase created successfully')
        except Exception as e:
            return jsonify(status=500, message=f"Error: {str(e)}")
