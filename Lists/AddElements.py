fruits = ["apple", "banana"]
fruits.append("cherry")
# ["apple", "banana", "cherry"]

fruits.append(["kiwi","grape"])
# ["apple","banana","cherry",["kiwi","grape"]]
# ↑ appends the list as a SINGLE element

nums = [10, 20, 40, 50]
nums.insert(2, 30)   # insert 30 at index 2
# [10, 20, 30, 40, 50]

nums.insert(0, 5)    # insert at front
# [5, 10, 20, 30, 40, 50]

nums.insert(999, 99) # beyond end → appends
# [5, 10, 20, 30, 40, 50, 99]
