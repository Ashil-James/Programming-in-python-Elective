# in-place sorting with sort() method
nums = [3, 1, 4, 1, 5]
nums.sort()                   # [1, 1, 3, 4, 5]  ascending
print(nums)
nums.sort(reverse=True)        # [5, 4, 3, 1, 1]  descending
print(nums)

words = ["banana", "apple", "cherry"]
words.sort()  
print(words)  # ["apple","banana","cherry"]
words.sort(key=len, reverse = True)# sort by string length
print(words)  # ["banana","cherry","apple"]

# sorted() function returns a NEW sorted list, original unchanged
print("With Sorted: ")
nums = [3, 1, 4]
new = sorted(nums)    
print(new)  # [1, 3, 4]
# nums is still [3, 1, 4] !

new1 = sorted(words, reverse=True, key = len)     # [4, 3, 1]
print(new1)

print(sorted("python"))               # ['h','n','o','p','t','y']