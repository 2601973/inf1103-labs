from product import Product
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


def check_stock_contract(product: Product) -> None:
    product.update_stock(0)
    assert product.to_dict()["stock"] == 0

    product.update_stock(10)
    assert product.to_dict()["stock"] == 10

    try:
        product.update_stock(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative stock should be rejected.")

    assert product.to_dict()["stock"] == 10


def main() -> None:
    supplier = Supplier(
        "S001", "Tech Supplies", "sales@example.com"
    )

    laptop = PhysicalProduct(
        "P001", "Laptop", 1200.0, 15, 2.5, supplier
    )

    ebook = DigitalProduct(
        "D001", "Python eBook", 19.99, 100, 8.5, supplier
    )

    inventory = Inventory()
    inventory.add_product(laptop)
    inventory.add_product(ebook)

    for product in inventory.get_products():
        show_product_details(product)
        check_stock_contract(product)
        print("PASS: Product preserves the stock-update contract.")
        print()

    print("PASS: Both product types work through Product references.")


if __name__ == "__main__":
    main()