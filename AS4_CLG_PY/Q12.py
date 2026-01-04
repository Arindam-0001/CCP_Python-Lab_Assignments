#   Display Grade 
# Input total marks
marks = float(input("Enter total marks (0–100): "))

# Check and assign grade using if-else
if marks >= 90 and marks <= 100:
    grade = 'O'
elif marks >= 80:
    grade = 'E'
elif marks >= 70:
    grade = 'A'
elif marks >= 60:
    grade = 'B'
elif marks >= 50:
    grade = 'C'
elif marks >= 0:
    grade = 'Fail'
else:
    grade = 'Invalid'
print("Grade is :", grade)