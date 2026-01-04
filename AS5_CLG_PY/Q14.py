# Program to calculate sum and average of nonnegative numbers using break
n=int(input("Enter how many numbers: "))
numbers=[]
print("Enter the numbers in the list(enter a negative numbers to stop): ")
for i in range(n):
    num=int(input(f"Number {i+1}: "))
    if num<0:
        break
    numbers.append(num)
print(numbers)
# Calculate sum and average
if len(numbers)>0:
    total = sum(numbers)
    avg = total/len(numbers)
    print("Sum of nonnegative numbers: ",total)
    print("Average of nonnegative numbers: ",avg)
else:
    print("No nonnegative numbers entered")