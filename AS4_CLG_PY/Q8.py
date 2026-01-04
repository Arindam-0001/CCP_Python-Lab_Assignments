# Prompts five integer and show them into increasing order
num1=int(input("Enter no1: "))
num2=int(input("Enter no2: "))
num3=int(input("Enter no3: "))
num4=int(input("Enter no4: "))
num5=int(input("Enter no5: "))
numbers=[num1,num2,num3,num4,num5]
numbers.sort()
print("All numbers in increasing order ", numbers)
