# Checking Armstrong number program
num=int(input("Enter a number: "))
digit=len(str(num))
copy=num
sum=0
while copy!=0:
    rem=copy%10
    sum=sum+rem**digit
    copy//=10
if sum==num:
    print(num,"is a Armstrong number")
else:
    print(num,"is not a Armstrong number")
