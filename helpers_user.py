from database import session
from models import Product, CartItem, Review

def welcome_shopper():
    print("🛍️  Welcome to Shelcy CLI - Your Terminal Boutique!")

def browse_products():
    print("\n📦 Available Products:")
    products = session.query(Product).all()
    for p in products:
        print(f"{p.id}. {p.name} - ${p.price:.2f} - {p.category}")

def view_product_details():
    pid = input("Enter product ID: ")
    product = session.query(Product).get(pid)
    if product:
        print(f"\n🧾 {product.name}")
        print(f"Price: ${product.price}")
        print(f"Description: {product.description}")
        print(f"Stock: {product.stock}")
    else:
        print("❌ Product not found.")

def search_by_category():
    cat = input("Enter category: ")
    results = session.query(Product).filter_by(category=cat).all()
    if results:
        for p in results:
            print(f"{p.id}. {p.name} - ${p.price}")
    else:
        print("❌ No products found in that category.")

def add_to_cart():
    pid = input("Enter product ID to add to cart: ")
    quantity = int(input("Enter quantity: "))
    
    cart = CartItem(user_id=1, product_id=pid, quantity=quantity)
    session.add(cart)
    session.commit()
    print("✅ Added to cart.")

def view_cart():
    cart_items = session.query(CartItem).filter_by(user_id=1).all()
    print("\n🛒 Your Cart:")
    for item in cart_items:
        product = session.query(Product).get(item.product_id)
        print(f"{product.name} x {item.quantity} = ${product.price * item.quantity:.2f}")

def place_order():
    
    print("🧾 Order placed! (This will be implemented in full logic soon)")

def leave_review():
    pid = input("Enter product ID to review: ")
    rating = int(input("Rating (1-5): "))
    comment = input("Comment: ")

    review = Review(user_id=1, product_id=pid, rating=rating, comment=comment)
    session.add(review)
    session.commit()
    print("✅ Review submitted.")
