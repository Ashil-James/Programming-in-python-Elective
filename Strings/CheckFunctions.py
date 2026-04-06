s = "Python123"
string = " "

print(s.isalpha())   # False (contains only letters )
print(s.isdigit())   # False (contains only digits)
print(s.isalnum())   # True (contains only letters and digits)
print(s.islower())   # False (All characters in lowercase)
print(s.isupper())   # False (All characters in uppercase)
print(string.isspace())   # True (Checks if all characters are whitespace)