# Read the value of x
x = float(input("Enter the value of x: "))

# Evaluate y using conditional expression
if x<0:
    y=1
elif x==0:
    y=0
else:
    y=-1

# Display the result
print(f"The value of y is: {y}")