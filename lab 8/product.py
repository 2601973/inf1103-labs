from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        supplier: Supplier,
    ) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__supplier: Supplier = supplier
        self.update_stock(stock)

    def get_product_id(self) -> str:
        return self.__product_id

    def update_stock(self, quantity: int) -> None:
        if type(quantity) is not int:
            raise ValueError("Stock must be a whole number.")

        if quantity < 0:
            raise ValueError("Stock cannot be negative.")

        self.__stock: int = quantity    

    def display_information(self) -> None:
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )

    def to_dict(
        self,
    ) -> dict[str, str | float | int | dict[str, str]]:
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier.to_dict(),
        }
    
    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    def get_supplier(self) -> Supplier:
        return self.__supplier

    def display_supplier_information(self) -> None:
        self.__supplier.display_information()

    def get_price(self) -> float:
        return self.__price
