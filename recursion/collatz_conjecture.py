def collatz(n, x):
    if n == 1:
        return x
    else:
        if n % 2 == 0:
            n = n / 2
            x += 1
        else:
            n = (n * 3) +1
            x += 1
        
        return collatz(n, x)

y = input("what number")
print(collatz(int(y), 0))
