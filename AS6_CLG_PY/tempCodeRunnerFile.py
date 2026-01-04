# Function to convert Celsius to Fahrenheit
def celsiusToFahrenheit(c):
    return (9/5) * c + 32

# Function to convert Fahrenheit to Celsius
def fahrenheitToCelsius(f):
    return (5/9) * (f - 32)

print("Celsius   Fahrenheit   |   Fahrenheit   Celsius")
print("------------------------------------------------")

c = 40.0
f = 120.0

while c >= 31.0 and f >= 30.0:
    print(c, "      ", round(celsiusToFahrenheit(c), 1),
          "   |     ", f, "      ", round(fahrenheitToCelsius(f), 2))
    c = c - 1
    f = f - 10
