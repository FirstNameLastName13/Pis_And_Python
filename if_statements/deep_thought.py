text = input("What is the answer to life, the universe, and everything?")
#removes weird formatting - e.g. uppercases, dashes, spaces, etc
if "-" in text:
    text = text.replace("-", "")

text = text.strip().lower()

#uses the final text to determine if the user gave the correct answer.
if text == "42" or text == "fourty two" or text == "fourtytwo":
    print("Yes :D")
else: 
    print("No")
