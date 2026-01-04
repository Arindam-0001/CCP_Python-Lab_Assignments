# Function to find all factors of a given number
def factors(n):
    factor_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            factor_list.append(i)
    return factor_list

# --- Main program ---
num = int(input("Enter a number: "))
print("Factors of", num, "are:", factors(num))
