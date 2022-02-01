def word_count(str):
    str = str.split()
    counts = []

    for i in str:
        if i not in counts:
            counts.append(i) 

    for i in range(0, len(counts)):
        print(counts[i], ':', str.count(counts[i]))

def main():
    text = input("Type a sentence: ")
    word_count(text)

main()
