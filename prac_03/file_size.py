def main():
    while True:
        file_name = input("Enter filename: ")
        if file_name == "":
            break
        try:
            lines = determine_file_size(file_name)
            print(f"{file_name} has {lines} lines.")
        except FileNotFoundError:
            print(f"ERROR: {file_name} does not exist.")

def determine_file_size(file_name):
    with open(file_name, "r") as in_file:
        number_of_lines = in_file.readlines()
        return len(number_of_lines)

main()