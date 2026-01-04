# Take input from the user
n = int(input("Enter the value of n: "))

# Check if n is a positive number
if n > 0:
    # Sum of first n natural numbers = n * (n + 1) / 2
    total_sum = n * (n + 1) // 2

    # Average = total_sum / n
    average = total_sum / n

    print("The average of first", n, "natural numbers is:", average)
else:
    print("Please enter a positive integer.")  