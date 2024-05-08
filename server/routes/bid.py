from sqlalchemy.orm import Session
from config.db import SessionLocal
from fastapi import APIRouter, Depends , HTTPException, Body

from crud.bid import Create_Bid, Get_Bid
from schemas.bid import Bid, CreateBid
from datetime import time, timedelta

from typing import Annotated


# define dependancy

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# define the routers

BidRouter = APIRouter()

@BidRouter.put('/bid/', response_model = Bid)
def create_bid(bidder_id: int, product_id: int , new_bid: CreateBid , end_time: Annotated[time | None, Body()] = None, db: Session = Depends(get_db)):
    return Create_Bid(db = db, bid = new_bid, bidder_id = bidder_id, product_id = product_id, Closing_time = end_time)


@BidRouter.get('/bid/', response_model = list[Bid])
def get_bids(limit: int = 100, skip:int = 0, db: Session = Depends(get_db)):
    return Get_Bid(db = db, limit = limit, skip = skip)