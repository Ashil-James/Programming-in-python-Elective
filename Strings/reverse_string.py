# Reverse a string using slicing
s = "Python"
print(s[::-1])   # nohtyP

# Reverse a string using a loop
rev = ""
for i in range(len(s)):
    rev = s[i] + rev
print(rev)   # nohtyP