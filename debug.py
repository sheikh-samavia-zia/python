# Exercise 1: Student Grade Checker
# 4 syntax/indentation errors
def check_grade(marks):

    if marks >= 80:
        print("Grade A")

    elif marks >= 60:
        print("Grade B")

    else:
        print("Grade C")


check_grade(75)

# Exercise 2: Shopping Bill Calculator
# 4 syntax/indentation error

prices = [200, 450, 150, 300]
total = 0

for price in prices:
    total = total + price

if total > 1000:
    print("Discount Applied")
    total = total - 100

else:
    print("No Discount")

print("Final Bill:", total)

# Exercise 3: Employee Salary Calculator
# 4 syntax/indentation errors


def calculate_salary(salary, bonus):
    final_salary = salary + bonus
    if final_salary > 50000:
        print("High Salary")
    else:
        print("Normal Salary")
    return final_salary


result = calculate_salary(40000, 5000)
print(result)

# Exercise 4: Even and Odd Number Counter
# 4 syntax/indentation errors

numbers = [10, 15, 22, 33, 40]
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if even_count > odd_count:
    print("More Even Numbers")

else:
    print("More Odd Numbers")

print("Even:", even_count)
print("Odd:", odd_count)


# Exercise 5
def withdraw(balance, amount):
    if amount <= 0:
        print("Invalid Amount")
    elif amount > balance:
        print("Insufficient Balance")
    else:
        balance = balance - amount
        print("Withdrawal Successful")

    return balance


account_balance = 10000

for amount in [2000, 3000, 6000]:
    account_balance = withdraw(account_balance, amount)

print("Remaining Balance:", account_balance)
