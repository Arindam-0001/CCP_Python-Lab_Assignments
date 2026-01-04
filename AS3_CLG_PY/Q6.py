# Reversed a four digit number
num=input("Enter a four digit number: ")
if len(num)==4 and num.isdigit():
    reversed_num=num[::-1]
    print("Reversed number:", reversed_num)
else:
    print("Invalid input!")