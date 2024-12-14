from api import db,fields
from api.Models.base import Base


productSerialized = {
    'id':fields.Integer,
    'name':fields.String,
    'purchase_uom_id':fields.Integer,
    'sale_uom_id':fields.Integer,
}

class Product(Base):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    
    purchase_uom_id = db.Column(db.Integer, db.ForeignKey('uom.id'), nullable=False)
    sale_uom_id = db.Column(db.Integer, db.ForeignKey('uom.id'), nullable=False)
    
    purchase_uom = db.relationship('Uom', foreign_keys=[purchase_uom_id])
    sale_uom = db.relationship('Uom', foreign_keys=[sale_uom_id])

    def __init__(self, name, purchase_uom_id, sale_uom_id):
        self.name = name
        self.purchase_uom_id = purchase_uom_id
        self.sale_uom_id = sale_uom_id

    def __repr__(self):
        return f"<Product(name='{self.name}')>"