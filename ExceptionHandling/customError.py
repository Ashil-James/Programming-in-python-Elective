class NegativeNumberError(Exception):
    def __init__(self, num):
        super().__init__(f"Negative number not allowed: {num}")
        self.num = num
        
class Calculator:
    def square(self, num):
        if num < 0:
            raise NegativeNumberError(num)
        return num * num
    
    
calc = Calculator()

try:
    result = calc.square(-4)
    print("Result:", result)

except NegativeNumberError as e:
    print("Error:", e)