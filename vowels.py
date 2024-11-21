
def contains_all_vowels(string):
    vowels = set("aeiou")
    string_vowels = set(c.lower() for c in string if c.lower() in vowels)
    return vowels.issubset(string_vowels)

string = "Education"
if contains_all_vowels(string):
    print(f"The string '{string}' contains all vowels.")
else:
    print(f"The string '{string}' does not contain all vowels.")

