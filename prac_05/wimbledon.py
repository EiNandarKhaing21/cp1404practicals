"""
CP1404 Practical - Wimbledon
"""

import csv

FILENAME = "wimbledon.csv"

def load_champions(filename):
    """Read champions data from file into a list of [champion, country]."""
    champions = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # skip header row
        for row in reader:
            year, champ_country, champ_name = row[0], row[1], row[2]
            champions.append([champ_name, champ_country])
    return champions

def count_champions(champions):
    """Return dictionary of champion -> number of wins."""
    champion_to_count = {}
    for name, _ in champions:
        champion_to_count[name] = champion_to_count.get(name, 0) + 1
    return champion_to_count

def get_countries(champions):
    """Return set of countries from champions list."""
    return {country for _, country in champions}

def main():
    champions = load_champions(FILENAME)

    # Count wins
    champion_to_count = count_champions(champions)
    print("Wimbledon Champions:")
    for name, wins in champion_to_count.items():
        print(f"{name} {wins}")

    # Countries
    countries = sorted(get_countries(champions))
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))

if __name__ == "__main__":
    main()
