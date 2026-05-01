class NegativeNumberError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


try:
    num = int(input("Enter a number: "))

    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")

    print("Valid number:", num)

except NegativeNumberError as e:
    print("Error:", e)