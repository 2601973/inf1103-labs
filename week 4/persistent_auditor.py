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

def add_product(inventory):
    while True:
        product_id = input(
            "New Product ID (or 'cancel'): "
        ).strip().upper()

        if product_id == "CANCEL":
            return

        if not product_id:
            print("Product ID cannot be empty.")
            continue

        if any(product["id"] == product_id for product in inventory):
            print("That Product ID already exists. Please try again.")
            continue

        break

    while True:
        name = input("Product Name (or 'cancel'): ").strip()

        if name.lower() == "cancel":
            return

        if name:
            break

        print("Product name cannot be empty.")

    while True:
        value = input("Price (or 'cancel'): ").strip()

        if value.lower() == "cancel":
            return

        try:
            price = float(value)
        except ValueError:
            print("Please enter a valid price.")
            continue

        if not 0 <= price < float("inf"):
            print("Please enter a finite, non-negative price.")
            continue

        break

    while True:
        value = input("Stock Quantity (or 'cancel'): ").strip()

        if value.lower() == "cancel":
            return

        try:
            stock = int(value)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if stock < 0:
            print("Stock cannot be negative.")
            continue

        break

    inventory.append({
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock,
    })

    print("Product added successfully!")


add_product(inventory)
update_stock(inventory)
display_all(inventory)

search_product(inventory)