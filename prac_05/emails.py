"""
CP1404 practical - emails
"""
def main():
    EMAIL_TO_NAME = {}
    email = input("Enter an email: ")
    while email != "":
        name = extract_name(email)
        print(f"Is your name {name}? (Y/N)")
        check_name = input("").lower()
        if check_name == "" or check_name == "y":
            EMAIL_TO_NAME[email] = name
        else:
            new_name = input("Name: ")
            name = new_name
            EMAIL_TO_NAME[email] = name
        email = input("Enter an email: ")

    for email, name in EMAIL_TO_NAME.items():
        print(f"{name} ({email})")

def extract_name(email):
    parts = email.split('@')
    name = parts[0]
    return name

if __name__ == '__main__':
    main()

