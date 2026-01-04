# Program to evaluate 1-2+3-4+....+n using for loop
n=100
result=0
for i in range(1,n+1):
    if i%2==0:
        result-=i
    else:
        result+=i
print("Result of series 1-2+3-4+....+100 is:  ",result)
        
