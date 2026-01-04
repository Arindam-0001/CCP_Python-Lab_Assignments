# GCD and LCM calculation
n1=int(input("Enter first no: "))
n2=int(input("Enter second no: "))
# GCD calculation
for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        gcd=i
print(f"GCD of {n1} and {n2} is {gcd}")
# LCM calculation 
lcm=(n1*n2)//gcd
print(f"LCM of {n1} and {n2} is {lcm}")


# singly LCM calculation
max=max(n1,n2)
while True:
    if max%n1==0 and max%n2==0:
        lcm=max
        break
    max+=1
print(f"LCM of {n1} and {n2} is {lcm}") 
    