original = [1, 2, 3]
copy1 = original.copy()
copy1.append(4)
# copy1   = [1, 2, 3, 4]
# original = [1, 2, 3]  ← unchanged!

# Three ways to copy:
b = original.copy()    # method
c = original[:]         # slice
d = list(original)     # constructor

# Aliasing: no copy, just another name for same list
a = [1, 2, 3]
b = a             # b points to SAME list!
b.append(4)
print(a)          # [1, 2, 3, 4]  ← a changed too!

# Fix: use copy()
b = a.copy()      # now b is independent
b.append(99)
print(a)          # [1, 2, 3, 4]  ← safe