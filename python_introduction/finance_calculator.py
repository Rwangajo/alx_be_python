monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

Monthly_savings = monthly_income - monthly_expenses
Projected_Savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)

print("Your monthly savings are ", Monthly_savings)
print("Projected savings after one year, with interest, is:", Projected_Savings)
