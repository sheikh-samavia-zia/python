account_balance = 20000
correct_pin = 1234
pin_attempts_allowed = 3
per_withdrawal_limit = 15000
withdrawn_so_far = 0
is_logged_in = False
history_log = []

# PIN verification
attempts = 0
while attempts < pin_attempts_allowed:
    entered_pin = int(input("Please enter your PIN: "))
    
    if entered_pin == correct_pin:
        is_logged_in = True
        print("PIN verified. Welcome!")
        break
    else:
        attempts += 1
        remaining = pin_attempts_allowed - attempts
        if remaining > 0:
            print(f"Incorrect PIN. {remaining} attempt(s) left.")
        else:
            print("Incorrect PIN.")

if not is_logged_in:
    print("Too many failed attempts. Your card is now blocked.")
else:
    running = True
    while running:
        print("\n--- Welcome to Smart ATM ---")
        print("1) Balance Enquiry")
        print("2) Cash Deposit")
        print("3) Cash Withdrawal")
        print("4) Mini Statement")
        print("5) Quit")

        try:
            menu_pick = int(input("Select an option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if menu_pick == 1:
            print(f"Available balance: ₹{account_balance}")

        elif menu_pick == 2:
            try:
                deposit_amt = int(input("Enter deposit amount: "))
            except ValueError:
                print("Invalid amount.")
                continue
            if deposit_amt <= 0:
                print("Amount must be positive.")
            else:
                account_balance += deposit_amt
                history_log.append(f"Deposited ₹{deposit_amt}")
                print(f"₹{deposit_amt} deposited. New balance: ₹{account_balance}")

        elif menu_pick == 3:
            try:
                withdraw_amt = int(input("Enter withdrawal amount: "))
            except ValueError:
                print("Invalid amount.")
                continue

            if withdraw_amt <= 0:
                print("Amount must be positive.")
            elif withdraw_amt > per_withdrawal_limit:
                print(f"Limit exceeded. Max per transaction: ₹{per_withdrawal_limit}")
            elif withdraw_amt > account_balance:
                print("Not enough balance.")
            else:
                account_balance -= withdraw_amt
                withdrawn_so_far += withdraw_amt
                history_log.append(f"Withdrew ₹{withdraw_amt}")
                print(f"₹{withdraw_amt} dispensed. New balance: ₹{account_balance}")

        elif menu_pick == 4:
            if not history_log:
                print("No transactions yet.")
            else:
                print("--- Transaction History ---")
                for entry in history_log:
                    print(" •", entry)

        elif menu_pick == 5:
            print("Thank you for banking with us. Goodbye!")
            running = False

        else:
            print("Invalid option. Try again.")