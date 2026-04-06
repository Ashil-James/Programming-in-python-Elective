t = (1, 2, 3)

lst = list(t)       # → [1, 2, 3]
lst.append(4)       # → [1, 2, 3, 4]
t = tuple(lst)      # → (1, 2, 3, 4)

# Or just use + to "extend":
t = t + ((4,6),)        # (1, 2, 3, 4) new tuple

print(t)