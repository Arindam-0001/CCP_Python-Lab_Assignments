# Function to find area of a triangle
def TriangleArea(base, height):
    area = 0.5 * base * height
    return area

# --- Main program ---
b = float(input("Enter base of triangle: "))
h = float(input("Enter height of triangle: "))

print("Area of Triangle =", TriangleArea(b, h))
