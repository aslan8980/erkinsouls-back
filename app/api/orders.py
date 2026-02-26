from fastapi import APIRouter, HTTPException
from app.data.cart import cart_items
from app.data.orders import orders
from app.models.order import Order

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("")
def create_order():
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total_price = sum(
        item.product.price * item.quantity for item in cart_items
    )

    order = Order(
        id=len(orders) + 1,
        items=cart_items.copy(),
        total_price=total_price
    )

    orders.append(order)
    cart_items.clear()  # очищаем корзину после заказа

    return order


@router.get("")
def get_orders():
    return orders