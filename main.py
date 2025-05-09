import sys
from typing import List, Tuple

from products import (
    LimitedProduct,
    NonStockedProduct,
    Product,
)
from promotions import (
    PercentDiscount,
    SecondHalfPrice,
    ThirdOneFree,
)
from store import Store


def list_products(store: Store) -> None:
    """Print all active products with their full description."""
    active = store.get_all_products()
    if not active:
        print("No active products in the store.")
        return

    print("\nActive Products:")
    for product in active:
        # __str__ shows full details including promos
        print(f"- {product}")


def show_total(store: Store) -> None:
    """Print total quantity of items in store."""
    total = store.get_total_quantity()
    print(f"\nTotal items in store: {total}")


def handle_order(store: Store) -> None:
    """Interactive flow for building and placing an order."""
    active = store.get_all_products()
    if not active:
        print("No active products available for ordering.")
        return

    print("\nAvailable for Order:")
    for idx, product in enumerate(active, start=1):
        promo = product.get_promotion()
        unit_price = (
            promo.apply_promotion(product, 1)
            if promo
            else product.price
        )
        label = f" [{promo.name}]" if promo else ""
        print(f"{idx}. {product.name} — ${unit_price:.2f}{label}")

    shopping: List[Tuple[Product, int]] = []
    while True:
        choice = input("\nEnter product number to add (or press Enter to finish): ")
        if not choice:
            break

        try:
            index = int(choice) - 1
            selected = active[index]
        except (ValueError, IndexError):
            print("Invalid product number. Please try again.")
            continue

        qty_input = input(f"Enter quantity of '{selected.name}' to purchase: ")
        try:
            quantity = int(qty_input)
        except ValueError:
            print("Quantity must be a positive integer.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        if (
            not isinstance(selected, NonStockedProduct)
            and quantity > selected.get_quantity()
        ):
            available = selected.get_quantity()
            print(f"Only {available} units available. Please enter a smaller amount.")
            continue

        shopping.append((selected, quantity))
        print(f"Added {quantity} × {selected.name} to your cart.")

    if not shopping:
        print("No items were selected for the order.")
        return

    print("\nReviewing your cart:")
    total_cost = 0.0
    for product, qty in shopping:
        try:
            cost = product.buy(qty)
        except Exception as exc:
            print(f"Cannot buy {qty} × {product.name}: {exc}")
            continue

        print(f" - {qty} × {product.name}: ${cost:.2f}")
        total_cost += cost

    print(f"\nOrder complete! Total cost: ${total_cost:.2f}")


def start(store: Store) -> None:
    """Launch the interactive console menu for the store."""
    menu = (
        "\nStore Menu\n"
        "----------\n"
        "1. List all products in store\n"
        "2. Show total amount in store\n"
        "3. Make an order\n"
        "4. Quit"
    )

    actions = {
        1: lambda: list_products(store),
        2: lambda: show_total(store),
        3: lambda: handle_order(store),
    }

    while True:
        print(menu)
        choice = input("\nPlease choose a number (1–4): ")
        try:
            option = int(choice)
        except ValueError:
            print("Invalid input: please enter a number between 1 and 4.")
            continue

        if option == 4:
            print("Exiting… Goodbye!")
            break

        action = actions.get(option)
        if action:
            action()
        else:
            print("Choice must be between 1 and 4. Please try again.")


def main() -> None:
    """Entry point: initializes store inventory and starts the UI."""
    try:
        products_list = [
            Product("MacBook Air M2", price=1450, quantity=100),
            Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            Product("Google Pixel 7", price=500, quantity=250),
            NonStockedProduct("Windows License", price=125),
            LimitedProduct(
                "Shipping", price=10, quantity=250, maximum=1
            ),
        ]
    except ValueError as error:
        print(f"Error creating products: {error}")
        sys.exit(1)

    # Create promotion catalog
    second_half = SecondHalfPrice("Second Half Price!")
    third_free = ThirdOneFree("Third One Free!")
    percent_30 = PercentDiscount("30% Off!", percent=30)

    # Attach promotions
    products_list[0].set_promotion(second_half)
    products_list[1].set_promotion(third_free)
    products_list[3].set_promotion(percent_30)

    store_instance = Store(products_list)
    start(store_instance)


if __name__ == "__main__":
    main()
