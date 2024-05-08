from sqlalchemy import DateTime, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base


class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key = True, nullable= False)
    product_name = Column (String, index = True, nullable= False)
    description = Column(String, index = True, nullable= False)
    location = Column(String, index = True, nullable= False)
    is_closed = Column(Boolean, default = False)
    
    # owner_email = Column(String, ForeignKey = "users.email")
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    # relationship
    owner =  relationship("User", back_populates = "products")
    bid = relationship("Bid", back_populates= "item")
     