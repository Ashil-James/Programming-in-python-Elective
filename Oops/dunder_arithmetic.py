class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __str__(self):
        return f"Value is {self.value}"

# Usage
a = Number(10)
b = Number(5)

c = a + b
d = a - b

print(c)
print(d)