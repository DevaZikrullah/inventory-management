from api import marshal_with,Blueprint,db,request
from api.Models.purchase import Purchase,purchase_serialized,PurchaseLine


class PurchaseRepository:

    @marshal_with(purchase_serialized)
    def get():
        purchase = Purchase.query.all()
        return purchase


    def post_purchase(purchase_data):
        purchase  = Purchase(**purchase_data)
        db.session.add(purchase)
        db.session.commit()
        return purchase
    
    def post_purchase_line(purchase_line_data,purchase_id :int):
        purchase_line = PurchaseLine(**purchase_line_data,purchase_id=purchase_id)
        db.session.add(purchase_line)
        db.session.commit()
        return purchase_line


    def getByNumber(purchase_number):
        purchase = Purchase.query.filter_by(purchase_number=purchase_number).first()
        return purchase
    
