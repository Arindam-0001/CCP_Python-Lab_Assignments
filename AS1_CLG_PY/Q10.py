# Displays the average speed in miles per hour
distance_km = 14
time_minutes = 45 + 30/60
time_hours = time_minutes / 60

speed_kmh = distance_km / time_hours
speed_mph = speed_kmh / 1.6

print("Average speed in km/h =",speed_kmh )
print("Average speed in miles/h =",speed_mph ) 