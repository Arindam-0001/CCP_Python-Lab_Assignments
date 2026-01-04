#  Conversion minutes to years & days
minutes= eval(input("Enter number of minutes: "))
days=minutes//(60*24)
years=days//365
reamining_days=days%365
print(f"{minutes} minutes is approximately {years} years and {reamining_days} days")