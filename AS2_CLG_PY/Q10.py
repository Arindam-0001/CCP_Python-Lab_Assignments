# Initial Deposite value
final_value=eval(input("Enter final account value: "))
rate=eval(input("Enter annual interest rate(%): "))
years=eval(input("Enter numbers of years: "))

monthly_rate=rate/(12*100)
months=years*12
initial_deposit=final_value/((1+monthly_rate)**months)
print("Initial Deposit required:",initial_deposit)