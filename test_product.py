import pytest
from products import Product


def test_create_normal_product():
    """
    Test that creating a product with valid details initializes correctly.
    """
    prod = Product("TestItem", price=10.0, quantity=5)
    assert prod._name == "TestItem"
    assert prod._price == 10.0
    assert prod.get_quantity() == 5
    assert prod.is_active()


def test_create_invalid_product_raises():
    """
    Test that invalid product details raise ValueError.
    """
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_zero_quantity_becomes_inactive():
    """
    Test that setting quantity to zero deactivates the product.
    """
    prod = Product("Sample", price=5.0, quantity=2)
    prod.set_quantity(0)
    assert prod.get_quantity() == 0
    assert not prod.is_active()


def test_purchase_modifies_quantity_and_returns_cost():
    """
    Test that buying a valid quantity updates stock and returns correct cost.
    """
    prod = Product("Book", price=12.5, quantity=4)
    cost = prod.buy(3)
    assert cost == pytest.approx(12.5 * 3)
    assert prod.get_quantity() == 1


def test_buy_more_than_available_raises():
    """
    Test that attempting to buy more than in stock raises ValueError.
    """
    prod = Product("Pen", price=2.0, quantity=2)
    with pytest.raises(ValueError):
        prod.buy(5)
