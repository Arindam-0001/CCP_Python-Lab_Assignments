# Function to find number of days in a year
def numberOfDaysInAYear(year):
    # Leap year check: divisible by 4 but not by 100, unless also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 366
    else:
        return 365

# --- Main program ---
print("Year   Days")
print("-------------")

for y in range(2010, 2021):   # from 2010 to 2020
    print(y, "   ", numberOfDaysInAYear(y))
