# Function to convert feet to meters
def footToMeter(foot):
    return 0.305 * foot

# Function to convert meters to feet
def meterToFoot(meter):
    return 3.279 * meter


print("Feet   Meters   |   Meters   Feet")
print("----------------------------------")

foot = 1.0
meter = 20.0

while foot <= 10.0 and meter <= 65.0:
    print(foot, "   ", round(footToMeter(foot), 3), "  |   ",
          meter, "   ", round(meterToFoot(meter), 3))
    foot = foot + 1
    meter = meter + 6
