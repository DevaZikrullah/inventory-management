from api import Blueprint,request
from api.Repositories.userRepository import *
from api.Domain.authDomain import *

authentication = Blueprint('auth_route',__name__)

class Authentication:
    @authentication.route('/register', methods =['GET', 'POST'])
    def register():
        username = request.json['username']
        password = request.json['password']
        try:
            AuthDomain.createAccount(username,password)
            return jsonify(
            status = 200,
            message = 'Succses Creataed Account',
            )
        except Exception as e:
            return jsonify(
                status=500,
                message=f"Can't create account: {str(e)}"
            )


    @authentication.route('/info', methods =['GET'])
    @jwt_required
    def info_account():
        try:
            AuthDomain.info_my_acc(get_jwt_identity())
            return jsonify(
            status = 200,
            message = 'Succses load info account',
            )
        except:
            return jsonify(
                status=500,
                message = 'Failed load info account'
            )
    
    @authentication.route('/login', methods =['POST'])
    def login():
        username = request.json['username']
        password = request.json['password']
        try:
            AuthDomain.login(username,password)
            token = create_access_token(identity=username)
            return jsonify(
            bearer_token= token,
            status = 200,
            message = 'Succses load info account',
            )
        except Exception as e:
            return jsonify(
                status=500,
                message=f"Failed load info account {str(e)}"
            )
