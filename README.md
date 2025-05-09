<p align="center">
  <img src="https://raw.githubusercontent.com/your-username/best-buy-2.0/main/assets/logo.png" alt="Best Buy 2.0 Logo" width="200"/>
</p>

# Best Buy 2.0  
<p align="center">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/cli-%F0%9F%93%9A-green.svg" alt="CLI">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey.svg" alt="License">
</p>

A sleek, modular **Python** CLI store simulator featuring robust inventory management, dynamic promotions, and modern object-oriented design.

---

## 📑 Table of Contents
- [🔥 Features](#-features)  
- [🛠️ Technologies](#️-technologies)  
- [📂 Project Structure](#-project-structure)   

---

## 🔥 Features
- **Rich Product Hierarchy**:  
  - `Product` with stock tracking & activation  
  - `NonStockedProduct` (e.g. licenses)  
  - `LimitedProduct` with per-order caps  
- **Promotion Engine**:  
  - `PercentDiscount` (e.g. 30% off)  
  - `SecondHalfPrice` (every 2nd item at 50% off)  
  - `ThirdOneFree` (buy 2, get 1 free)  
- **Modern Python**:  
  - `@property` getters/setters  
  - Magic methods: `__str__`, `__gt__`, `__contains__`, `__add__`  
- **Intuitive CLI**:  
  - List products, view totals, and place orders  
  - Real-time price previews with promotions  
  - Line-item cost breakdown on checkout  

---

## 🛠️ Technologies
| Technology   | Purpose                                    |
|--------------|--------------------------------------------|
| Python 3.10+ | Core language & CLI                        |
| pytest       | Automated testing                          |
| abc          | Abstract base classes for Promotion types  |

---

## 📂 Project Structure
```text
best-buy-2.0/
├── main.py           # CLI entry point & user flow
├── products.py       # Product classes & promo integration
├── promotions.py     # Promotion framework & strategies
├── store.py          # Inventory & order management
├── test_product.py   # pytest suite for Product behaviors
├── test_store.py     # sanity-check script for Store magic methods
└── README.md         # Project overview & documentation

