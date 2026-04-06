s = "Hello, World!"

# Reverse a string
s[::-1]                    # "!dlroW ,olleH"

# Check if palindrome
print("racecar" == "racecar"[::-1])  # True

# Remove first / last character
s[1:]      # "ello, World!"
s[:-1]     # "Hello, World!"

# Get every other character
s[::2]     # "Hlo ol!"

# First N characters
s[:5]      # "Hello"

# Last N characters
s[-6:]     # "orld!"

# Middle chunk
s[7:12]    # "World"

# Slice works on lists too!
nums = [10,20,30,40,50]
nums[1:4]  # [20, 30, 40]
nums[::-1] # [50, 40, 30, 20, 10]