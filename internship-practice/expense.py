#!/usr/bin/env python3
"""
╔══════════════════════════════════════╗
║       DAILY EXPENSE CALCULATOR       ║
╚══════════════════════════════════════╝
"""

def separator(char="─", width=42):
    print(char * width)

def header():
    print()
    print("╔══════════════════════════════════════════╗")
    print("║       💰  DAILY EXPENSE CALCULATOR  💰   ║")
    print("╚══════════════════════════════════════════╝")
    print()

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("  ⚠️  Please enter a value greater than 0.\n")
            else:
                return value
        except ValueError:
            print("  ⚠️  Invalid input. Please enter a number.\n")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("  ⚠️  Please enter a value greater than 0.\n")
            else:
                return value
        except ValueError:
            print("  ⚠️  Invalid input. Please enter a whole number.\n")

def calculate_expenses(daily_expense, num_days):
    total        = daily_expense * num_days
    weekly_avg   = daily_expense * 7
    monthly_avg  = daily_expense * 30
    yearly_avg   = daily_expense * 365
    return total, weekly_avg, monthly_avg, yearly_avg

def display_results(daily_expense, num_days, total, weekly_avg, monthly_avg, yearly_avg):
    print()
    separator("═")
    print("  📊  EXPENSE SUMMARY REPORT")
    separator("═")

    print(f"  📅  Daily Expense   : ₹ {daily_expense:>10,.2f}")
    print(f"  🔢  Number of Days  : {num_days:>12} days")
    separator()
    print(f"  💸  TOTAL EXPENSE   : ₹ {total:>10,.2f}")
    separator()

    print()
    print("  📈  PROJECTED EXPENSES (based on daily rate)")
    separator("─")
    print(f"  📆  Weekly  (7 days)  : ₹ {weekly_avg:>10,.2f}")
    print(f"  🗓️  Monthly (30 days) : ₹ {monthly_avg:>10,.2f}")
    print(f"  📅  Yearly (365 days) : ₹ {yearly_avg:>10,.2f}")
    separator("═")
    print()

def main():
    header()

    print("  Enter your expense details below:")
    print()

    daily_expense = get_positive_float("  💵  Daily expense amount (₹): ")
    num_days      = get_positive_int  ("  📆  Number of days          : ")

    total, weekly_avg, monthly_avg, yearly_avg = calculate_expenses(daily_expense, num_days)

    display_results(daily_expense, num_days, total, weekly_avg, monthly_avg, yearly_avg)

    # Savings tip
    suggested_savings = total * 0.20
    print(f"  💡  Tip: Save 20% → ₹ {suggested_savings:,.2f} over {num_days} days!")
    print()
    separator("═")
    print("  ✅  Thank you for using the Expense Calculator!")
    separator("═")
    print()

if __name__ == "__main__":
    main()