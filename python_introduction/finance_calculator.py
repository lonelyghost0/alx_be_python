monthly_income = int(input("Enter your monthly income:"))
total_monthly = int(input("Enter your total monthly expenses:"))
monthly_saving = monthly_income - total_monthly
Projected_Savings = monthly_saving * 12 + (monthly_saving * 12 * 0.05)
print(f"Your monthly savings are {monthly_saving}")
print (f"Projected savings after one year, with interest, is: {Projected_Savings}")
