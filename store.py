from typing import List, Tuple

from products import Product


class Store:
    """
    Holds a collection of Product instances and supports
    inventory operations, ordering, and useful operator overloads.
    """

    def __init__(self, products_list: List[Product]) -> None:
        self._products: List[Product] = list(products_list)

    def add_product(self, product: Product) -> None:
        """Add a product to inventory."""
        if not isinstance(product, Product):
            raise TypeError("add_product expects a Product instance.")
        self._products.append(product)

    def remove_product(self, product: Product) -> None:
        """Remove a product from inventory."""
        try:
            self._products.remove(product)
        except ValueError:
            raise ValueError("Product not found in inventory.")

    def get_total_quantity(self) -> int:
        """Return total quantity across all products."""
        return sum(prod.quantity for prod in self._products)

    def get_all_products(self) -> List[Product]:
        """
        Return a list of all active (in‑stock) products.
        """
        return [prod for prod in self._products if prod._active]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Place an order of (Product, quantity) items.
        Returns total cost.
        """
        total: float = 0.0
        for item in shopping_list:
            prod, qty = item
            if not isinstance(prod, Product) or not isinstance(qty, int):
                raise TypeError("Order items must be (Product, int) tuples.")
            total += prod.buy(qty)
        return total

    # --------------------------------------------------------------------
    # Magic methods
    # --------------------------------------------------------------------

    def __contains__(self, product: Product) -> bool:
        """
        Enable `product in store` syntax.
        """
        return product in self._products

    def __add__(self, other: "Store") -> "Store":
        """
        Merge two stores with `store1 + store2`, returning a new Store.
        """
        if not isinstance(other, Store):
            return NotImplemented
        merged_list = self._products + other._products
        return Store(merged_list)

    def __str__(self) -> str:
        """
        Human-readable summary of the store and its active products.
        """
        header = (
            f"Store: {len(self._products)} total products, "
            f"{self.get_total_quantity()} items in stock"
        )
        lines = [header, "Active products:"]
        for prod in self.get_all_products():
            lines.append(f" - {prod}")
        return "\n".join(lines)
