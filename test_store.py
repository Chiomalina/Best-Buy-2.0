# test_store.py

from products import Product
from store import Store

def run_sanity_checks():
    mac   = Product("MacBook Air M2", 1450, 100)
    bose  = Product("Bose Earbuds", 250, 500)
    pixel = Product("Pixel 7", 500, 250)

    best = Store([mac, bose])
    print(mac > bose)        # True
    print(mac < bose)        # False
    print(mac in best)       # True
    print(pixel in best)     # False

    best2 = Store([pixel])
    merged = best + best2
    print("\nMerged store:")
    print(merged)

if __name__ == "__main__":
    run_sanity_checks()
