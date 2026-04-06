a = [1, 2, 3]
b = [4, 5, 6]
s = "HELLO"
a.extend(b)
# [1, 2, 3, 4, 5, 6]  ← items unpacked, not nested
print(a)

a.extend("hi")    # strings are iterable too
# [1, 2, 3, 4, 5, 6, "h", "i"]
a.extend(s)
print(a)

# extend vs append comparison:
x = [1,2]
x.append([3,4])   # [1, 2, [3, 4]]  ← nested!
print(x)
print(x[2][0])

x = [1,2]
x.extend([3,4])   # [1, 2, 3, 4]    ← flat!
print(x)