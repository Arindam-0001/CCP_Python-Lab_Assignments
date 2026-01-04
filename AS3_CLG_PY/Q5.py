# Display ASCII code to character
ascii_code=int(input("Enter an ASCII code(0-127): "))
if 0<=ascii_code<=127:
    print("Character:",chr(ascii_code))
else:
    print("Invalid ASCII code!")