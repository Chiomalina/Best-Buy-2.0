from typing import Optional


class Product:
    """
    A base product with stock tracking and optional promotion.
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
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
        self._promotion: Optional["Promotion"] = None
        self.set_quantity(quantity)

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def is_active(self) -> bool:
        return self._active

    def set_quantity(self, quantity: int) -> None:
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        self._quantity = quantity
        self._active = quantity > 0

    def get_quantity(self) -> int:
        # Legacy support
        return self.quantity

    def set_promotion(self, promo: Optional["Promotion"]) -> None:
        if promo is not None:
            from promotions import Promotion
            if not isinstance(promo, Promotion):
                raise TypeError("Promotion must be a Promotion instance or None.")
        self._promotion = promo

    def get_promotion(self) -> Optional["Promotion"]:
        return self._promotion

    def buy(self, quantity: int) -> float:
        if not self.is_active:
            raise Exception("Cannot buy an inactive product.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")
        if quantity > self._quantity:
            raise ValueError("Not enough items in stock.")

        if self._promotion:
            total = self._promotion.apply_promotion(self, quantity)
        else:
            total = self._price * quantity

        self.set_quantity(self._quantity - quantity)
        return total

    def __str__(self) -> str:
        base = f"{self._name}, Price: {self._price:.2f}, Quantity: {self._quantity}"
        if self._promotion:
            base += f" ▶ Promo: {self._promotion.name}"
        return base


class NonStockedProduct(Product):
    """
    A product without stock limits (e.g., software license).
    """

    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, price, quantity=0)
        self._active = True

    def set_quantity(self, quantity: int) -> None:
        _ = quantity  # ignore
        self._quantity = 0
        self._active = True

    def buy(self, quantity: int) -> float:
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")
        if self._promotion:
            return self._promotion.apply_promotion(self, quantity)
        return self._price * quantity

    def __str__(self) -> str:
        base = f"{self._name}, Price: {self._price:.2f} (Non-Stocked)"
        if self._promotion:
            base += f" ▶ Promo: {self._promotion.name}"
        return base


class LimitedProduct(Product):
    """
    A product with a per-order purchase limit.
    """

    def __init__(self, name: str, price: float, quantity: int, maximum: int) -> None:
        super().__init__(name, price, quantity)
        if not isinstance(maximum, int) or maximum <= 0:
            raise ValueError("Maximum must be a positive integer.")
        self._maximum: int = maximum

    @property
    def maximum(self) -> int:
        return self._maximum

    def buy(self, quantity: int) -> float:
        if quantity > self._maximum:
            raise Exception(f"Cannot buy more than {self._maximum} of '{self._name}' per order.")
        return super().buy(quantity)

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} (Max {self._maximum}/order)"
