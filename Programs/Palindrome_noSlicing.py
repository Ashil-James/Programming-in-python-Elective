string = str(input("Enter a string: "))
flag = True

for i in range(len(string)//2):
    if(string[i] != string[len(string) -1 - i]):
        flag = False
        print("Not a palindrome")
        break

if flag:
    print("Palindrome")