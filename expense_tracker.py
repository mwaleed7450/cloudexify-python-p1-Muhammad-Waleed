expenses = []
expense_id = 1  


def add_expense():
    """Add a new expense to the list."""
    global expense_id
    print("\n--- ADD NEW EXPENSE ---")
    description = input("Description: ")

    
    while True:
        try:
            amount = float(input("Amount (PKR): "))
            if amount <= 0:
                print("Amount must be positive!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")

    categories = ["Food", "Transport", "Shopping", "Bills", "Other"]
    print("\nCategories:")
    for i, cat in enumerate(categories, 1):
        print(f" {i}. {cat}")

    while True:
        try:
            choice = int(input("Select category (1-5): "))
            if 1 <= choice <= 5:
                category = categories[choice - 1]
                break
            print("Please select 1-5")
        except ValueError:
            print("Enter a number!")

    expense = {
        "id": expense_id,
        "description": description,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    expense_id += 1
    print(f"\nExpense added! ID: {expense['id']}")


def view_expenses():
    """Display all expenses in a formatted table."""
    if not expenses:
        print("\nNo expenses yet. Add some first!")
        return

    print("\n--- ALL EXPENSES ---")
    print(f"{'ID':<5} {'Description':<20} {'Category':<12} {'Amount':>10}")
    print("-" * 50)

    total = 0
    for exp in expenses:
        print(f"{exp['id']:<5} "
              f"{exp['description']:<20} "
              f"{exp['category']:<12} "
              f"PKR {exp['amount']:>8.2f}")
        total += exp['amount']

    print("-" * 50)
    print(f"{'TOTAL:':<38} PKR {total:>8.2f}")


def category_summary():
    """Show a summary of spending by category with percentages."""
    if not expenses:
        print("\nNo expenses to summarize!")
        return

    summary = {}
    for exp in expenses:
        cat = exp['category']
        if cat in summary:
            summary[cat] += exp['amount']
        else:
            summary[cat] = exp['amount']

    print("\n--- CATEGORY SUMMARY ---")
    total = sum(exp['amount'] for exp in expenses)
    for category, amount in summary.items():
        percent = (amount / total) * 100
        print(f"{category:<12}: PKR {amount:>8.2f} ({percent:.1f}%)")


def filter_by_category():
    """Ask for a category and show only matching expenses with their total."""
    if not expenses:
        print("\nNo expenses to filter!")
        return

    categories = ["Food", "Transport", "Shopping", "Bills", "Other"]
    print("\nCategories:")
    for i, cat in enumerate(categories, 1):
        print(f" {i}. {cat}")

    category_input = input("Enter category name: ").strip().title()

    matches = [exp for exp in expenses if exp['category'] == category_input]

    if not matches:
        print(f"\nNo expenses found in category '{category_input}'.")
        return

    print(f"\n--- EXPENSES IN '{category_input.upper()}' ---")
    print(f"{'ID':<5} {'Description':<20} {'Amount':>10}")
    print("-" * 40)

    total = 0
    for exp in matches:
        print(f"{exp['id']:<5} {exp['description']:<20} PKR {exp['amount']:>8.2f}")
        total += exp['amount']

    print("-" * 40)
    print(f"Total for {category_input}: PKR {total:.2f}")


def delete_expense():
    """Delete an expense by ID after confirmation."""
    if not expenses:
        print("\nNo expenses to delete!")
        return

    view_expenses()

    try:
        target_id = int(input("\nEnter the ID of the expense to delete: "))
    except ValueError:
        print("Please enter a valid numeric ID!")
        return

    # Find the expense with that ID
    target_expense = None
    for exp in expenses:
        if exp['id'] == target_id:
            target_expense = exp
            break

    if target_expense is None:
        print(f"No expense found with ID {target_id}.")
        return

    confirm = input(
        f"Are you sure you want to delete '{target_expense['description']}' "
        f"(PKR {target_expense['amount']:.2f})? (y/n): "
    ).strip().lower()

    if confirm == 'y':
        expenses.remove(target_expense)
        print("Expense deleted successfully!")
    else:
        print("Deletion cancelled.")


def save_expenses():
    """Save all expenses to a text file."""
    with open("expenses.txt", "w") as f:
        for exp in expenses:
            line = (f"{exp['id']},"
                    f"{exp['description']},"
                    f"{exp['amount']},"
                    f"{exp['category']}\n")
            f.write(line)
    print("Expenses saved!")


def load_expenses():
    """Load expenses from the text file, if it exists."""
    global expense_id
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    expense = {
                        "id": int(parts[0]),
                        "description": parts[1],
                        "amount": float(parts[2]),
                        "category": parts[3]
                    }
                    expenses.append(expense)
                    expense_id = int(parts[0]) + 1
    except FileNotFoundError:
        pass  


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print(" CLOUDEXIFY EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category Summary")
    print("4. Filter by Category")
    print("5. Delete Expense")
    print("6. Save Expenses")
    print("7. Save & Exit")
    print("=" * 40)


def main():
    print("Loading saved expenses...")
    load_expenses()
    print(f"Loaded {len(expenses)} expenses.")

    while True:
        show_menu()
        choice = input("Select option (1-7): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            save_expenses()
        elif choice == "7":
            save_expenses()
            print("\nGoodbye! Expenses saved.")
            break
        else:
            print("Invalid choice! Please enter 1-7.")


if __name__ == "__main__":
    main()