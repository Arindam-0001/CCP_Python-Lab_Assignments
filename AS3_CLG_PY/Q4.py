# Area of a regular polygon
import math
n=int(input("Enter number of sides:"))
s=float(input("Enter the length of a side: "))
area=(n*s**2)/(4*math.tan(math.pi/n))
print(f"Area of the polygon is :{area:.2f}")