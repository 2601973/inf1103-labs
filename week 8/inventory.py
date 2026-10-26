class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        product_id = product.get_product_id()

        if self.search_product(product_id) is not None:
            raise ValueError("That Product ID already exists.")

        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return

        print("\nCurrent Inventory")
        print("-" * 48)

        for product in self.__products:
            product.display_information()

        print("-" * 48)