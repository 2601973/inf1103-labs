import json
from pathlib import Path

from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


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
        product_type = item.get("type")

        if product_type == "physical":
            product = PhysicalProduct(
                item["id"],
                item["name"],
                item["price"],
                item["stock"],
                item["weight"],
            )
        elif product_type == "digital":
            product = DigitalProduct(
                item["id"],
                item["name"],
                item["price"],
                item["stock"],
                item["download_size"],
            )
        else:
            raise ValueError(
                f"Unknown or missing product type: {product_type}"
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