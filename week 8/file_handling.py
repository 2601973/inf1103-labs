import json
from pathlib import Path

from inventory import Inventory
from product import Product


INVENTORY_FILE = Path(__file__).with_name("inventory.json")


def load_inventory(file_path=INVENTORY_FILE):
    file_path = Path(file_path)
    inventory = Inventory()

    if not file_path.exists():
        print("Inventory file not found. Starting with empty inventory.")
        return inventory

    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        product = Product(
            item["id"],
            item["name"],
            item["price"],
            item["stock"],
        )
        inventory.add_product(product)

    print("Inventory loaded successfully.")
    return inventory


def save_inventory(inventory, file_path=INVENTORY_FILE):
    file_path = Path(file_path)

    data = [
        product.to_dict()
        for product in inventory.get_products()
    ]

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully.")