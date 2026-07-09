"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subjects = load_data(FILENAME)
    display_subjects(subjects)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            subject_data = [parts[0], parts[1], int(parts[2])]
            subjects.append(subject_data)
    return subjects


def display_subjects(subjects):
    """Display subject details in a readable format."""
    name_width = max(len(subject[1]) for subject in subjects)
    for subject in subjects:
        code = subject[0]
        lecturer = subject[1]
        students = subject[2]

        print(f"{code} is taught by {lecturer:{name_width}} and has {students:3} students")


main()