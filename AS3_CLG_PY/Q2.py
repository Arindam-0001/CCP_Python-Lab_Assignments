# Calculate the great circle distance
import math

# input in degrees
lat1=float(input("Enter latitude of point1(degrees): "))
long1=float(input("Enter longitude of point1(degrees): "))
lat2=float(input("Enter latitude of point2(degrees): "))
long2=float(input("Enter longitude of point2(degrees): "))

# Convert to radians
x1=math.radians(lat1)
y1=math.radians(long1)
x2=math.radians(lat2)
y2=math.radians(long2)

# radius of earth
radius=6371.01

# Great circle distance formula
distance=radius*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))

print(f"The great circle distance(km) is: {distance:.2f}")