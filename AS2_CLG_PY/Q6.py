# sum of digits in a number
number=eval(input("Enter a no. between 0-1000 : "))
# Extracting digits from the number
d1=number%10
d2=(number//10)%10
d3=(number//100)%10
d4=(number//1000)%10 
digit_sum=d1+d2+d3+d4
print("The sum of digits:",digit_sum)
