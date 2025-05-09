from typing import Optional


class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name               # uses property setter
        self.price = price             # uses property setter
        self.quantity = quantity       # uses property setter
        self._active: bool = self.quantity > 0
        self._promotion: Optional["Promotion"] = None

    # ——— PROPERTIES ———

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, val: str) -> None:
        if not isinstance(val, str) or not val.strip():
            raise ValueError("Product name must be a non-empty string.")
        self._name = val

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, val: float) -> None:
        if not isinstance(val, (int, float)) or val < 0:
            raise ValueError("Price must be a non-negative number.")
        self._price = float(val)

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, val: int) -> None:
        if not isinstance(val, int) or val < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        self._quantity = val
        self._active = (val > 0)

    @property
    def active(self) -> bool:
        return self._active

    @property
    def promotion(self) -> Optional["Promotion"]:
        return self._promotion

    def set_promotion(self, promo: Optional["Promotion"]) -> None:
        if promo is not None:
            from promotions import Promotion
            if not isinstance(promo, Promotion):
                raise TypeError("promotion must be a Promotion instance or None")
        self._promotion = promo

    # ——— MAGIC & COMPARISONS ———

    def __str__(self) -> str:
        base = f"{self.name}, Price: ${self.price:.2f}, Qty: {self.quantity}"
        if self.promotion:
            base += f"  ▶ Promo: {self.promotion.name}"
        return base

    def __gt__(self, other: "Product") -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price

    def __lt__(self, other: "Product") -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    # ——— BUSINESS METHODS ———

    def buy(self, quantity: int) -> float:
        if not self.active:
            raise Exception("Cannot buy an inactive product.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")
        if quantity > self.quantity:
            raise ValueError("Not enough items in stock.")

        # price calculation
        if self.promotion:
            total = self.promotion.apply_promotion(self, quantity)
        else:
            total = self.price * quantity

        # reduce stock
        self.quantity = self.quantity - quantity
        return total


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, price, quantity=0)

    @Product.quantity.setter
    def quantity(self, val: int) -> None:
        # ignore any attempts; stay active
        self._quantity = 0
        self._active = True

    def buy(self, quantity: int) -> float:
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int) -> None:
        super().__init__(name, price, quantity)
        if not isinstance(maximum, int) or maximum <= 0:
            raise ValueError("Maximum must be a positive integer.")
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise Exception(f"Cannot buy more than {self.maximum} of '{self.name}' per order.")
        return super().buy(quantity)
