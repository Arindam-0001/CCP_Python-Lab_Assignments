# Reverse four digit integer
num=int(input("Enter a four digit number: "))
d1=num%10
d2=(num//10)%10
d3=(num//100)%10
d4=(num//1000)
reversed_num=d1*1000+d2*100+d3*10+d4
print("Reversed number: ",reversed_num)