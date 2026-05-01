try:
    f = open("data.txt", "r")
    print(f.read())

except FileNotFoundError:
    print("File not found")

finally:
    print("Closing file")
    try:
        f.close()
    except:
        pass

"""
try:
    x = int(input("Enter number: "))
    print(10 / x)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program ended")
"""