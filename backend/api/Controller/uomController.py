from api.Domain.uomDomain import *
from api import request,jsonify,Blueprint

uomRoute = Blueprint('uom_route',__name__)

class UomController:
    
    @uomRoute.route('/create-uom',methods = ['POST'])
    def create():
        name = request.json['name']
        try:
            uomDomain.createUom(name)
            return jsonify(
            status = 200,
            message = 'create uom sucsess',
            )
        except:
            return jsonify(
                status=500,
                message = 'cant create uom'
            )