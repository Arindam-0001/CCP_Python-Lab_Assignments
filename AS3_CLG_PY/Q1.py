# Computing the area of a pentagon 
import math
length=float(input("Enter the length from the center of a pentagon to a vertex(r): "))
Side=2*length*(math.sin(math.pi/5))
print(f"The side of the pentagon is: {Side:.2f}")
Area=(3*(math.sqrt(3))/2)*(Side*Side)
print(f"The area of the pentagon is: {Area:.2f}")
