valid = [1, 5, 10, 25, 50, 100]
total = 0

def main():
    global total
    coin = input("what coin?")
    coin = float(coin)
    if coin in valid:
        total += coin
    else:
        print("invalid coin")

while total < 50:
    print(f"amount due: {50 - total}")
    main()
print("enjoy your beverage :D")
