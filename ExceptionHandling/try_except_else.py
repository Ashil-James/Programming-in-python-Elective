try:
    x = int(input("Enter number: "))
    result = 10 / x

except ValueError:
    print("Invalid input!")

except ZeroDivisionError:
    print("Division by zero!")

else:
    print("Success! Result =", result)