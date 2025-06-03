from helpers_user import (
    welcome_shopper,
    browse_products,
    view_product_details,
    search_by_category,
    add_to_cart,
    view_cart,
    place_order,
    leave_review
)

def run_user_cli():
    welcome_shopper()

    while True:
        print("\n🛒 What would you like to do?")
        print("1. Browse products")
        print("2. View product details")
        print("3. Search by category")
        print("4. Add product to cart")
        print("5. View cart")
        print("6. Place order")
        print("7. Leave a review")
        print("8. Exit")

        choice = input("👉 Enter your choice: ")

        if choice == "1":
            browse_products()
        elif choice == "2":
            view_product_details()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            add_to_cart()
        elif choice == "5":
            view_cart()
        elif choice == "6":
            place_order()
        elif choice == "7":
            leave_review()
        elif choice == "8":
            print("👋 Thanks for shopping with Shelcy!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == '__main__':
    run_user_cli()
