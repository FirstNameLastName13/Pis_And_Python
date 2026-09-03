x = (input("what temperature is it, in degrees fahrenheit?"))
#checks if the string contains letters
if any(char.isalpha() for char in x):
    print("invalid input")
#if the string doesn't contain letters than this part of the program will run
else:
    x = float(x)
    if x > 140:
        print("invalid input")
    else:
        if x < 60:
            print("you need to bring a sweater")
        else:
            print("you do not need a sweater")
