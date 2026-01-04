# Energy required to heat water
M=eval(input("Enter amount of water in kg: "))
initial_temp=eval(input("Enter initial temperature: "))
final_temp=eval(input("Enter final temperature: "))
Q=M*(final_temp-initial_temp)*4184
print("Energy required (in joules): ",Q)