from fastapi import APIRouter, HTTPException
import app.data.cart as cart_data
from app.data.products import products
from app.models.cart import CartItem

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.get("")
def get_cart():
    return cart_data.cart_items


@router.post("")
def add_to_cart(product_id: int, quantity: int = 1):
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    for item in cart_data.cart_items:
        if item.product.id == product_id:
            item.quantity += quantity
            return item

    cart_item = CartItem(product=product, quantity=quantity)
    cart_data.cart_items.append(cart_item)
    return cart_item


@router.delete("/{product_id}")
def remove_from_cart(product_id: int):

    cart_data.cart_items = [
        item for item in cart_data.cart_items
        if item.product.id != product_id
    ]

    return {"message": "Item removed"}




@router.patch("/{product_id}")
def update_quantity(product_id: int, quantity: int):
    for item in cart_data.cart_items:
        if item.product.id == product_id:

            if quantity <= 0:
                cart_data.cart_items = [
                    i for i in cart_data.cart_items
                    if i.product.id != product_id
                ]
                return {"message": "Item removed"}

            item.quantity = quantity
            return item

    raise HTTPException(status_code=404, detail="Item not found")