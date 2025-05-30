import json
from database import session, engine
from models import Base, Product, User

Base.metadata.create_all(engine)

with open('db.json') as f:
    data = json.load(f) # load data from the Json fie 


for user_data in data.get("users", []):
    user = User(
        id=user_data["id"],
        username = user_data['username'],
        email= user_data['email'],
        password=user_data['password'],
        is_admin = user_data.get('isadmin', False),
        avatar_url = user_data.get("avatar_url", "")
    )
    session.merge(user)

for product_data in data.get('products', []):

    images = product_data.get("images", [])
    image = images[0] if images else "https://via.placeholder.com/150"

    product = Product(
        id=product_data["id"],
        name=product_data["name"],
        price=product_data["price"],
        image=image,
        category=product_data["category"],
        stock=product_data["stock"],
        description=product_data["description"]
    )

    session.merge(product)

session.commit()
session.close()