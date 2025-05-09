# promotions.py

from abc import ABC, abstractmethod
from products import Product

class Promotion(ABC):
    """
    Abstract base class for all promotions.
    """
    def __init__(self, name: str):
        if not name or not isinstance(name, str):
            raise ValueError("Promotion name must be a non-empty string.")
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Calculate total price after applying this promotion on `quantity` units of `product`.
        """
        pass


class PercentDiscount(Promotion):
    """
    Applies a percentage discount to every unit.
    E.g. 30% off means you pay 70% of normal price.
    """
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        if not (0 <= percent <= 100):
            raise ValueError("percent must be between 0 and 100")
        self.percent = percent

    def apply_promotion(self, product: Product, quantity: int) -> float:
        full_price = product._price * quantity
        discount = full_price * (self.percent / 100)
        return full_price - discount


class SecondHalfPrice(Promotion):
    """
    Every second item is half price.
    E.g. for quantity=3 you pay: full + half + full = 2.5 × unit price.
    """
    def apply_promotion(self, product: Product, quantity: int) -> float:
        unit = product._price
        pairs, remainder = divmod(quantity, 2)
        # each pair costs 1.5 * unit
        return pairs * (1.5 * unit) + remainder * unit


class ThirdOneFree(Promotion):
    """
    Buy two, get one free: every third item is free.
    E.g. for quantity=4 you pay: 2 full + 1 free + 1 full = 3 × unit price.
    """
    def apply_promotion(self, product: Product, quantity: int) -> float:
        unit = product._price
        triples, remainder = divmod(quantity, 3)
        # each triple costs 2 * unit
        return triples * (2 * unit) + remainder * unit
