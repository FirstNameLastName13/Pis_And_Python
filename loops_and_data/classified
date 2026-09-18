text = input("what text?")

text = text.lower()
text = text.replace(",", "")
text = text.replace(".", "")
text = text.replace("?", "")
text = text.replace("!", "")

words = text.split(" ")
for i in range(len(words)):
    if words[i] == "james" or words[i] == "london" or words[i] == "mi6" or words[i] == "classified" or words[i] == "paris" or words[i] == "midnight" or words[i] == "nuclear" or words[i] == "asset":
            words[i] = "[REDACTED]"

words = " ".join(words)

print(words)
