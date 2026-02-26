from pydantic import BaseModel
from app.models.product import Product


class CartItem(BaseModel):
    product: Product
    quantity: int