# # Function to find the sum of digits in an integer
# def sum_digits():
#     num = int(input("Enter an integer: "))  # User input
#     digit_sum = 0                           # Initialize sum

#     while num > 0:                          # Loop until num becomes 0
#         rem = num % 10                      # Extract last digit
#         digit_sum = digit_sum + rem         # Add to sum
#         num = num // 10                     # Remove last digit

#     print("Sum of digits:", digit_sum)      # Output the result

# sum_digits()                                # Function call


def sumDigits(n):
    digit_sum = 0                           # Initialize sum

    while n > 0:                          # Loop until num becomes 0
        rem = n % 10                      # Extract last digit
        digit_sum = digit_sum + rem         # Add to sum
        n = n // 10                     # Remove last digit

    print("Sum of digits:", digit_sum)      # Output the result

sumDigits(123)                               # Function call
