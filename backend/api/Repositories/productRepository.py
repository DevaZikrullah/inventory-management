from api import marshal_with,Blueprint,db,request
from api.Models.product import Product,productSerialized


class ProductRepository:

    @marshal_with(productSerialized)
    def get():
        product = Product.query.all()
        return product


    def post(product_data):
        product  = Product(**product_data)
        db.session.add(product)
        db.session.commit()
        return Product.query.all()

    def getByName(name):
        product = Product.query.filter_by(name=name).first()
        return product
    
    def getById(id :int):
        product = Product.query.get(id)
        return product
    
