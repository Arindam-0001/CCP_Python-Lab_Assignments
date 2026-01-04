# # Function to display three numbers in increasing order
# def displaySortedNumbers(num1,num2,num3):
#     # Find the largest between three numbers
#     if num1>num2 and num1>num3:
#         large=num1
#     elif num2>num1 and num2>num3:
#         large=num2
#     else:
#         large=num3
#     # Find the 2nd largest between three numbers
#     if num1==large:
#         if num2>num3:
#             largest2=num2
#         else:
#             largest2=num3
#     elif num2==large:
#         if num1>num3:
#             largest2=num1
#         else:
#             largest2=num3
#     else:
#         if num2>num1:
#             largest2=num2
#         else:
#             largest2=num1
#     # Find the smallest between three numbers
#     if num1<num2 and num1<num3:
#         smallest=num1
#     elif num2<num1 and num2<num3:
#         smallest=num2
#     else:
#         smallest=num3
#     print(smallest,largest2,large)     

# displaySortedNumbers(1,2,3)
# displaySortedNumbers(7,9,6)

def displaySortedNumbers(num1, num2, num3):
    numbers = [num1, num2, num3]
    numbers.sort()   # sorts in ascending order
    print(numbers[0], numbers[1], numbers[2])

# Test cases
displaySortedNumbers(1, 2, 3)
displaySortedNumbers(7, 9, 6)
displaySortedNumbers(10, 5, 8)


def displaySortedNumbers(num1, num2, num3):
    print(*sorted([num1, num2, num3]))
