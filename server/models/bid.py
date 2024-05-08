from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from config.db import Base

class Bid(Base):
    __tablename__ = "bids"
    
    id = Column(Integer, primary_key=True, nullable= False)
    amount = Column(Integer, nullable= False)
    bidder_id = Column(String, ForeignKey("users.id"))
    product_id = Column(String, ForeignKey("products.id"))
    closing_time = Column(DateTime)
    
    # relationship
    
    bidder = relationship("User", back_populates="bidding")
    item = relationship("Product", back_populates="bid")