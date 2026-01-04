# Display area of a triangle

# Input coordinates
x1=eval(input("Enter x1: "))
y1=eval(input("Enter y1: "))

x2=eval(input("Enter x2: "))
y2=eval(input("Enter y2: "))

x3=eval(input("Enter x3: "))
y3=eval(input("Enter y3: "))

# calculation side length
s1=  (((x2-x1)**2+(y2-y1)**2))**0.5
s2=  (((x3-x2)**2+(y3-y2)**2))**0.5
s3=  (((x1-x3)**2+(y1-y3)**2))**0.5

# calculate semi perimeter
s=(s1+s2+s3)/2

# Area using Heron's formula
area=((s*(s-s1)*(s-s2)*(s-s3)))**0.5
print("Area of triangle is: ",area)