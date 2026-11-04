def draw(n):
    if n == 1:
        print("*")
        
    else:
        print("*" * n)
        draw(n-1)
        print("*" * n)

x = input("what number: ")
draw(int(x))
