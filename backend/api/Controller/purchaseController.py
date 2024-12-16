from api.Domain.purchaseDomain import *
from api import request,jsonify,Blueprint
from api.Schema.purchaseSchema import PurchaseSchema
from pydantic import ValidationError

purchaseRoute = Blueprint('purchase_route_controller',__name__)

class PurchaseController:
    
    @purchaseRoute.route('/create-purchase', methods=['POST'])
    def create():
        try:
            purchase_data = PurchaseSchema(**request.json)
            purchase_lines = request.json.get('purchase_line', [])

            if not isinstance(purchase_lines, list):
                return jsonify(status=400, message="Invalid format for purchase_line; expected a list"), 400
            
            purchaseDomain.createItem({
                'purchase_number': purchase_data.purchase_number,
                'vendor_name': purchase_data.vendor_name,
                'order_date': purchase_data.order_date
            },purchase_lines)

            return jsonify(status=200, message='Purchase created successfully'), 200

        except ValidationError as e:
            return jsonify(status=400, message="Validation Error", errors=e.errors()), 400

        except Exception as e:
            return jsonify(status=500, message=f"Error: {str(e)}"), 500