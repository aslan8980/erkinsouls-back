from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    id: int
    title: str
    price: float
    images: List[str]
    category: str
    description: str