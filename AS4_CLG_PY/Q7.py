# Take input from the user
ch = input("Enter a single alphabet: ")

# Convert to lowercase for uniform comparison
ch = ch.lower()

# Check if it's an alphabet and then whether it's a vowel
if ch.isalpha() and (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    print(f"{ch} is a vowel.")
elif ch.isalpha():
    print(f"{ch} is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet.") 