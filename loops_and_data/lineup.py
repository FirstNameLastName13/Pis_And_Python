votes = {}
artist = ""
def main():
    while True:
        global artist 
        artist = input("enter a musician:")
        artist = artist.strip()
        artist = artist.lower()
        key = artist
        if artist == "done":
            alpha = dict(sorted(votes.items()))
            for key, value in alpha.items():
                print(f"{key}: {value}")
            break
        elif key in votes:
            votes[key] += 1
        elif not key in votes:
            votes[artist] = 1
main()
