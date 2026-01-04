# # Input year
# year = int(input("Enter a year: "))

# # Check leap year using if-elif-else
# if year % 400 == 0:
#     print(year, "is a leap year.")
# elif year % 100 == 0:
#     print(year, "is not a leap year.")
# elif year % 4 == 0:
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.") 


# Input year
year = int(input("Enter a year: "))

# Check leap year using logical operators
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")