from typing import List, Tuple
from products import Product


class Store:
    def __init__(self, products_list: List[Product]) -> None:
        self._products = list(products_list)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("add_product expects a Product instance.")
        self._products.append(product)

    def remove_product(self, product: Product) -> None:
        try:
            self._products.remove(product)
        except ValueError:
            raise ValueError("Product not found in inventory.")

    def get_total_quantity(self) -> int:
        return sum(prod.quantity for prod in self._products)

    def get_all_products(self) -> List[Product]:
        return [prod for prod in self._products if prod.active]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total = 0.0
        for prod, qty in shopping_list:
            if not isinstance(prod, Product) or not isinstance(qty, int):
                raise TypeError("Order items must be (Product, int) tuples.")
            total += prod.buy(qty)
        return total

    # ——— MAGIC METHODS ———

    def __contains__(self, product: Product) -> bool:
        return product in self._products

    def __add__(self, other: "Store") -> "Store":
        if not isinstance(other, Store):
            return NotImplemented
        # merge product lists; shallow copy
        combined = self._products + other._products
        return Store(combined)

    def __str__(self) -> str:
        lines = [
            f"Store: {len(self._products)} total products, {self.get_total_quantity()} items in stock",
            "Active products:"
        ]
        lines += [f" - {prod}" for prod in self.get_all_products()]
        return "\n".join(lines)

