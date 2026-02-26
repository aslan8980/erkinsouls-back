from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.products import router as products_router
from app.api.cart import router as cart_router
from app.api.orders import router as orders_router

app = FastAPI(title="MenStore API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products_router)
app.include_router(orders_router)
app.include_router(cart_router)

@app.get("/")
def root():
    return {"status": "ok"}