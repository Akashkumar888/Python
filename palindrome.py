
def is_symmetric(string):
    n = len(string)
    mid = n // 2
    if string[:mid] == string[mid:][::-1]:
        return "Symmetrical"
    elif string == string[::-1]:
        return "Palindrome"
    else:
        return "Neither"

string = "madam"
result = is_symmetric(string)
print(f"The string '{string}' is {result}.")

