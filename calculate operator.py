def calculate(a, operator, b):
	valid_operators = ("+", "-", "*", "/", "//", "%", "**")
	if operator not in valid_operators:
		raise ValueError("Invalid operator")

	if operator in ("/", "//", "%") and b == 0:
		raise ValueError("Division by zero is not allowed")

	if operator == "+":
		return a + b
	if operator == "-":
		return a - b
	if operator == "*":
		return a * b
	if operator == "/":
		return a / b
	if operator == "//":
		return a // b
	if operator == "%":
		return a % b
	return a ** b


first_number = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /, //, %, **): ").strip()
second_number = float(input("Enter the second number: "))

try:
	print(calculate(first_number, operator, second_number))
except ValueError as error:
	print(error)