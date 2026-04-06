fruits = ["apple", "banana", "apple", "cherry"]
fruits.remove("apple")
# ["banana", "apple", "cherry"]  ← only FIRST "apple" gone
# Raises ValueError if item not found

nums = [10, 20, 30, 40]

x = nums.pop()      # no index → removes LAST
# x = 40,  nums = [10, 20, 30]
print(x)

y = nums.pop(0)     # removes FIRST
# y = 10,  nums = [20, 30]
print(y)

z = nums.pop(1)     # removes index 1
# z = 30,  nums = [20]
print(z)

# Del removes by index or slice
a = [1, 2, 3, 4, 5]
del a[0]    # removes index 0
# a = [2, 3, 4, 5]
del a[1:3] # removes slice [1:3]
# a = [2, 5]
print(a)

#clear: removes all the elements and returns an empty list
nums = [1, 2, 3, 4]
nums.clear()
# []   ← empty list, variable still exists