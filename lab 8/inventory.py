from product import Product


class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        product_id = product.get_product_id()

        if self.find_product(product_id) is not None:
            raise ValueError("That Product ID already exists.")

        self.__products.append(product)

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def search_product(self, product_id: str) -> Product | None:
        return self.find_product(product_id)

    def remove_product(self, product_id: str) -> bool:
        product = self.find_product(product_id)

        if product is None:
            return False

        self.__products.remove(product)
        return True

    def display_all(self) -> None:
        if not self.__products:
            print("Inventory is empty.")
            return

        print("\nCurrent Inventory")
        print("-" * 48)

        for product in self.__products:
            product.display_information()

        print("-" * 48)

    def get_products(self) -> list[Product]:
        return self.__products.copy()