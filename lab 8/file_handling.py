import json
from pathlib import Path

from inventory import Inventory
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


INVENTORY_FILE = Path(__file__).with_name("inventory.json")


def load_inventory(
    file_path: str | Path = INVENTORY_FILE,
) -> Inventory:
    file_path = Path(file_path)
    inventory = Inventory()
    suppliers: dict[str, Supplier] = {}

    if not file_path.exists():
        print("Inventory file not found. Starting with empty inventory.")
        return inventory

    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        supplier_data = item.get("supplier")

        if supplier_data is None:
            supplier_data = {
                "supplier_id": "SAMPLE001",
                "name": "Sample Supplier",
                "contact_email": "supplier@example.com",
            }

        supplier_id = supplier_data["supplier_id"]

        if supplier_id not in suppliers:
            suppliers[supplier_id] = Supplier(
                supplier_id,
                supplier_data["name"],
                supplier_data["contact_email"],
            )

        supplier = suppliers[supplier_id]
        product_type = item.get("type")

        if product_type == "physical":
            product = PhysicalProduct(
                item["id"],
                item["name"],
                item["price"],
                item["stock"],
                item["weight"],
                supplier,
            )
        elif product_type == "digital":
            product = DigitalProduct(
                item["id"],
                item["name"],
                item["price"],
                item["stock"],
                item["download_size"],
                supplier,
            )
        else:
            raise ValueError(
                f"Unknown or missing product type: {product_type}"
            )

        inventory.add_product(product)

    print("Inventory loaded successfully.")
    return inventory


def save_inventory(
    inventory: Inventory,
    file_path: str | Path = INVENTORY_FILE,
) -> None:
    file_path = Path(file_path)

    data = [
        product.to_dict()
        for product in inventory.get_products()
    ]

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully.")