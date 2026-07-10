import random

MIN_NUMBER = 1
MAX_NUMBER = 45

try:
    quick_pick_count = int(input("How many quick picks? "))
    for _ in range(quick_pick_count):
        pool = list(range(MIN_NUMBER, MAX_NUMBER + 1))
        random.shuffle(pool)
        numbers = sorted(pool[:6])
        print(" ".join(f"{number:2}" for number in numbers))
except ValueError:
    print("Invalid input!")
