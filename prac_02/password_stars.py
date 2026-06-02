def main():
	"""Get a valid password and display it as asterisks."""
	password_length = 8
	password = get_password(password_length)
	print("*" * len(password))


def get_password(password_length):
	"""Prompt the user for a password of at least password_length characters."""
	password = input("Enter password: ")
	while len(password) < password_length:
		print(f"Password length must be at least {password_length}. Please re-enter.")
		password = input("Enter password: ")
	return password

main()