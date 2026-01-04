# Calculating area and volume of a cylinder
radius=eval(input("Enter radius of a cylinder:"))
length=eval(input("Enter length of a cylinder:"))
pi=3.14159
# compute area and volume  of a cylinder
Area=radius*radius*pi
volume=Area*length
print(f"The area of the cylinder is {Area} and volume is {volume}")