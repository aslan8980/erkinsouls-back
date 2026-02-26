from fastapi import APIRouter, HTTPException
from app.data.products import products
from app.models.product import Product

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("", response_model=list[Product])
def get_products():
    return products


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")