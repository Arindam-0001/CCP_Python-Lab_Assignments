# Future investment value
Investment_Amount=eval(input("Enter investment amount: "))
Annual_rate=eval(input("Enter annual interest rate(%): "))
years=eval(input("Enter numbers of years: "))

monthly_rate=Annual_rate/(12*100)
months=years*12

future_value=Investment_Amount*((1+monthly_rate)**months)
print("Future investment value:",future_value)