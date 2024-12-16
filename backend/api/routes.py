from api import app,Blueprint
from .Controller.authController import authentication
from .Controller.productController import productRoute
from .Controller.uomController import uomRoute
from .Controller.purchaseController import purchaseRoute

api = Blueprint('api', __name__, url_prefix='/api')
web = Blueprint('web',__name__)

api.register_blueprint(productRoute)
api.register_blueprint(purchaseRoute)
api.register_blueprint(authentication)
api.register_blueprint(uomRoute)


app.register_blueprint(api)

app.register_blueprint(web)