# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero not allowed!"

# --- Main program ---
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Addition =", add(x, y))
print("Subtraction =", subtract(x, y))
print("Multiplication =", multiply(x, y))
print("Division =", divide(x, y))
