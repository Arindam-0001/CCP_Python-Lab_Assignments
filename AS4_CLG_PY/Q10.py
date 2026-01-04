# Prompt user to enter an integer
num = int(input("Enter an integer: "))

# Check divisibility using logical operators
if num % 5 == 0 and num % 6 == 0:
    print(f"{num} is divisible by both 5 and 6.")
elif num % 5 == 0 or num % 6 == 0:
    print(f"{num} is divisible by 5 or 6.")
else:
    print(f"{num} is not divisible by either 5 or 6.")