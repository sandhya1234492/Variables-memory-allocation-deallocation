def calculate(first_number, second_number):
	results = {
		"Addition": first_number + second_number,
		"Subtraction": first_number - second_number,
		"Multiplication": first_number * second_number,
	}

	if second_number == 0:
		results["Division"] = "Cannot divide by zero"
		results["Floor division"] = "Cannot divide by zero"
		results["Remainder"] = "Cannot divide by zero"
	else:
		results["Division"] = first_number / second_number
		results["Floor division"] = first_number // second_number
		results["Remainder"] = first_number % second_number

	return results


first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

for operation, result in calculate(first_number, second_number).items():
	print(f"{operation}: {result}")
