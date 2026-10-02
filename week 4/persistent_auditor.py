inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
]


def display_all(inventory):
    if not inventory:
        print("Inventory is empty.")
        return

    print("\nCurrent Inventory")
    print("-" * 60)

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("-" * 60)


display_all(inventory)

def search_product(inventory):
    while True:
        product_id = input(
            "Enter Product ID (or 'cancel' to go back): "
        ).strip().upper()

        if product_id == "CANCEL":
            return

        for product in inventory:
            if product["id"] == product_id:
                print("\nProduct Found")
                print("-" * 40)
                print(f"ID: {product['id']}")
                print(f"Name: {product['name']}")
                print(f"Price: ${product['price']:.2f}")
                print(f"Stock: {product['stock']}")
                return

        print("Product not found. Please try again.")

def update_stock(inventory):
    while True:
        product_id = input(
            "Enter Product ID (or 'cancel' to go back): "
        ).strip().upper()

        if product_id == "CANCEL":
            return

        for product in inventory:
            if product["id"] == product_id:
                print(f"\nName: {product['name']}")
                print(f"Current Stock: {product['stock']}")

                while True:
                    quantity = input(
                        "New Stock Quantity (or 'cancel'): "
                    ).strip()

                    if quantity.upper() == "CANCEL":
                        return

                    try:
                        new_stock = int(quantity)
                    except ValueError:
                        print("Please enter a whole number.")
                        continue

                    if new_stock < 0:
                        print("Stock cannot be negative.")
                        continue

                    product["stock"] = new_stock
                    print("Stock updated successfully!")
                    return

        print("Product not found. Please try again.")


update_stock(inventory)
display_all(inventory)

search_product(inventory)