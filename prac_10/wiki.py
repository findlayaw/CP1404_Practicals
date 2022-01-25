import wikipedia

def main():
    while True:
        title = input("Title: ")
        print(wikipedia.summary(title))
        if title == "":
            break