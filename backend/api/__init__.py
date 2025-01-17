from flask import Flask,request,Blueprint,jsonify,render_template
from flask_restful import Api,marshal_with,fields
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity
from flask_cors import CORS  
from pydantic import ValidationError


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flask'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)
CORS(app)

#run "flask test"
@app.cli.command('test')
def test():
    print('work')

from api import routes
from api.Models import product,purchase,uom,location