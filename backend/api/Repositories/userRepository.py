from api import (marshal_with,
                    Blueprint,
                    db,
                    request,
                    generate_password_hash
                    )
from api.models import User


class UserRepository:

    def get():
        users = User.query.all()
        return users    

    def post(username,password):
        user  = User(username,generate_password_hash(password))
        db.session.add(user)  # Add the user to the session
        db.session.commit()
        return User.query.all()
        
    def getByName(username):
        user =  User.query.filter_by(name=username).first()
        return user
