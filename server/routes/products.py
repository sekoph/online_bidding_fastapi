from sqlalchemy.orm import Session
from config.db import SessionLocal
from fastapi import APIRouter, Depends, HTTPException 


from crud.products import Create_Product, Get_Products
from schemas.products import CreateProduct, Product

productsRouter = APIRouter()

# define dependancy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
 
#get all products    
@productsRouter.get('/products/', response_model = list[Product])
def get_products(limit: int = 100, skip: int = 0 , db: Session = Depends(get_db)):
    return Get_Products(db, limit = limit, skip = skip)


# create new products
@productsRouter.post('/products/', response_model = Product)
def create_product(user_id: int, new_product: CreateProduct, db: Session = Depends(get_db)):
    return Create_Product(db = db, product = new_product, user_id = user_id)
