# # Program to find roots using nested if-else

# import math

# # Input coefficients
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))

# # Calculate discriminant
# d = b**2 - 4*a*c

# # Check nature of roots
# if a != 0:
#     if d > 0:
#         root1 = (-b + math.sqrt(d)) / (2*a)
#         root2 = (-b - math.sqrt(d)) / (2*a)
#         print("Roots are real and distinct:")
#         print("Root 1 =", root1)
#         print("Root 2 =", root2)
#     else:
#         if d == 0:
#             root = -b / (2*a)
#             print("Roots are real and equal:")
#             print("Root =", root)
#         else:
#             realPart = -b / (2*a)
#             imagPart = math.sqrt(-d) / (2*a)
#             print("Roots are complex and imaginary:")
#             print("Root 1 =", complex(realPart, imagPart))
#             print("Root 2 =", complex(realPart, -imagPart))
# else:
#     print("This is not a quadratic equation.")


# Program to find roots using elif-else

import math

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate discriminant
d = b**2 - 4*a*c
if d == 0:
    root = -b / (2*a)
    print("Roots are real and equal:")
    print("Root =", root)
elif d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are real and distinct:")
    print("Root 1 =", root1)
    print("Root 2 =", root2)
elif d < 0:
    realPart = -b / (2*a)
    imagPart = math.sqrt(-d) / (2*a)
    print("Roots are complex and imaginary:")
    print("Root 1 =", complex(realPart, imagPart))
    print("Root 2 =", complex(realPart, -imagPart))
else:
    print("This is not a quadratic equation.") 