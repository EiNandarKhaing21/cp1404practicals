password_length = 8
password = input("Enter password: ")
while len(password) < password_length:
	print("Password length must be at least 8. Please re-enter.")
	password = input("Enter password: ")
print("*" * len(password))