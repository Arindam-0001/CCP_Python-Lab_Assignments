
# Function to find the sum of factors of a given number
def sumFactors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total = total + i
    return total

# --- Main program ---
num = int(input("Enter a number: "))
print("Sum of factors of", num, "is:", sumFactors(num))
