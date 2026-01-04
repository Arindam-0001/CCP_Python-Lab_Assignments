# Area of a pentagon
import math
s=float(input("Enter the side length of the pentagon: "))
area=(5*s**2)/(4*math.tan(math.pi/5))
print(f"Area of the pentagon is :{area:.2f}")