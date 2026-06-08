MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    """Run the score menu program."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score(score)
            print(result)
        elif choice == "S":
            star_result = get_stars(score)
            print(star_result)
        else:
            print("Invalid message!")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")

def get_valid_score():
    """Get a valid score between 0 and 100."""
    score = int(input("Enter a score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def determine_score(score):
    """Return the score result."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def get_stars(score):
    """Return stars"""
    stars = "*" * score
    return stars

main()