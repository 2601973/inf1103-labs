from product import Product
from order_line import OrderLine


class Order:
    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, index: int) -> bool:
        if index < 0 or index >= len(self.__order_lines):
            return False

        self.__order_lines.pop(index)
        return True

    def calculate_total(self) -> float:
        return sum(
            (line.calculate_subtotal() for line in self.__order_lines),
            0.0,
        )

    def display_information(self) -> None:
        print(f"\nOrder: {self.__order_id}")

        if not self.__order_lines:
            print("Order is empty.")

        for index, line in enumerate(self.__order_lines):
            print(f"Line {index}:")
            line.display_information()

        print(f"Order total: ${self.calculate_total():.2f}")

    def get_order_lines(self) -> tuple[OrderLine, ...]:
        return tuple(self.__order_lines)