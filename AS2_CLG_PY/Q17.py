# Sum of first and last digit of a six digit number
num=int(input("Enter a six digit number: "))
first_digit=num//100000
last_digit=num%10
digit_sum=first_digit+last_digit
print("sum of first and last digit is: ",digit_sum)