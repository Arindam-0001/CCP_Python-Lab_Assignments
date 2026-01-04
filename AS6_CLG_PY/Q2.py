# # Program to reverse an integer

# # Method 1: Using string slicing
# def reverse_str():
#     num = int(input("Enter an integer: "))
#     if num < 0:
#         rev = -int(str(abs(num))[::-1])
#     else:
#         rev = int(str(num)[::-1])
#     print("Reversed number (Method 1):", rev)

# # Method 2: Using while loop
# def reverse_loop():
#     num = int(input("Enter an integer: "))
#     n = abs(num)
#     rev = 0

#     while n > 0:
#         rem = n % 10
#         rev = rev * 10 + rem
#         n = n // 10

#     if num < 0:
#         rev = -rev
#     print("Reversed number (Method 2):", rev)

# # Call both methods
# reverse_str()
# reverse_loop()


def reverse(number):
    rev = 0
    while number > 0:
        rem = number % 10       # Get last digit
        rev = rev * 10 + rem    # Add to reversed number
        number = number // 10   # Remove last digit
    print(rev)

reverse(123)
