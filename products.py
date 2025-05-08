# products.py

class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Create a Product with a name, unit price, and initial quantity.
        Raises ValueError if name is empty or price/quantity are negative.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name must be a non-empty string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        self._name: str = name
        self._price: float = float(price)
        self._quantity: int = 0
        self._active: bool = False

        # Use the setter logic to initialize quantity & active state
        self.set_quantity(quantity)

    def get_quantity(self) -> int:
        """Return how many units of this product are currently in stock."""
        return self._quantity

    def is_active(self) -> bool:
        """Return True if this product is active (available for purchase)."""
        return self._active

    def activate(self) -> None:
        """Mark the product as active."""
        self._active = True

    def deactivate(self) -> None:
        """Mark the product as inactive."""
        self._active = False

    def set_quantity(self, quantity: int) -> None:
        """
        Update the stock level.
        Raises ValueError if quantity is negative.
        Deactivates the product if quantity == 0, otherwise activates it.
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        self._quantity = quantity
        if quantity > 0:
            self.activate()
        else:
            self.deactivate()

    def show(self) -> str:
        """Return a human-readable description of this product."""
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}"

    def buy(self, quantity: int) -> float:
        """
        Purchase a given number of items.
        Raises Exception if the product is inactive.
        Raises ValueError if the requested quantity is invalid or exceeds stock.
        Returns the total cost as float.
        """
        if not self.is_active():
            raise Exception("Cannot buy an inactive product.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")
        if quantity > self._quantity:
            raise ValueError("Not enough items in stock.")

        total_price = self._price * quantity
        # Deduct from stock and adjust active flag if needed
        self.set_quantity(self._quantity - quantity)
        return total_price

    def __str__(self) -> str:
        return self.show()
