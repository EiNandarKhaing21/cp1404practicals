"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    """Get a user score and a random score, then display their results."""
    score = float(input("Enter score: "))
    result = determine_score(score)
    print(f"User score {score} is {result}.")
    if result == "Excellent":
        print("You get a prize!")

    random_score = random.randint(1,100)
    result = determine_score(random_score)
    print(f"Random: {random_score} = {result}")

def determine_score(score):
    """Return the score result."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()