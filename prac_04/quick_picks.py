import random

NUM_PER_LINE = 6
MIN = 1
MAX = 45


def main():
    quick_picks = int(input("How many quick picks? "))
    while quick_picks < 0:
        print("Invalid number")
        quick_picks = int(input("How many quick picks? "))

    for i in range(quick_picks):
        quick_pick_list = []
        for n in range(NUM_PER_LINE):
            number = random.randint(MIN, MAX)
            while number in quick_pick_list:
                number = random.randint(MIN, MAX)
            quick_pick_list.append(number)

        quick_pick_list.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick_list))


main()
