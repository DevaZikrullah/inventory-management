from api import marshal_with,db
from api.Models.uom import Uom,uomSerialized


class UomRepository:

    @marshal_with(uomSerialized)
    def get():
        uom = Uom.query.all()
        return uom

    def post(name :str):
        uom  = Uom(name = name)
        db.session.add(uom)
        db.session.commit()
        return Uom.query.all()

    def getByName(name :str):
        uom = Uom.query.filter_by(name=name).first()
        return uom
    
    def getById(id :int):
        uom = Uom.query.get(id)
        return uom
    
