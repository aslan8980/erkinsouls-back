from app.models.product import Product

products: list[Product] = [
    Product(
        id=1,
        title="Black Oversized Hoodie",
        price=49.99,
        images=[
            "https://example.com/hoodie-1.jpg",
            "https://example.com/hoodie-2.jpg",
        ],
        category="hoodies",
        description="Comfortable oversized hoodie made from cotton."
    ),
    Product(
        id=2,
        title="Classic White T-Shirt",
        price=19.99,
        images=[
            "https://example.com/tshirt-1.jpg",
        ],
        category="tshirts",
        description="Minimalist white t-shirt for everyday wear."
    ),
]