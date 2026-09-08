
def convert(a):
    x, y = a.split(":")
    x = int(x)
    y = int(y)
    y = y / 60
    return(x + y)

def main():
    time = input("what time is it")
    time = convert(time)
    if time > 6 and time < 7 or time > 18 and time < 19:
        print("dinner time")
    elif time > 7 and time < 8:
        print("breakfast time")
    elif time > 12 and time < 13 or time > 1 and time < 2:
        print("lunch time")
    else:
        print("")

main()
