#defines a function to check if the year is evenly divisible by 100
def check100(x):
    if x % 100 == 0:
        return(True)
    else:
        return(False)
#defines a function to check if the year is evenly divisible by 400
def check400(x):
    if x % 400 == 0:
        return(True)
    else:
        return(False)
#takes user input and converts to a int
y = input("What year is it?")
y = int(y)
#checking if it's a leap year.
if y % 4 == 0:
    check100(y)
    check400(y)
    #all possible conditions of y % 4 = 0.
    if check100(y) == True and check400(y) == False:
        print("Not a leap year")
    if check100(y) == True and check400(y) == True:
        print("Leap year")
    if check100(y) == False and check400(y) == False:
        print("Leap year")
else:
    print("Not a leap year")
