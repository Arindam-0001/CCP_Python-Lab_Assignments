# sum of a five digit number
num=int(input("Enter a five digit number: "))
d1=num%10
d2=(num//10)%10
d3=(num//100)%10
d4=(num//1000)%10
d5=(num//10000)%10
sum_digits=d1+d2+d3+d4+d5
print("sum of digits: ",sum_digits)