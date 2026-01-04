# Program to find squares of positive integers using continue
n=int(input("Enter how many numbers you want to input: "))
print("Enter the numbers: ")
for i in range(n):
    num=int(input(f"Number {i+1}: "))
    if num<=0:
        print("No square will calculate as it is negative no ")
        continue
    square=num**2
    print(f"Square of {num} is {square}")


