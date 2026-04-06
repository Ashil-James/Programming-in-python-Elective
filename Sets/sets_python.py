# Creating sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Adding elements
A.add(10)                  # add single element
A.update(B)           # add multiple elements
print(A)
# Removing elements
A.remove(2)                # removes 2 (error if not present)
A.discard(100)             # safe remove (no error)

# Set operations
union_set = A.union(B)             # all elements
intersection_set = A.intersection(B)  # common elements
difference_set = A.difference(B)      # A - B
symmetric_set = A.symmetric_difference(B)  # non-common

# Other functions
length = len(A)
maximum = max(A)
minimum = min(A)
total = sum(A)

# Output
print("Set A:", A)
print("Set B:", B)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (A-B):", difference_set)
print("Symmetric Difference:", symmetric_set)
print("Length:", length)
print("Max:", maximum)
print("Min:", minimum)
print("Sum:", total)