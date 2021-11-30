def main():
    score = float(input("Enter score: "))
    print(score_status(score))

def score_status(score):
    while score >= 0 and score <= 100:
        if score >= 90:
            print("Excellent")
            break
        elif score >= 50:
            print("Passable")
            break
        else:
            print("Bad")
            break
    else:
        print("Invalid score")

main()