def add(x, y, z):
    if y == "+":
        print(x + z)
def subtract(x, y, z):
    if y == "-":
        print(x - z)
def multiply(x, y, z):
    if y == "*":
        print(x * z)
def divide(x, y, z):
    if y == "/":
        if z == 0:
            print("invalid input. you have broken the fabric of spacetime")
        else:
            print(x / z)

st = input("What math can I do for you today?")
x, y, z = st.split(" ")
x = float(x)
z = float (z)
add(x, y, z)
subtract(x, y, z)
multiply(x, y, z)
divide(x, y, z)
