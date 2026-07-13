import csv

from prac_07.guitar import Guitar

def main():
    """Read file of guitars details, save as objects, display."""
    guitars = []
    # Open the file for reading
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        # Add the guitar we've just constructed to the list
        guitars.append(guitar)
    in_file.close()
    sorted_guitars = sorted(guitars)

    for guitar in sorted_guitars:
        print(guitar)


def using_csv():
    """Guitar file reader version using the csv module."""
    in_file = open('guitars.csv', 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)
    for row in reader:
        print(row)
    in_file.close()



main()