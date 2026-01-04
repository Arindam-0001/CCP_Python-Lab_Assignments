# Palindrome number checking number

# Function to reverse the number
def reverse(number):
    rev = str(number)[::-1]
    return rev

# Function to check if the number is a palindrome
def isPalindrome(number):
    if str(number) == reverse(number):
        return True
    else:
        return False

# Main code
num = int(input("Enter a number: "))

if isPalindrome(num):
    print(num, "is a Palindrome number")
else:
    print(num, "is not a Palindrome number")
