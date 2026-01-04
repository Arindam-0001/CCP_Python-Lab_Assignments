# Take input from the user
original = input("Enter a five-digit number: ")

# Check if it's a valid five-digit number
if original.isdigit() and len(original) == 5:
    reversed_number = original[::-1]  # Reverse the string
    print("Reversed number:", reversed_number)

    # Compare original and reversed
    if original == reversed_number:
        print("The original and reversed numbers are equal.")
    else:
        print("The original and reversed numbers are NOT equal.")
else:
    print("Invalid input. Please enter a five-digit number.")