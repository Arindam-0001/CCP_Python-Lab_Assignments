# # To find the largest number between three numbers

# # Input three numbers
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))

# # Nested if-else to find the largest
# if a >= b:
#     if a > c:
#         largest = a
#     else:
#         largest = c
# else:
#     if b > c:
#         largest = b
#     else:
#         largest = c

# print("The largest number is:", largest)


# To find the largest number between three numbers

# Input three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# using elif-else to find the largest
if a>b and a>c:
    largest=a
elif b>c and b>a:
    largest=b
else:
    largest=c
print("The largest number is:", largest)