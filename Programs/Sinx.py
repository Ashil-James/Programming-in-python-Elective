"""
    Generate sum of sin series
    sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
"""

def fact(n): 
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

n = int(input("Enter the number of terms: "))
x = float(input("Enter the value of x (in radians): "))

sin_x = 0
for i in range(n):
    term = ((-1)**i) * (x ** (2 *(i + 1)))/ fact((2 *i) + 1)
    sin_x += term

print(f"The sum of the first {n} terms of the sin series for x = {x} is: {sin_x}")