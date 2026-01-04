# Program to evaluate y=x^n using loop
x=int(input("Enter the value of x: "))
n=int(input("Enter the value of n(non-negative integer): "))
y=1
for i in range(n):
    y*=x
print(f"{x} ^ {n} = {y}")
