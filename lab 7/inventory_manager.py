from file_handling import load_inventory, save_inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

def search_product(inventory):
    print("\nSearch Product")

    while True:
        product_id = input(
            "Enter Product ID (or 'cancel' to go back): "
        ).strip().upper()

        if product_id == "CANCEL":
            return

        product = inventory.search_product(product_id)

        if product is not None:
            print("\nProduct Found")
            product.display_information()
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

        product = inventory.search_product(product_id)

        if product is None:
            print("Product not found. Please try again.")
            continue

        product.display_information()

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

            try:
                product.update_stock(new_stock)
            except ValueError as error:
                print(error)
                continue

            print("Stock updated successfully!")
            return

def add_product(inventory):
    print("\nAdd New Product")

    while True:
        print("1. Physical product")
        print("2. Digital product")

        product_type = input(
            "Choose product type (or 'cancel'): "
        ).strip().lower()

        if product_type == "cancel":
            return

        if product_type in ("1", "2"):
            break

        print("Invalid choice. Please enter 1 or 2.")

    while True:
        product_id = input(
            "New Product ID (or 'cancel'): "
        ).strip().upper()

        if product_id == "CANCEL":
            return

        if not product_id:
            print("Product ID cannot be empty.")
            continue

        if inventory.search_product(product_id) is not None:
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

    if product_type == "1":
        prompt = "Weight in kilograms (or 'cancel'): "
    else:
        prompt = "Download size in megabytes (or 'cancel'): "

    while True:
        value = input(prompt).strip()

        if value.lower() == "cancel":
            return

        try:
            extra_value = float(value)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not 0 < extra_value < float("inf"):
            print("Please enter a finite number greater than zero.")
            continue

        break

    if product_type == "1":
        product = PhysicalProduct(
            product_id, name, price, stock, extra_value
        )
    else:
        product = DigitalProduct(
            product_id, name, price, stock, extra_value
        )

    inventory.add_product(product)

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
            inventory.display_all()
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