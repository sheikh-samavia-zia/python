def calculate_bonus(salary):
    if salary >= 50000:
        bonus = salary * 0.20
    else:
        bonus = salary * 0.10
    return bonus


def calculate_tax(total_salary):
    if total_salary >= 60000:
        tax = 2000
    else:
        tax = 0
    return tax


def salary_calculator(base_salary):
    bonus = calculate_bonus(base_salary)
    total_salary = base_salary + bonus
    tax = calculate_tax(total_salary)
    salary_after_tax = total_salary - tax
    return {
        "Base Salary": base_salary,
        "Bonus": bonus,
        "Total Salary": total_salary,
        "Tax": tax,
        "Salary After Tax": salary_after_tax,
    }


if __name__ == "__main__":
    salary = float(input("Enter base salary: "))
    result = salary_calculator(salary)
    print("\n--- Salary Breakdown ---")
    for key, value in result.items():
        print(f"{key}: {value:,.2f}")
