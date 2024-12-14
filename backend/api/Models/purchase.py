from api import db,fields
from api.Models.base import Base


purchase_serialized = {
    'id':fields.Integer,
    'purchase_number':fields.String,
}

class Purchase(Base):
    __tablename__ = 'purchase'
    id = db.Column(db.Integer, primary_key=True)
    purchase_number = db.Column(db.String(50), nullable=False)
    vendor_name = db.Column(db.String(50), nullable=False)
    order_date = db.Column(db.DateTime, nullable = False)
    
    def __init__(self, purchase_number):
        self.purchase_number = purchase_number

    # def __repr__(self):
    #     return f"<Purchase(name='{self.purchase_number}')>"
    
class PurchaseLine(Base):
    __tablename__ = 'purchase_line'
    id = db.Column(db.Integer, primary_key=True)


    purchase_id = db.Column(db.Integer, db.ForeignKey('purchase.id'), nullable=False)
    purchase_purchase_line = db.relationship('Purchase', foreign_keys=[purchase_id])

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product_purchase_line = db.relationship('Product', foreign_keys=[product_id])

    qty = db.Column(db.Integer)
    taxes = db.Column(db.Float)

    purchase_line_uom_id = db.Column(db.Integer, db.ForeignKey('uom.id'), nullable=False)
    purchase_line_uom = db.relationship('Uom', foreign_keys=[purchase_line_uom_id])

    total = db.Column(db.Float)

    
    def __init__(self, purchase_number,purchase_id):
        self.purchase_id = purchase_id
        self.purchase_number = purchase_number

    # def __repr__(self):
    #     return f"<Product(name='{self.name}')>"