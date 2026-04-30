"""
simplified version
"""
count = 0
with open('content.txt', 'r') as f:
    data = f.read()

for char in data:
    if char.isupper():
        count +=1

print("The file has ", count, " uppercase letters")
""""
Another possible alternative
count = 0

with open('content.txt', 'r') as f:
    line = f.readline()
    while line:
        words = line.split()
        for i in range(len(words)):
            currWrd = words[i]
            for j in range(len(currWrd)):
                if(currWrd[j].isupper()):
                    count +=1
        line = f.readline()

print("The file has ", count, " uppercase letters")
"""