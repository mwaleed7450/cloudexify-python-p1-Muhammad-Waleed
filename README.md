# Personal Expense Tracker

**CloudExify Python Internship — Month 1, Project 1**

## 👤 Student Details
- **Name:** Muhammad Waleed
- **Registration No:** CX-INT-2026-PY-0248

## 📌 Project Description
The Personal Expense Tracker is a command-line Python application that helps
users record, view, and manage their daily expenses. It supports adding
expenses with categories, viewing all expenses in a formatted table,
generating a category-wise spending summary, filtering expenses by category,
deleting expenses, and saving/loading data between sessions using file
handling.

## ⚙️ How to Run the Application
1. Make sure Python 3.x is installed on your system.
2. Clone this repository or download the files.
3. Open a terminal in the project folder.
4. Run the following command:
   ```
   python expense_tracker.py
   ```
5. Follow the on-screen menu (options 1–7) to use the application.

## ✅ Features Implemented
- **Add Expense** — enter description, amount, and category (with validation)
- **View All Expenses** — displays a formatted table with a running total
- **Category Summary** — shows total spending per category with percentages
- **Filter by Category** — view only expenses from a chosen category
- **Delete Expense** — remove an expense by ID with confirmation prompt
- **Save Expenses** — saves all data to `expenses.txt`
- **Load on Startup** — previously saved expenses load automatically
- **Input Validation** — handles invalid numbers, empty lists, and bad menu choices using try/except

## 🗂️ Project Structure
```
expense_tracker/
├── expense_tracker.py     # Main application file
├── expenses.txt            # Data storage file (auto-created)
├── README.md                # This file
└── screenshots/
    ├── main_menu.png
    └── expense_list.png
```

## 📸 Screenshots
See the `screenshots/` folder for:
- Main menu view
- Expense list with 5+ entries

## 🛠️ Concepts Used
Variables & data types, input/output, if/else conditions, while loops,
functions, lists, dictionaries, file handling, string formatting, try/except
error handling.

