#  # A) Print the following pattern
# # $ $ $ $ $ 
# # $ $ $ $ $
# # $ $ 0 $ $
# # $ $ $ $ $
# # $ $ $ $ $

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==j==3):
#             print("0",end=" ")
#         else:
#             print("$",end=" ")
#     print()


# # B) Print the following pattern
# # $  $  $  $  $  
# # $           $
# # $           $
# # $           $
# # $  $  $  $  $

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==1 or i==5 or j==5 or j==1):
#             print("$ ",end=" ")
#         else:
#             print("  ",end=" ")
#     print()


# # C) Print the following pattern
# # $  $  $  $  $  
# #          $
# #       $
# #    $
# # $

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==1 or i+j==6):
#             print("$ ",end=" ")
#         else:
#             print("  ",end=" ")
#     print()


# # D) Print the following pattern
# # *  
# # *  *
# # *  *  *
# # *  *  *  *
# # *  *  *  *  *

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#             print("* ",end=" ")
#     print()


# # E) Print the following pattern
# # *  *  *  *  *  
# # *  *  *  *
# # *  *  *
# # *  *
# # *
 
# # # method-1:
# # n=5
# # for i in range(n,0,-1):
# #     for j in range(1,i+1):
# #             print("* ",end=" ")
# #     print()

# # method-2:
# n=5
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#             print("* ",end=" ")
#     print()


# # F) Print the following pattern
# #             *  
# #          *  *
# #       *  *  *
# #    *  *  *  *
# # *  *  *  *  *

# n=5
# for i in range(1,n+1):
#     for k in range(1,n+1-i):
#           print("  ",end=" ")
#     for j in range(1,i+1):
#             print("* ",end=" ")
#     print()


# # G) Print the following pattern
# # *  *  *  *  *  
# #    *  *  *  *
# #       *  *  *
# #          *  *
# #             *

# n=5
# for i in range(n,0,-1):
#     for k in range(1,n+1-i):
#           print("  ",end=" ")
#     for j in range(1,i+1):
#             print("* ",end=" ")
#     print()


# # H) Print the following pattern
# #            *  
# #          *  *  *
# #       *  *  *  *  *
# #    *  *  *  *  *  *  *
# # *  *  *  *  *  *  *  *  *

# n=5
# for i in range(1,n+1):
#     for k in range(1,n+1-i):
#           print("  ",end=" ")
#     for j in range(1,(2*i-1)+1):
#             print("* ",end=" ")
#     print()


# # I) Print the following pattern
# # *  *  *  *  *  *  *  *  *  
# #    *  *  *  *  *  *  *  
# #       *  *  *  *  *  
# #          *  *  *  
# #             *  

# n=5
# for i in range(n,0,-1):
#     for k in range(1,n+1-i):
#           print("  ",end=" ")
#     for j in range(1,(2*i-1)+1):
#             print("* ",end=" ")
#     print()


# # J) Print the following pattern
# # *  
# # *  *
# # *  *  *
# # *  *  *  *
# # *  *  *
# # *  *
# # *

# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#             print("* ",end=" ")
#     print()
# n=3
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#             print("* ",end=" ")
#     print() 


# # K) Print the following pattern
# #          *  
# #       *  *
# #    *  *  *
# # *  *  *  *
# #    *  *  *
# #       *  *
# #          *

# n=4
# for i in range(1,n+1):
#     for k in range(1,n+1-i):
#           print("  ",end=" ")
#     for j in range(1,i+1):
#             print("* ",end=" ")
#     print()
# n=3
# for i in range(n,0,-1):
#     for k in range(0,n+1-i):
#           print("  ",end=" ")
#     for j in range(1,i+1):
#             print("* ",end=" ")
#     print()


# # L) Print the following pattern
# #          *  
# #       *  *  *
# #    *  *  *  *  *
# # *  *  *  *  *  *  *
# #    *  *  *  *  *
# #       *  *  *
# #          *

# n=4
# for i in range(1,n+1):
#     for k in range(1,n+1-i):
#           print("  ",end=" ")
#     for j in range(1,(2*i-1)+1):
#             print("* ",end=" ")
#     print()
# n=3
# for i in range(n,0,-1):
#     for k in range(0,n+1-i):
#           print("  ",end=" ")
#     for j in range(1,(2*i-1)+1):
#             print("* ",end=" ")
#     print()


# # M) Print the following pattern
# # *               * 
# # * *           * *
# # * * *       * * *
# # * * * *   * * * *
# # * * * * * * * * *

# n=5
# for i in range(1,6):
#         for j in range(i):
#             print("*",end=" ")
#         for k in range(((5-i)*2)-1):
#           print(" ",end=" ")
#         if i==5:
#             for j in range(4):
#                 print("*",end=" ")
#         else:
#             for j in range(i):
#                 print("*",end=" ")

#         print()


# # N) Print the following pattern
# # * * * * * * * * * 
# # * * * *   * * * *
# # * * *       * * *
# # * *           * *
# # *               *

# for i in range(5,0,-1):
#   for j in range(i):
#     print("*",end=" ")
#   for k in range(((5-i)*2)-1):
#     print(" ",end=" ")
#   if i==5:
#     for L in range(4):
#       print("*",end=" ")
#   else:    
#     for L in range(i):
#       print("*",end=" ")
#   print()

# # O) Print the following pattern
# # 1 
# # 2 2
# # 3 3 3
# # 4 4 4 4
# # 5 5 5 5 5

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#             print(i ,end=" ")
#     print()


# # P) Print the following pattern
# # 1 
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#             print(j ,end=" ")
#     print()


# # Q) Print the following pattern
# # 1 
# # 0 1
# # 1 0 1
# # 0 1 0 1
# # 1 0 1 0 1

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if(i==j or (i+j)%2==0):
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()


# # R) Print the following pattern
# #          1 
# #        2 3 2
# #      3 4 5 4 3
# #    4 5 6 7 6 5 4
# #  5 6 7 8 9 8 7 6 5 

# for i in range(1,6):
#   for j in range(5-i,0,-1):
#     print(" ",end=" ")
#   for k in list(range(i,2*i))+list(range(2*i-2,i-1,-1)):
#     print(f"{k}",end=" ")
#   print()

# # S) Print the following pattern
# #      1 
# #     1 1
# #    1 2 1
# #   1 3 3 1
# #  1 4 6 4 1

# import math
# for i in range(5):
#   for j in range(5-i,0,-1):
#     print(" ",end="")
#   for k in range(i+1):
#     print(math.comb(i,k),end=" ")
#   print()

# # T) Print the following pattern  
# #        1   
# #       2   3
# #     4   5   6
# #   7   8   9   10
# # 11  12  13  14  15

# a=1
# for i in range(1,6):
#   print("  "*(5-i),end="")
#   for j in range(i):
#     if a<11:
#       print(f"{a}",end="   ")
#     else:
#       print(f"{a}",end="  ")
#     a+=1
#   print()