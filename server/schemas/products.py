from pydantic import BaseModel

class BaseProduct(BaseModel):
    product_name: str
    description: str
    location: str
    is_closed: bool
   
    
class CreateProduct(BaseProduct):
    pass

class Product(BaseProduct):
    id: int
    owner_id: int

    
    class config:
        orm_mode = True