import json
from pathlib import Path


INVENTORY_FILE = Path(__file__).with_name("inventory.json")


def load_inventory():
    if not INVENTORY_FILE.exists():
        print("inventory.json not found. Starting with empty inventory.")
        return []
    
    print("inventory.json found.")
    with INVENTORY_FILE.open("r", encoding="utf-8") as file:
        inventory = json.load(file)

    print("Inventory loaded successfully.")
    return inventory

def save_inventory(inventory):
    with INVENTORY_FILE.open("w", encoding="utf-8") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json.")

def display_all(inventory):
    if not inventory:
        print("Inventory is empty.")
        return

    print("\nCurrent Inventory")
    print("-" * 48)

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("-" * 48)


def search_product(inventory):
    print("\nSearch Product")
    while True:
        product_id = input(
            "Enter Product ID (or 'cancel' to go back): "
        ).strip().upper()

        if product_id == "CANCEL":
            return

        for product in inventory:
            if product["id"] == product_id:
                print("\nProduct Found")
                print("-" * 48)
                print(f"ID: {product['id']}")
                print(f"Name: {product['name']}")
                print(f"Price: ${product['price']:.2f}")
                print(f"Stock: {product['stock']}")
                print("-" * 48)
                return

        print("Product not found. Please try again.")

def update_stock(inventory):
    print("\nUpdate Stock")
    while True:
        product_id = input(
            "Enter Product ID (or 'cancel' to go back): "
        ).strip().upper()

        if product_id == "CANCEL":
            return

        for product in inventory:
            if product["id"] == product_id:
                print("\nProduct Found:")
                print(f"Name: {product['name']}")
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
    print("\nAdd New Product")
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

def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()
    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        option = input("Enter option: ").strip()

        if option == "1":
            display_all(inventory)
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            search_product(inventory)
        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory)
        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter 1 to 6.")


if __name__ == "__main__":
    main()