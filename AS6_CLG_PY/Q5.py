def countLowertoUpper(text):
    upper = 0
    lower = 0

    for ch in text:
        if ch >= 'A' and ch <= 'Z':
            upper = upper + 1
        elif ch >= 'a' and ch <= 'z':
            lower = lower + 1

    result = {"Uppercase": upper, "Lowercase": lower}
    return result


# --- Sample calls ---
print(countLowertoUpper("Hello World"))
print(countLowertoUpper("Python Programming"))
print(countLowertoUpper("CENTRAL calcutta Polytechnic"))
