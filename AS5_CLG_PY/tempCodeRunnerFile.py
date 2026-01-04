n=5
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
        for k in range(((5-i)*2)-1):
          print(" ",end=" ")
        if i==5:
            for j in range(4):
                print("*",end=" ")
        else:
            for j in range(i):
                print("*",end=" ")
    print()