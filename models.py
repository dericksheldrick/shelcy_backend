from sqlalchemy import Column,Integer, String, Boolean, Float, Text, ForeignKey,DateTime
from sqlalchemy.orm import relationship 
from database import Base
from datetime import datetime, timezone

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    username = Column(String, nullable = False, unique = True)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    is_admin = Column(Boolean, default = False)
    avatar_url = Column(String)
    created_at = Column(DateTime, default = datetime.now(timezone.utc))

    cart_items = relationship('CartItem', back_populates = 'user', cascade = 'all, delete-orphan') #if the user is deleted we also delete the items he had place in cart
    orders = relationship('Order', back_populates='user')
    reviews = relationship('Review', back_populates = 'user', foreign_keys='Review.user_id', cascade = 'all, delete-orphan') # if user is deleted, we alss delete his reviews 

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    price = Column(Float, nullable = False)
    image = Column(String)
    category = Column(String)
    description = Column(Text)
    collection = Column(Text)
    stock = Column(Integer, default = 0)
    created_at = Column(DateTime, default = datetime.now(timezone.utc))

    cart_items = relationship('CartItem', back_populates = 'product')
    order_items = relationship('OrderItem', back_populates='product')
    reviews = relationship('Review', back_populates = 'product',foreign_keys='Review.product_id', cascade = 'all, delete-orphan')  # if the product is deleted, the reviews are also removed.


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    total_amount = Column(Float)
    status = Column(String)
    created_at = Column(DateTime, default = datetime.now(timezone.utc))

    user = relationship('User', back_populates = 'orders')
    order_items = relationship('OrderItem', back_populates = 'order')

class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key = True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, default = 1)
    price = Column(Float)

    order = relationship('Order', back_populates = 'order_items')
    product = relationship('Product', back_populates = 'order_items')


class CartItem(Base):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, default = 1)

    user = relationship('User', back_populates = 'cart_items')
    product = relationship('Product', back_populates = 'cart_items')

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    rating = Column(Integer)
    comment = Column(String)
    created_at = Column(DateTime, default = datetime.now(timezone.utc))

    user = relationship('User', back_populates = 'reviews', foreign_keys=[user_id])
    product = relationship('Product', back_populates = 'reviews',foreign_keys=[product_id])