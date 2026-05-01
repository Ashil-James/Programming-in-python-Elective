class OddNumberError(Exception):
    def __init__(self, num):
        self.num = num
        super().__init__(f"{num} is an odd number, only even numbers allowed")
        
try:
    n = int(input("Enter a number: "))

    if n % 2 != 0:
        raise OddNumberError(n)

    print("Valid number:", n)

except OddNumberError as e:
    print("Error:", e)
    print("You entered:", e.num)   # using stored value