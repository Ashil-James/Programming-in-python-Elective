fruits = ["apple", "banana", "cherry", "banana"]

print(fruits.index("banana"))       # 1  (first match)
print(fruits.index("banana", 2))    # 3  (search from index 2)
print(fruits.index("cherry", 0, 3)) # 2  (search in [0:3])

nums = [1, 2, 2, 3, 2, 4]
nums.count(2)    # 3
nums.count(5)    # 0  (no error, just 0)

# count also works with complex items:
lst = [[1,2], [3,4], [1,2]]
lst.count([1,2])  # 2
