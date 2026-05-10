from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Cart, CartItem

app = FastAPI()

DATABASE_URL = "mysql+pymysql://root:Yash%402004@localhost/ecommerce_cart"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

@app.post("/cart/")
def create_cart(user_id: int):
    db = SessionLocal()
    cart = Cart(user_id=user_id)
    db.add(cart)
    db.commit()
    db.refresh(cart)
    db.close()
    return {"cart_id": cart.id}

@app.post("/cart/{cart_id}/item/")
def add_item(cart_id: int, product_id: int, quantity: int):
    db = SessionLocal()
    item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity)
    db.add(item)
    db.commit()
    db.close()
    return {"message": "Item added"}

@app.get("/cart/{cart_id}")
def get_cart(cart_id: int):
    db = SessionLocal()
    items = db.query(CartItem).filter(CartItem.cart_id == cart_id).all()
    db.close()

    if not items:
        return {"message": "Cart empty or not found"}

    return items
