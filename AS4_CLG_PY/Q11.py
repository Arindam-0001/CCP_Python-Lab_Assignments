# Input three sides of the triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# First, check if the sides can form a triangle
if a + b > c and b + c > a and c + a > b:
    # Check for equilateral
    if a == b == c:
        print("The triangle is equilateral.")
    # Check for isosceles
    elif a == b or b == c or c == a:
        print("The triangle is isosceles.")
    # Check for right-angled using Pythagoras theorem
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print("The triangle is right-angled.")
    # If none of the above, it's scalene
    else:
        print("The triangle is scalene.")
else:
    print("The given sides do not form a valid triangle.")