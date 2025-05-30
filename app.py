from database import engine, Base
from models import User, Product, CartItem, Review

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)