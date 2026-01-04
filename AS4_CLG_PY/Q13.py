# Input three edges
a = float(input("Enter edge a: "))
b = float(input("Enter edge b: "))
c = float(input("Enter edge c: "))

# Check for triangle validity
if a + b > c and b + c > a and c + a > b:
    perimeter = a + b + c
    print(f"The triangle is valid. Perimeter = {perimeter}")
else:
    print("Invalid input. The edges do not form a triangle.")