
# Project: Simple Banking System (PS-14)
# Name: Saumya sahu
# ERP-ID: RU-26-02462

import json
import os

# Simple Banking System
# Project No. 14
# Minimum Balance: Rs. 500
# Starting Account Number: 1001
# Data File: bank.txt

DATA_FILE = "bank.txt"
MINIMUM_BALANCE = 500
START_ACCOUNT_NUMBER = 1001


# Load account data from file
def load_accounts():
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r") as file:
            accounts = json.load(file)

        if not isinstance(accounts, dict):
            raise ValueError("Invalid bank data format.")

        return accounts

    except json.JSONDecodeError:
        raise ValueError(
            "bank.txt contains invalid data. Please check the file."
        )


# Save account data to file
def save_accounts(accounts):
    with open(DATA_FILE, "w") as file:
        json.dump(accounts, file, indent=4)


# Get a valid positive integer amount
def get_amount(message):
    while True:
        try:
            amount = int(input(message))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount

        except ValueError:
            print("Invalid input! Please enter a valid whole number.")


# Create a new account
def create_account(accounts):
    name = input("Enter customer name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    opening_balance = get_amount("Enter opening deposit: Rs. ")

    if opening_balance < MINIMUM_BALANCE:
        print("Minimum opening balance must be Rs. 500.")
        return

    if accounts:
        account_number = max(int(acc) for acc in accounts) + 1
    else:
        account_number = START_ACCOUNT_NUMBER

    account_number = str(account_number)

    accounts[account_number] = {
        "name": name,
        "balance": opening_balance
    }

    save_accounts(accounts)

    print("\nAccount created successfully!")
    print("A/C No:", account_number)
    print("Balance:", opening_balance)


# Deposit money
def deposit_money(accounts):
    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("Account", account_number, "not found.")
        return

    amount = get_amount("Enter deposit amount: Rs. ")

    accounts[account_number]["balance"] += amount

    save_accounts(accounts)

    print("Deposit successful.")
    print("Updated Balance:",
          accounts[account_number]["balance"])


# Withdraw money
def withdraw_money(accounts):
    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("Account", account_number, "not found.")
        return

    amount = get_amount("Enter withdrawal amount: Rs. ")

    current_balance = accounts[account_number]["balance"]

    if current_balance - amount < MINIMUM_BALANCE:
        print("Withdrawal denied!")
        print("Minimum balance of Rs. 500 must be maintained.")
        return

    accounts[account_number]["balance"] -= amount

    save_accounts(accounts)

    print("Withdrawal successful.")
    print("Balance:", accounts[account_number]["balance"])


# Transfer money
def transfer_money(accounts):
    sender = input("Enter sender account number: ").strip()
    receiver = input("Enter receiver account number: ").strip()

    if sender not in accounts:
        print("Sender account", sender, "not found.")
        print("Transfer cancelled.")
        return

    if receiver not in accounts:
        print("Account", receiver, "not found.")
        print("Transfer cancelled.")
        return

    if sender == receiver:
        print("Cannot transfer money to the same account.")
        print("Transfer cancelled.")
        return

    amount = get_amount("Enter transfer amount: Rs. ")

    sender_balance = accounts[sender]["balance"]

    if sender_balance - amount < MINIMUM_BALANCE:
        print("Transfer denied!")
        print("Minimum balance of Rs. 500 must be maintained.")
        return

    accounts[sender]["balance"] -= amount
    accounts[receiver]["balance"] += amount

    save_accounts(accounts)

    print("Transfer successful.")
    print("Sender Balance:", accounts[sender]["balance"])
    print("Receiver Balance:", accounts[receiver]["balance"])


# Check account balance
def check_balance(accounts):
    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("Account", account_number, "not found.")
        return

    print("\nAccount Number:", account_number)
    print("Account Holder:", accounts[account_number]["name"])
    print("Available Balance:",
          accounts[account_number]["balance"])


# Main menu
def main():
    try:
        accounts = load_accounts()
    except (ValueError, OSError) as error:
        print("Unable to load bank data:", error)
        return

    while True:
        print("\n========== SIMPLE BANKING SYSTEM ==========")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Check Balance")
        print("6. Exit")
        print("===========================================")

        choice = input("Enter your choice (1-6): ").strip()

        try:
            if choice == "1":
                create_account(accounts)

            elif choice == "2":
                deposit_money(accounts)

            elif choice == "3":
                withdraw_money(accounts)

            elif choice == "4":
                transfer_money(accounts)

            elif choice == "5":
                check_balance(accounts)

            elif choice == "6":
                print("Thank you for using Simple Banking System!")
                break

            else:
                print("Invalid choice! Please select 1 to 6.")

        except (OSError, ValueError) as error:
            print("Operation could not be completed:", error)


if __name__ == "__main__":
    main()
