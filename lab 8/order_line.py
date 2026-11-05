from product import Product


class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        if type(quantity) is not int:
            raise ValueError("Order quantity must be a whole number.")

        if quantity <= 0:
            raise ValueError("Order quantity must be greater than zero.")

        self.__product: Product = product
        self.__quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    def display_information(self) -> None:
        print(
            f"Product ID: {self.__product.get_product_id()} | "
            f"Quantity: {self.__quantity} | "
            f"Subtotal: ${self.calculate_subtotal():.2f}"
        )