from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models.bid import Bid
from schemas.bid import CreateBid
from datetime import time , timedelta


# function to create bid

def Create_Bid(db: Session, bid: CreateBid, bidder_id : int, product_id: int, Closing_time: time):
    try:
        new_bid = Bid(**bid.model_dump(), bidderId = bidder_id, productId = product_id, closing_time = Closing_time)
        db.add(new_bid)
        db.commit()
        db.refresh(new_bid)
        return new_bid
    except:
        db.rollback()
        return False
    
def Get_Bid(db: Session, limit:int, skip: int):
    return db.query(Bid).offset(skip).limit(limit).all()
        
    