from math import isclose

from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order


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

    # Association: products retain references to their supplier.
    assert laptop.get_supplier() is supplier
    assert ebook.get_supplier() is supplier

    del supplier

    laptop.display_supplier_information()
    ebook.display_supplier_information()
    assert laptop.get_supplier() is ebook.get_supplier()
    print("PASS: Supplier association survives deleting the variable.")

    # Aggregation: the same product can move between inventories.
    inventory_a = Inventory()
    inventory_b = Inventory()

    inventory_a.add_product(laptop)
    assert inventory_a.remove_product("P001")
    assert inventory_a.find_product("P001") is None

    laptop.display_information()
    inventory_b.add_product(laptop)
    assert inventory_b.find_product("P001") is laptop
    assert not inventory_a.remove_product("MISSING")
    print("PASS: Inventory removal does not destroy the product.")

    # Composition: each order creates its own order line.
    order_a = Order("O001")
    order_b = Order("O002")

    order_a.add_order_line(laptop, 2)
    order_b.add_order_line(laptop, 1)

    assert len(order_a.get_order_lines()) == 1
    assert len(order_b.get_order_lines()) == 1

    assert (
        order_a.get_order_lines()[0]
        is not order_b.get_order_lines()[0]
    )
    assert (
        order_a.get_order_lines()[0].get_product()
        is order_b.get_order_lines()[0].get_product()
    )
    print("PASS: Two distinct order lines reference one laptop.")

    # Each line contributes its own subtotal.
    order_a.add_order_line(ebook, 3)
    assert isclose(order_a.calculate_total(), 2459.97)
    assert isclose(order_b.calculate_total(), 1200.0)
    order_a.display_information()

    # The owning order manages removal.
    assert order_a.remove_order_line(0)
    assert isclose(order_a.calculate_total(), 59.97)
    assert isclose(order_b.calculate_total(), 1200.0)
    assert order_b.get_order_lines()[0].get_product() is laptop
    assert not order_a.remove_order_line(99)
    print("PASS: Removing a line leaves the product and other order intact.")

    # Invalid quantities must not create a line.
    previous_count = len(order_b.get_order_lines())

    try:
        order_b.add_order_line(laptop, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("Zero quantity should be rejected.")

    assert len(order_b.get_order_lines()) == previous_count
    print("PASS: Invalid quantity does not add an order line.")

    assert isclose(Order("EMPTY").calculate_total(), 0.0)
    print("\nPASS: All relationship tests passed.")


if __name__ == "__main__":
    main()
    