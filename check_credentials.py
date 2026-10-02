def check_credentials(username, password):
	if username == "admin" and password == "python123":
		return "Valid user"
	return "Invalid user"


username = input("Enter username: ")
password = input("Enter password: ")

print(check_credentials(username, password))