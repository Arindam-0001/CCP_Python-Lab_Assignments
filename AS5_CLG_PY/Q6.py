# # Palindrome number checking program    method-1
# num=int(input("Enter a number: "))
# original_num=num
# f=1
# rev=0
# while num!=0:
#     rem=num%10
#     rev+=f*rem
#     f*=10
#     num//=10
# if rev==original_num:
#     print(original_num,"is a palindrome number")
# else:
#     print(original_num,"is not a palindrome number")


# Palindrome number checking program    method-2
num=input("Enter a number: ")
if num==num[::-1]:
    print(num,"is a palindrome number")
else:
     print(num,"is not a palindrome number")