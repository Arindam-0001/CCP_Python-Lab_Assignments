# Given sides a,b,c of triangle, calculate angles(rounded to neares integer)
import math
a=float(input("Enter side a: "))
b=float(input("Enter side b: "))
c=float(input("Enter side c: "))

# Use cosine law:
A=math.acos((b**2+c**2-a**2)/(2*b*c))
B=math.acos((a**2+c**2-b**2)/(2*a*c))
C=math.acos((a**2+b**2-c**2)/(2*a*b))

# Converts radians to degrees
A_deg=round(math.degrees(A))
B_deg=round(math.degrees(B))
C_deg=round(math.degrees(C))

print("Angles of triangle(rounded):")
print("Angle A: ",A_deg)
print("Angle B: ",B_deg)
print("Angle C: ",C_deg)