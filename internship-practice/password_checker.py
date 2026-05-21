import re
import getpass

def check_password_strength(password):
    rules = {
        "length":   len(password) >= 8,
        "upper":    bool(re.search(r'[A-Z]', password)),
        "lower":    bool(re.search(r'[a-z]', password)),
        "digit":    bool(re.search(r'[0-9]', password)),
        "special":  bool(re.search(r'[!@#$%^&*()\-_=+\[\]{};:\'",.<>?/\\|`~]', password)),
    }

    labels = {
        "length":  "At least 8 characters",
        "upper":   "Contains an uppercase letter",
        "lower":   "Contains a lowercase letter",
        "digit":   "Contains a number",
        "special": "Contains a special character (!@#$%^&*...)",
    }

    score = sum(rules.values())

    if score == 1:
        strength = "Very Weak"
    elif score == 2:
        strength = "Weak"
    elif score == 3:
        strength = "Fair"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    is_strong = rules["length"] and score >= 4

    return rules, labels, score, strength, is_strong


def print_results(rules, labels, score, strength, is_strong):
    print("\n" + "=" * 45)
    print("        PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    print("\n  Checklist:")
    for key, passed in rules.items():
        mark = "✓" if passed else "✗"
        print(f"   {mark}  {labels[key]}")

    bar_filled = "█" * score
    bar_empty  = "░" * (5 - score)
    print(f"\n  Strength : {bar_filled}{bar_empty}  {strength}  ({score}/5)")

    print("\n" + "-" * 45)
    if is_strong:
        print("  ✓  STRONG PASSWORD")
    else:
        print("  ✗  WEAK PASSWORD — improve your password!")
    print("=" * 45 + "\n")


def main():
    print("\n========================================")
    print("      PASSWORD STRENGTH CHECKER")
    print("========================================")

    while True:
        try:
            password = getpass.getpass("\n  Enter password (hidden): ")
        except Exception:
            password = input("\n  Enter password: ")

        if not password:
            print("  ⚠  No password entered. Please try again.")
            continue

        rules, labels, score, strength, is_strong = check_password_strength(password)
        print_results(rules, labels, score, strength, is_strong)

        again = input("  Check another password? (y/n): ").strip().lower()
        if again != 'y':
            print("\n  Goodbye!\n")
            break


if __name__ == "__main__":
    main()