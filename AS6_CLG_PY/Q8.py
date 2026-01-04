# Function to print characters between ch1 and ch2
def printChars(ch1, ch2, numberPerLine):
    count = 0
    for ch in range(ord(ch1), ord(ch2) + 1):
        print(chr(ch), end=' ')
        count = count + 1
        if count % numberPerLine == 0:
            print()  # move to the next line

# --- Main program ---
printChars('1', 'Z', 10)
