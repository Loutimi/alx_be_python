monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - total_monthly_expenses
simple_interest = monthly_income * 0.005 * 12
projected_savings = monthly_savings * 12 * (1 + 0.05)
print(f"Your monthly savings are ${int(monthly_savings)}")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}")
