from typing import List, Tuple

from numpy.ma.core import maximum

from products import Product


class Store:
    """
    Store holds a collection of Product instances and allows operations
    such as adding, removing, querying inventory, and placing orders.
    """
    def __init__(self, products_list: List[Product]) -> None:
        """
        Initialize the store with a list of Product objects.

        Args:
            products_list (List[Product]): Initial inventory of products.
        """
        # Make a shallow copy to avoid external mutations
        self._products: List[Product] = list(products_list)

    def add_product(self, product: Product) -> None:
        """
        Add a new product to the store's inventory.

        Args:
            product (Product): The product to add.
        Raises:
            TypeError: If the argument is not a Product instance.
        """
        if not isinstance(product, Product):
            raise TypeError("add_product expects a Product instance.")
        self._products.append(product)


    def remove_product(self, product: Product) -> None:
        """
        Remove a product from the store's inventory.

        Args:
            product (Product): The product to remove.
        Raises:
            ValueError: If the product is not in inventory.
        """
        try:
            self._products.remove(product)
        except ValueError:
            raise ValueError("Product not found in the store inventory.")

    def get_total_quantity(self) -> int:
        """
        Return the total quantity of all products in the store.

        Returns:
            int: Sum of quantities of all inventory items.
        """
        return sum(prod.get_quantity() for prod in self._products)

    def get_all_products(self) -> List[Product]:
        """
        Retrieve a list of all active products in the store.
        Active means the product's is_active() returns True.

        Returns:
            List[Product]: Active products.
        """
        return [prod for prod in self._products if prod.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Place an order for multiple products.

        Args:
            shopping_list (List[Tuple[Product, int]]): List of (Product, quantity) tuples.
        Returns:
            float: Total cost of the order.
        Raises:
            Exception: Propagates exceptions from Product.buy().
        """
        total_price: float = 0.0
        for item in shopping_list:
            if (not isinstance(item, tuple) or len(item) != 2
                    or not isinstance(item[0], Product)
                    or not isinstance(item[1], int)):
                raise TypeError("Each order item must be a (Product, int) tuple.")
            product, qty = item
            # Product.buy will handle stock and activity checks
            cost = product.buy(qty)
            total_price += cost
        return total_price

    def __str__(self) -> str:
        """
        Return a human-readable summary of the store.

        Includes total products, total quantity, and list of active items.
        """
        lines: List[str] = []
        lines.append(f"Store has {len(self._products)} total products.")
        lines.append(f"Total quantity in inventory: {self.get_total_quantity()}")
        lines.append("Active Products:")
        for prod in self.get_all_products():
            lines.append(f" - {prod}")
        return "\n".join(lines)


if __name__ == "__main__":
    # Example usage and basic smoke test
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        Product("Windows License", price=125),
        Product("shipping", price=10, quantity=250, maximum=1),
    ]
    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())            # Expect 850
    print(best_buy.order([(active_products[0], 1), (active_products[1], 2)]))

