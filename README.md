# 🛒 Best Buy Store

![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python) ![MIT License](https://img.shields.io/badge/License-MIT-green)

Welcome to **Best Buy Store**, a sleek **terminal-based** shopping system showcasing core OOP principles in Python.

---

## ✨ At a Glance

| 🚀 Component      | 🔍 Description                                      |
| ----------------- | --------------------------------------------------- |
| **Product Class** | - Define items with *name*, *price*, *quantity* 🏷️ |

* Auto-activate/deactivate based on stock levels 🔄 |
  \| **Store Class**   | - Aggregates `Product` objects into inventory 📦
* Add/remove products dynamically ➕➖
* Compute total stock and process multi-item orders 💰 |
  \| **CLI Interface** | - Interactive menu: list products, view total, make orders, quit 🖥️
* Validates input & handles edge cases (invalid input, out-of-stock) 🚨 |
  \| **Style Checks**  | - **pycodestyle** for PEP8 compliance (max length 79) ⚙️                             |

---

## 📂 Project Layout

```text
Best Buy Store/
├── products.py      # Product class: inventory, price, activation logic
├── store.py         # Store class: inventory management, ordering
├── main.py          # Interactive CLI to run the store
└── README.md        # This file: project overview & usage guide
```

---

## ⚡ Quick Start

```bash
# 1. Clone repository
git clone https://github.com/your-username/best-buy-store.git
cd best-buy-store

# 2. (Optional) Create & activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Launch the store
python main.py
```

---

## 🎯 How to Use

When the app starts, you'll see:

```text
Store Menu
----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
```

1. **List Products** 🛍️: Shows active items with price & quantity.
2. **Show Total** 📊: Displays sum of all product quantities.
3. **Make an Order** 🛒:

   * Enter the number corresponding to a product.
   * Specify desired quantity (validated against stock).
   * Repeat until done; press **Enter** to finish.
   * View total cost and watch stock update.
4. **Quit** 🚪: Exit the application.

**Tip:** The system gracefully handles invalid inputs and out-of-stock requests.

---

## 🛠️ Style Checks

Ensure code quality and consistency by running:

```bash
pycodestyle . --max-line-length=79
```

Fix any reported violations to adhere to PEP8 standards.

---

## 🤝 Contributing

1. **Fork** the repo 🔀
2. Create a **feature** branch: `git checkout -b feature/<your-feature>` 🌱
3. **Commit** your changes: `git commit -m "Add <feature>"` 💬
4. **Push**: `git push origin feature/<your-feature>` 📤
5. **PR**: Open a Pull Request for review 🔍

---

## 📜 License

This project is released under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

Developed by **Lina Chioma Anaso** ([chiomalinaanaso@gmail.com](mailto:chiomalinaanaso@gmail.com)) 🎓
