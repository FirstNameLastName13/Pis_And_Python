def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def num_check(number):
    num_list = []
    for i in range(len(number)):
         if not number[i].isalpha():
              x = int(number[i])
              num_list.append(x)
    if num_list[0] == 0:
                return False
    else:
        return True
    
def check_2(string):
    for i in range(len(string)):
        try:
            if not string[i].isalpha() and string[i + 1].isalpha():
                return False
        except:
            return True
    else:
        return True

def is_valid(s):
    plate = list(s)
    try:
        for i in range(len(s)):
            i = int(i)
    except TypeError:
        print("")
    
    if len(plate) < 2 or len(plate) > 6:
        return False
    elif not s.isalnum():
        return False
    elif s.isalpha():
        return True
    elif not s[0].isalpha() and not s[1].isalpha():
            return False
    elif not num_check(plate):
        return False
    elif not check_2(plate):
        return False
    else:
        return True
main()
