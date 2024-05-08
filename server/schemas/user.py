from pydantic import BaseModel
from schemas.products import Product


# base class for user
class UserBase(BaseModel):
    username: str
    email: str
    role: str
    

# to create user 
class CreateUser(UserBase):
    password: str


#to pass all the user  
class User(UserBase):
    id: int
    products:list[Product] = []
    
    class config:
        orm_mode = True
        
