# promotions.py

from abc import ABC, abstractmethod
from products import Product


class Promotion(ABC):
    """
    Abstract base class for all promotions.
    """
    def __init__(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError(
                "Promotion name must be a non-empty string."
            )
        self._name: str = name

    @property
    def name(self) -> str:
        """Return the promotion name."""
        return self._name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Calculate total price after applying promotion on
        'quantity' units of 'product'.
        """
        ...


class PercentDiscount(Promotion):
    """
    Applies a percentage discount to every unit.
    E.g. 30%% off means you pay 70%% of normal price.
    """
    def __init__(self, name: str, percent: float) -> None:
        super().__init__(name)
        if not isinstance(percent, (int, float)):
            raise TypeError("Percent must be a number.")
        if percent < 0 or percent > 100:
            raise ValueError("Percent must be between 0 and 100.")
        self._percent: float = float(percent)

    def apply_promotion(self, product: Product, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError(
                "Quantity must be a positive integer."
            )
        full_price = product.price * quantity
        discount = full_price * (self._percent / 100)
        return full_price - discount


class SecondHalfPrice(Promotion):
    """
    Every second item is half price.
    """
    def apply_promotion(self, product: Product, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError(
                "Quantity must be a positive integer."
            )
        unit_price = product.price
        pairs, remainder = divmod(quantity, 2)
        # each pair costs 1.5 * unit_price
        return pairs * (1.5 * unit_price) + remainder * unit_price


class ThirdOneFree(Promotion):
    """
    Buy two, get one free: every third item is free.
    """
    def apply_promotion(self, product: Product, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError(
                "Quantity must be a positive integer."
            )
        unit_price = product.price
        triples, remainder = divmod(quantity, 3)
        # each triple costs 2 * unit_price
        return triples * (2 * unit_price) + remainder * unit_price
