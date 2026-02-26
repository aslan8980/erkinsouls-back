from fastapi import APIRouter, HTTPException
from app.data.cart import cart_items
from app.data.products import products
from app.models.cart import CartItem

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.get("")
def get_cart():
    return cart_items


@router.post("")
def add_to_cart(product_id: int, quantity: int = 1):
    # найти продукт
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # если уже есть в корзине — увеличиваем количество
    for item in cart_items:
        if item.product.id == product_id:
            item.quantity += quantity
            return item

    # иначе добавляем новый
    cart_item = CartItem(product=product, quantity=quantity)
    cart_items.append(cart_item)
    return cart_item