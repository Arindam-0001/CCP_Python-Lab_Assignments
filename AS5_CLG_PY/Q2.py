# count no of digits and alphabets
# Input string
text = 'Nagpur440010'

# Initialize counters
alphabet_count = 0
digit_count = 0

# Loop through each character
for char in text:
    if char.isalpha():
        alphabet_count += 1
    elif char.isdigit():
        digit_count += 1

# Display the results
print("Number of alphabets:", alphabet_count)
print("Number of digits:", digit_count) 