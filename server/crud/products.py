from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.products import Product
from schemas.products import CreateProduct


# create new product

def Create_Product(db: Session , product: CreateProduct, user_id: int):
    try:
        new_product = Product(**product.model_dump(), owner_id = user_id)
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
    except IntegrityError:
        db.rollback()
        return False
    # product_name = product.product_name, description = product.description, location = product.location, is_closed = product.is_closed,
    
def Get_Products(db: Session, limit:int, skip: int):
     return db.query(Product).offset(skip).limit(limit).all()    



