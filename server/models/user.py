from sqlalchemy import Column , String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from config.db import Base
# from config.db import meta


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key= True, index=True)
    username = Column(String, index=True, nullable= False)
    email =  Column(String,index= True, unique= True, nullable= False)
    hashed_password = Column(String ,nullable=False)
    role = Column(String, index=True, nullable=False)
    
    # relationship
    
    products = relationship("Product", back_populates="owner")
    bidding = relationship("Bid", back_populates="bidder")
    

    