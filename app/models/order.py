from pydantic import BaseModel
from typing import List
from app.models.cart import CartItem


class Order(BaseModel):
    id: int
    items: List[CartItem]
    total_price: float