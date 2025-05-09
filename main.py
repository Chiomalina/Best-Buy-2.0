import sys
from typing import List, Tuple

from products import Product, NonStockedProduct, LimitedProduct
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount
from store import Store


def list_products(store: Store) -> None:
    """Print all active products with their full description."""
    products = store.get_all_products()
    if not products:
        print("No active products in the store.")
        return

    print("\nActive Products:")
    for prod in products:
        # show() includes name, price, quantity, and promo
        print(f"- {prod.show()}")


def show_total(store: Store) -> None:
    """Print total quantity of items in store."""
    total = store.get_total_quantity()
    print(f"\nTotal items in store: {total}")


def handle_order(store: Store) -> None:
    """Interactive flow for building and placing an order."""
    active_products = store.get_all_products()
    if not active_products:
        print("No active products available for ordering.")
        return

    print("\nAvailable for Order:")
    for idx, prod in enumerate(active_products, start=1):
        promo = prod.get_promotion()
        unit_price = (
            promo.apply_promotion(prod, 1)
            if promo
            else prod._price
        )
        promo_label = f" [{promo.name}]" if promo else ""
        print(f"{idx}. {prod._name} — unit price: ${unit_price:.2f}{promo_label}")

    shopping_list: List[Tuple[Product, int]] = []
    while True:
        selection = input("\nEnter product number to add (or press Enter to finish): ")
        if not selection:
            break

        try:
            idx = int(selection) - 1
            chosen = active_products[idx]
        except (ValueError, IndexError):
            print("Invalid product number. Please try again.")
            continue

        qty_str = input(f"Enter quantity of '{chosen._name}' to purchase: ")
        try:
            qty = int(qty_str)
        except ValueError:
            print("Quantity must be a positive integer.")
            continue

        if qty <= 0:
            print("Quantity must be greater than zero.")
            continue

        # skip stock check for non‑stocked products
        if not isinstance(chosen, NonStockedProduct) and qty > chosen.get_quantity():
            print(f"Only {chosen.get_quantity()} units available. Please enter a smaller amount.")
            continue

        shopping_list.append((chosen, qty))
        print(f"Added {qty} x {chosen._name} to your cart.")

    if not shopping_list:
        print("No items were selected for the order.")
        return

    print("\nReviewing your cart:")
    total_cost = 0.0
    for item, qty in shopping_list:
        try:
            cost = item.buy(qty)
        except Exception as e:
            print(f"Cannot buy {qty}×{item._name}: {e}")
            continue
        print(f" - {qty}×{item._name}: ${cost:.2f}")
        total_cost += cost

    print(f"\nOrder complete! Total cost: ${total_cost:.2f}")


def start(store_instance: Store) -> None:
    """
    Launch the interactive console menu for the store.
    """
    menu = (
        "\nStore Menu"
        "\n----------"
        "\n1. List all products in store"
        "\n2. Show total amount in store"
        "\n3. Make an order"
        "\n4. Quit"
    )

    actions = {
        1: lambda: list_products(store_instance),
        2: lambda: show_total(store_instance),
        3: lambda: handle_order(store_instance),
    }

    while True:
        print(menu)
        choice_str = input("\nPlease choose a number (1-4): ")
        try:
            choice = int(choice_str)
        except ValueError:
            print("Invalid input: please enter a number between 1 and 4.")
            continue

        if choice == 4:
            print("Exiting... Goodbye!")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Choice must be between 1 and 4. Please try again.")


def main() -> None:
    """
    Entry point: initializes store inventory and starts the UI.
    """
    try:
        product_list = [
            Product("MacBook Air M2", price=1450, quantity=100),
            Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            Product("Google Pixel 7", price=500, quantity=250),
            NonStockedProduct("Windows License", price=125),
            LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
        ]
    except ValueError as error:
        print(f"Error creating products: {error}")
        sys.exit(1)

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half Price!")
    third_one_free    = ThirdOneFree("Third One Free!")
    thirty_percent    = PercentDiscount("30% Off!", percent=30)

    # Attach promotions
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
