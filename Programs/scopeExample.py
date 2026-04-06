x = 10   # global variable

def outer():
    y = 20   # enclosed variable
    print("x in outer =", x)   # global
    def inner():
        z = 30   # local variable
        print("x =", x)   # global
        print("y =", y)   # enclosed
        print("z =", z)   # local

    inner()

outer()
print("x outside =", x)