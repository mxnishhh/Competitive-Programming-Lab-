code = input("Enter book code: ")

valid = True

# Check length
if len(code) != 12:
    valid = False

# Check first 3 characters are uppercase letters
elif not (code[0:3].isalpha() and code[0:3].isupper()):
    valid = False

# Check first hyphen
elif code[3] != '-':
    valid = False

# Check 4 digits
elif not code[4:8].isdigit():
    valid = False

# Check second hyphen
elif code[8] != '-':
    valid = False

# Check last 3 digits
elif not code[9:12].isdigit():
    valid = False

if valid:
    print("Valid book code")
else:
    print("Invalid book code")