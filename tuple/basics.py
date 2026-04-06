# Use parentheses ( ) — commas define the tuple, not parens
t1 = (10, 20, 30)
t2 = ("apple", "banana", "cherry")
t3 = (1, "hello", 3.14, True)   # mixed types
t4 = ()                              # empty tuple
t5 = (42,)                          # ← comma needed for single item!
t6 = (1, 2, (3, 4), (5, 6))        # nested tuples

# Parens are optional — commas are what matter
t7 = 10, 20, 30                     # also a tuple!
type(t7)  # <class 'tuple'>


t = ("a", "b", "c")
type(t)          # <class 'tuple'>
len(t)           # 3
"b" in t         # True
"z" not in t     # True

# Convert any iterable to tuple
tuple([1, 2, 3])     # (1, 2, 3)
tuple("hello")       # ('h','e','l','l','o')
tuple(range(5))      # (0, 1, 2, 3, 4)
print(tuple({1,2,3}.union({4,5,6})))       # (1, 2, 3) from set

a = (1, 2)
b = (3, 4)
c = a + b          # (1, 2, 3, 4) new tuple
d = a * 3          # (1, 2, 1, 2, 1, 2)
e = ("x",) * 4     # ('x','x','x','x')

print(a)
print(b)
print(c)
print(d)
print(e)




t = (3, 1, 2)
# Order is preserved forever
# (3, 1, 2) stays (3, 1, 2)

# Comparing tuples:
print((1,2) == (1,2))   # True
print((1,2) == (2,1))   # False — order matters
