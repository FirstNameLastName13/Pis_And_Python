#function to remove punctuation
def punctuation(text):
    y = text.strip().lower()
    if "!" in y:
        y = y.replace("!", "")
    if "." in y:
        y = y.replace(".", "")
    if "," in y:
        y = y.replace(",", "")
    if "?" in y:
        y = y.replace("?", "")
    if "-" in y:
        y = y.replace("-", "")
    if " " in y:
        y = y.replace(" ", "")
    return y

#actual (recursive) function to check if the text is a palindrome
def is_palindrome(text):
    if len(text) == 0:
        return True
    if len(text) == 1:
        return True
    elif text[0] == text[-1]:
        new_text = text[1:-1]
        return is_palindrome(new_text)
    elif text[0] != text[-1]:
        return False

    
#asks for user input
answer = input("input: ")
#checks if the input with all punctuation removed is a palindrome
print(is_palindrome(punctuation(answer)))
