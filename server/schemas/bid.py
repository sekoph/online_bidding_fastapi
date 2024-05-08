from pydantic import BaseModel
from datetime import time

class BidBase(BaseModel):
    amount: int
    

    
class CreateBid(BidBase):
    pass 


class Bid(BidBase):
    id: int
    bidderId: int
    productId: int
    closingTime: time

   
    
    
    class config:
        orm_mode = True