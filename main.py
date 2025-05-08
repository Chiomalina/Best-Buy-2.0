import sys
from typing import List, Tuple

from products import Product
from store import Store


def start(store_instance: Store) -> None:
    """
    Launches the interactive console menu for the store.
    Args:
        store_instance (Store): The Store object to interact with.
    """
    menu = (
        "\nStore Menu"
        "\n----------"
        "\n1. List all products in store"
        "\n2. Show total amount in store"
        "\n3. Make an order"
        "\n4. Quit"
    )

    while True:
        print(menu)
        choice_str = input("\nPlease choose a number (1-4): ")

        try:
            choice = int(choice_str)
        except ValueError:
            print("Invalid input: please enter a number between 1 and 4.")
            continue

        if choice == 1:
            # List active products
            products = store_instance.get_all_products()
            if not products:
                print("No active products in the store.")
            else:
                print("\nActive Products:")
                for prod in products:
                    print(f"- {prod._name} | Price: {prod._price} | "
                          f"Quantity: {prod.get_quantity()}")

        elif choice == 2:
            total = store_instance.get_total_quantity()
            print(f"Total items in store: {total}")

        elif choice == 3:
            active_products = store_instance.get_all_products()
            if not active_products:
                print("No active products available for ordering.")
            else:
                print("\nAvailable for Order:")
                for idx, prod in enumerate(active_products, start=1):
                    print(f"{idx}. {prod._name} (Price: {prod._price}, "
                          f"Quantity: {prod.get_quantity()})")

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
                    if qty > chosen.get_quantity():
                        print(f"Only {chosen.get_quantity()} units available. "
                              f"Please enter a smaller amount.")
                        continue

                    # Add to shopping list
                    shopping_list.append((chosen, qty))
                    print(f"Added {qty} x {chosen._name} to your cart.")

                if shopping_list:
                    try:
                        total_cost = store_instance.order(shopping_list)
                        print(f"\nOrder complete! Total cost: ${total_cost:.2f}")
                    except Exception as error:
                        print(f"Error processing order: {error}")
                else:
                    print("No items were selected for the order.")

        elif choice == 4:
            print("Exiting... Goodbye!")
            break

        else:
            print("Choice must be between 1 and 4. Please try again.")


def main() -> None:
    """
    Entry point: initializes store inventory and starts the UI.
    """
    try:
        initial_products = [
            Product("MacBook Air M2", price=1450, quantity=100),
            Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            Product("Google Pixel 7", price=500, quantity=250),
        ]
    except ValueError as error:
        print(f"Error creating products: {error}")
        sys.exit(1)

    best_buy = Store(initial_products)
    start(best_buy)


if __name__ == "__main__":
    main()
