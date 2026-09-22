def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

    

def is_valid(s):
    plate = [s]
    if len(plate) < 2 or if len(plate):
        return False
    elif not plate.isalnum():
        return False
    elif any(isinstance(item, (int, float)) for item in plate):
        return False

main()
