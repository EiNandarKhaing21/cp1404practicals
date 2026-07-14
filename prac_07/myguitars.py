import csv

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = using_csv()
    display_guitars(guitars)
    add_new_guitars(guitars)
    save_guitars(guitars)


def using_csv():
    """Load guitars from CSV file into a list of Guitar objects."""
    guitars = []
    with open(FILENAME, "r", newline="") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name, year, cost = row[0], int(row[1]), float(row[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    """Display guitars sorted by year."""
    guitars.sort()  # uses __lt__ method in Guitar
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>25} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def add_new_guitars(guitars):
    """Ask user to enter new guitars and add them to the list."""
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")


def save_guitars(guitars):
    """Save list of Guitar objects back to CSV file."""
    with open(FILENAME, "w", newline="") as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


main()