# Python Examples

This file explains all Python programs found in the current folder. I checked the actual .py files and explained each one in simple beginner-friendly English.

There are 10 Python files in this folder.

---

## 1. calculate.py

### Program 1: Simple arithmetic calculator

What it does:
This program takes two numbers from the user and performs basic arithmetic operations such as addition, subtraction, multiplication, division, floor division, and remainder.

Code:
```python
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
```

Line-by-line explanation:
- `def calculate(first_number, second_number):` → Creates a function named `calculate`. This function needs two values, called parameters.
- `results = { ... }` → Creates a dictionary called `results` to store many results under names like "Addition" and "Subtraction".
- `"Addition": first_number + second_number` → Adds the two numbers and stores the answer under the name "Addition".
- `"Subtraction": first_number - second_number` → Subtracts second number from first number.
- `"Multiplication": first_number * second_number` → Multiplies the numbers.
- `if second_number == 0:` → Checks whether the second number is zero.
- `results["Division"] = "Cannot divide by zero"` → If the second number is zero, we cannot divide. So the program stores a message instead of a number.
- `results["Floor division"] = "Cannot divide by zero"` → Same idea for floor division.
- `results["Remainder"] = "Cannot divide by zero"` → Same idea for remainder.
- `else:` → This runs only when the second number is not zero.
- `results["Division"] = first_number / second_number` → Normal division using `/`.
- `results["Floor division"] = first_number // second_number` → Floor division removes the decimal part. Example: 9 // 4 gives 2.
- `results["Remainder"] = first_number % second_number` → Remainder gives the leftover value. Example: 9 % 4 gives 1.
- `return results` → Sends the dictionary back to the place where the function was called.
- `first_number = float(input(...))` → Takes input from the user, converts it to a decimal number using `float()`, and stores it.
- `second_number = float(input(...))` → Takes the second input and converts it to decimal.
- `for operation, result in calculate(first_number, second_number).items():` → Calls the function and loops through each item in the returned dictionary.
- `print(f"{operation}: {result}")` → Prints the operation name and its result.

How it works:
1. The program asks for the first number.
2. It asks for the second number.
3. It calls the `calculate` function.
4. The function checks whether the second number is zero.
5. If not zero, it calculates all operations and returns the results.
6. The loop prints each result one by one.

Example:
Input:
```
Enter the first number: 10
Enter the second number: 3
```

Expected output:
```
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Floor division: 3
Remainder: 1
```

Important concepts:
- `def` → Used to create a function.
- `return` → Sends a value back from a function.
- `if` → Checks a condition.
- `else` → Runs when the condition is false.
- `float()` → Converts input text into a decimal number.
- Dictionary → Stores data as key-value pairs.
- `for` loop → Repeats over items in a collection.

Real-world analogy:
This is like a basic calculator machine. It accepts two numbers and gives several answers at once.

---

## 2. check_number.py

### Program 2: Check if a number is even/odd and divisible by 3 or 5

What it does:
This program accepts an integer and tells whether it is even or odd, and whether it is divisible by 3 and 5.

Code:
```python
def check_number(number):
	return {
		"Even or odd": "Even" if number % 2 == 0 else "Odd",
		"Divisible by 3": number % 3 == 0,
		"Divisible by 5": number % 5 == 0,
	}


number = int(input("Enter an integer: "))

for check, result in check_number(number).items():
	print(f"{check}: {result}")
```

Line-by-line explanation:
- `def check_number(number):` → Defines a function that accepts one integer value.
- `return { ... }` → Returns a dictionary with multiple answers.
- `"Even or odd": "Even" if number % 2 == 0 else "Odd"` → Uses a conditional expression. If the number is divisible by 2, it prints "Even"; otherwise it prints "Odd".
- `number % 2 == 0` → `%` gives the remainder. If remainder is 0, the number is divisible by 2.
- `"Divisible by 3": number % 3 == 0` → Checks if remainder is 0 when dividing by 3.
- `"Divisible by 5": number % 5 == 0` → Checks if remainder is 0 when dividing by 5.
- `number = int(input("Enter an integer: "))` → Takes input and converts it to an integer using `int()`.
- `for check, result in check_number(number).items():` → Calls the function, then loops through each key-value pair in the dictionary.
- `print(f"{check}: {result}")` → Prints each check and its result.

How it works:
1. The user enters an integer.
2. The function checks divisibility by 2, 3, and 5.
3. It returns a dictionary with the results.
4. The loop prints each result.

Example:
Input:
```
Enter an integer: 15
```

Expected output:
```
Even or odd: Odd
Divisible by 3: True
Divisible by 5: True
```

Important concepts:
- `%` operator → Finds the remainder.
- `if ... else` inside a dictionary value → Short form of a conditional expression.
- `return` → Returns the result dictionary.
- `int()` → Converts input to an integer.

Real-world analogy:
This is like a number scanner that checks whether the number fits certain rules.

---

## 3. check_marks.py

### Program 3: Student mark result checker

What it does:
This program receives a student’s marks and tells whether the student has passed, failed, or earned distinction.

Code:
```python
def check_marks(marks):
	if marks >= 75:
		return "Distinction"
	if marks >= 35:
		return "Pass"
	return "Fail"


marks = float(input("Enter the student's marks: "))
print(check_marks(marks))
```

Line-by-line explanation:
- `def check_marks(marks):` → Creates a function that accepts one value called `marks`.
- `if marks >= 75:` → Checks if the marks are 75 or more.
- `return "Distinction"` → If true, the function returns the string "Distinction".
- `if marks >= 35:` → If the first condition is false, it checks whether marks are 35 or above.
- `return "Pass"` → If true, it returns "Pass".
- `return "Fail"` → If both conditions are false, it returns "Fail".
- `marks = float(input("Enter the student's marks: "))` → Takes user input and converts it to a decimal number.
- `print(check_marks(marks))` → Calls the function and prints the result.

How it works:
1. The program asks for the student's marks.
2. It checks the marks in order.
3. If marks are at least 75, it returns “Distinction”.
4. Otherwise, if marks are 35 or above, it returns “Pass”.
5. Otherwise, it returns “Fail”.

Example:
Input:
```
Enter the student's marks: 80
```

Expected output:
```
Distinction
```

Important concepts:
- `if` → Checks a condition.
- `return` → Stops the function and gives a result.
- `float()` → Accepts decimal marks.

Real-world analogy:
This is like a school result system that decides pass/fail based on marks.

---

## 4. check_eligibility.py

### Program 4: Student eligibility check

What it does:
This program checks whether a student is eligible based on marks, attendance, and backlog status.

Code:
```python
def check_eligibility(marks, attendance, has_backlog):
	if marks >= 60 and attendance >= 75 and not has_backlog:
		return "Eligible"
	return "Not eligible"


marks = float(input("Enter the student's marks: "))
attendance = float(input("Enter the attendance percentage: "))
has_backlog = input("Does the student have a backlog? (true/false): ").strip().lower() == "true"

print(check_eligibility(marks, attendance, has_backlog))
```

Line-by-line explanation:
- `def check_eligibility(marks, attendance, has_backlog):` → Defines a function with three parameters.
- `if marks >= 60 and attendance >= 75 and not has_backlog:` → This is a combined condition. The student is eligible only if all of these are true:
  - marks are at least 60
  - attendance is at least 75
  - there is no backlog
- `return "Eligible"` → If all conditions are true, returns "Eligible".
- `return "Not eligible"` → If any condition is false, returns "Not eligible".
- `marks = float(input(...))` → Reads marks and converts to float.
- `attendance = float(input(...))` → Reads attendance percentage.
- `has_backlog = input(...).strip().lower() == "true"` → Reads a text answer like true or false, removes spaces, converts to lowercase, and compares with "true". The result is a Boolean value (`True` or `False`).
- `print(check_eligibility(marks, attendance, has_backlog))` → Calls the function and prints the result.

How it works:
1. The program asks for marks.
2. It asks for attendance.
3. It asks if the student has a backlog.
4. It checks all conditions together with `and` and `not`.
5. It prints whether the student is eligible or not.

Example:
Input:
```
Enter the student's marks: 70
Enter the attendance percentage: 80
Does the student have a backlog? (true/false): false
```

Expected output:
```
Eligible
```

Important concepts:
- `and` → All conditions must be true.
- `not` → Reverses a condition. Example: `not has_backlog` means no backlog.
- `==` → Comparison operator. Checks if two values are equal.
- Boolean values → `True` or `False`.

Real-world analogy:
This is like a rule check for admission. A student must satisfy all rules before getting approval.

---

## 5. check_credentials.py

### Program 5: Username and password check

What it does:
This program checks whether a username and password match the required values.

Code:
```python
def check_credentials(username, password):
	if username == "admin" and password == "python123":
		return "Valid user"
	return "Invalid user"


username = input("Enter username: ")
password = input("Enter password: ")

print(check_credentials(username, password))
```

Line-by-line explanation:
- `def check_credentials(username, password):` → Defines a function with two parameters.
- `if username == "admin" and password == "python123":` → Checks whether both values match exactly.
- `return "Valid user"` → If both match, returns a success message.
- `return "Invalid user"` → Otherwise, returns an error message.
- `username = input("Enter username: ")` → Reads the username from the user.
- `password = input("Enter password: ")` → Reads the password.
- `print(check_credentials(username, password))` → Calls the function and prints the result.

How it works:
1. The program asks for the username.
2. It asks for the password.
3. It compares the values with the required ones.
4. If both are correct, it prints “Valid user”.
5. Otherwise, it prints “Invalid user”.

Example:
Input:
```
Enter username: admin
Enter password: python123
```

Expected output:
```
Valid user
```

Important concepts:
- `==` → Checks equality.
- `and` → Both conditions must be true.
- String comparison → Strings must match exactly, including case and characters.

Real-world analogy:
This is like logging into an account. The system checks whether the username and password are correct.

---

## 6. calculate_discount.py

### Program 6: Discount and final amount calculator

What it does:
This program calculates the discount and the final amount to be paid based on the purchase amount.

Code:
```python
def calculate_discount(amount):
	if amount >= 5000:
		discount_rate = 0.20
	elif amount >= 3000:
		discount_rate = 0.10
	elif amount < 300:
		discount_rate = 0.05
	else:
		discount_rate = 0

	discount_amount = round(amount * discount_rate, 2)
	final_amount = round(amount - discount_amount, 2)

	return {
		"Discount amount": discount_amount,
		"Final payable amount": final_amount,
	}


purchase_amount = float(input("Enter the purchase amount: "))
result = calculate_discount(purchase_amount)

for label, value in result.items():
	print(f"{label}: {value:.2f}")
```

Line-by-line explanation:
- `def calculate_discount(amount):` → Defines a function that accepts one amount value.
- `if amount >= 5000:` → If the amount is 5000 or more, apply the highest discount.
- `discount_rate = 0.20` → 20% discount.
- `elif amount >= 3000:` → If the amount is between 3000 and 4999, apply 10% discount.
- `discount_rate = 0.10` → 10% discount.
- `elif amount < 300:` → If the amount is less than 300, apply 5% discount.
- `discount_rate = 0.05` → 5% discount.
- `else:` → If the amount is between 300 and 4999, no discount is applied.
- `discount_rate = 0` → No discount.
- `discount_amount = round(amount * discount_rate, 2)` → Calculates the discount amount and rounds it to 2 decimal places.
- `final_amount = round(amount - discount_amount, 2)` → Subtracts the discount from the original amount.
- `return { ... }` → Returns a dictionary containing the discount amount and final payable amount.
- `purchase_amount = float(input(...))` → Reads the purchase amount.
- `result = calculate_discount(purchase_amount)` → Calls the function and stores the returned dictionary.
- `for label, value in result.items():` → Loops through each item of the dictionary.
- `print(f"{label}: {value:.2f}")` → Prints each item with two digits after the decimal point.

How it works:
1. The user enters the purchase amount.
2. The function checks the discount rules in order.
3. It calculates the discount amount and the final price.
4. It returns both values in a dictionary.
5. The loop prints them neatly.

Example:
Input:
```
Enter the purchase amount: 6000
```

Expected output:
```
Discount amount: 1200.00
Final payable amount: 4800.00
```

Important concepts:
- `if/elif/else` → Used for decision-making based on conditions.
- `round()` → Rounds a number to a given number of decimal places.
- Dictionary → Stores multiple values together.

Real-world analogy:
This behaves like a shop billing system that decides how much discount to apply.

---

## 7. check_access.py

### Program 7: Access grant decision

What it does:
This program decides whether a person is allowed access by checking age, ID, and employee status.

Code:
```python
def check_access(age, has_id, is_employee):
	if (age >= 18 and has_id) or is_employee:
		return "Access granted"
	return "Access denied"


age = int(input("Enter age: "))
has_id = input("Do you have an ID? (yes/no): ").strip().lower() == "yes"
is_employee = input("Are you an employee? (yes/no): ").strip().lower() == "yes"

print(check_access(age, has_id, is_employee))
```

Line-by-line explanation:
- `def check_access(age, has_id, is_employee):` → Defines a function with three parameters.
- `if (age >= 18 and has_id) or is_employee:` → Access is granted if either:
  - the person is at least 18 and has an ID, or
  - the person is an employee.
- `return "Access granted"` → If the condition is true, it allows access.
- `return "Access denied"` → Otherwise, access is denied.
- `age = int(input("Enter age: "))` → Stores age as an integer.
- `has_id = input(...).strip().lower() == "yes"` → Reads the answer, removes spaces, converts to lowercase, then compares it with "yes". This gives a Boolean value.
- `is_employee = input(...).strip().lower() == "yes"` → Same process for employee status.
- `print(check_access(age, has_id, is_employee))` → Calls the function and prints the result.

How it works:
1. The user enters age.
2. The user says whether they have an ID.
3. The user says whether they are an employee.
4. The function checks the rules.
5. It prints whether access is allowed or not.

Example:
Input:
```
Enter age: 22
Do you have an ID? (yes/no): yes
Are you an employee? (yes/no): no
```

Expected output:
```
Access granted
```

Important concepts:
- `and` → Both conditions must be true.
- `or` → At least one condition must be true.
- Boolean values → `True` or `False`.

Real-world analogy:
This is like office entry rules. A person may be allowed in if they are old enough and have ID, or if they are an employee.

---

## 8. check_skill.py

### Program 8: Skill availability check

What it does:
This program checks whether a skill name is present in a list of required skills.

Code:
```python
required_skills = ["python", "SQL", "git", "Html"]


def check_skill(skill_name):
	if skill_name in required_skills:
		return "Skill available"
	return "Skill not available"


skill_name = input("Enter a skill name: ")
print(check_skill(skill_name))
```

Line-by-line explanation:
- `required_skills = ["python", "SQL", "git", "Html"]` → Creates a list named `required_skills` containing skills.
- `def check_skill(skill_name):` → Defines a function that accepts one skill name.
- `if skill_name in required_skills:` → Checks whether the entered skill is present in the list.
- `return "Skill available"` → If found, it returns this message.
- `return "Skill not available"` → If not found, it returns this message.
- `skill_name = input("Enter a skill name: ")` → Reads the skill name from user input.
- `print(check_skill(skill_name))` → Calls the function and prints the result.

How it works:
1. A list of required skills is stored.
2. The user enters a skill.
3. The program checks whether that skill exists in the list.
4. It prints either available or not available.

Example:
Input:
```
Enter a skill name: python
```

Expected output:
```
Skill available
```

Important concepts:
- List → A collection of values stored in order.
- `in` operator → Checks whether a value is inside a list.
- `input()` → Reads text from the user.

Real-world analogy:
This is like checking whether a requested skill appears in a company’s required skill list.

---

## 9. calculate operator.py

### Program 9: Calculator with many operators and error handling

What it does:
This program performs arithmetic operations using different operators and also handles invalid operators and division by zero.

Code:
```python
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
```

Line-by-line explanation:
- `def calculate(a, operator, b):` → Defines a function that accepts three values: two numbers and an operator.
- `valid_operators = ("+", "-", "*", "/", "//", "%", "**")` → Creates a tuple of allowed operators.
- `if operator not in valid_operators:` → Checks whether the user entered an operator that is not allowed.
- `raise ValueError("Invalid operator")` → Stops the program and raises an error if the operator is invalid.
- `if operator in ("/", "//", "%") and b == 0:` → Checks if division-like operations are used and the second number is zero.
- `raise ValueError("Division by zero is not allowed")` → Raises an error if division by zero is attempted.
- `if operator == "+":` → Checks for addition.
- `return a + b` → Adds the numbers and returns the result.
- `if operator == "-":` → Checks for subtraction.
- `return a - b` → Subtracts.
- `if operator == "*":` → Checks for multiplication.
- `return a * b` → Multiplies.
- `if operator == "/":` → Checks for normal division.
- `return a / b` → Divides and returns a decimal result.
- `if operator == "//":` → Checks for floor division.
- `return a // b` → Divides and gives only the whole part.
- `if operator == "%":` → Checks for modulus.
- `return a % b` → Returns the remainder.
- `return a ** b` → If none of the earlier operators matched, this handles power operation (`**`).
- `first_number = float(input("Enter the first number: "))` → Reads the first number.
- `operator = input("Enter an operator (+, -, *, /, //, %, **): ").strip()` → Reads the operator and removes extra spaces.
- `second_number = float(input("Enter the second number: "))` → Reads the second number.
- `try:` → Starts a block where errors may happen.
- `print(calculate(first_number, operator, second_number))` → Calls the function and prints the result.
- `except ValueError as error:` → If a `ValueError` occurs, this block handles it.
- `print(error)` → Prints the error message.

How it works:
1. User enters two numbers and an operator.
2. The function checks whether the operator is valid.
3. It checks for division by zero.
4. It performs the chosen operation.
5. A `try/except` block catches and prints error messages instead of crashing.

Example 1: valid input
Input:
```
Enter the first number: 12
Enter an operator (+, -, *, /, //, %, **): *
Enter the second number: 5
```

Expected output:
```
60.0
```

Example 2: invalid operator
Input:
```
Enter the first number: 10
Enter an operator (+, -, *, /, //, %, **): ^
Enter the second number: 3
```

Expected output:
```
Invalid operator
```

Example 3: division by zero
Input:
```
Enter the first number: 8
Enter an operator (+, -, *, /, //, %, **): /
Enter the second number: 0
```

Expected output:
```
Division by zero is not allowed
```

Important concepts:
- `tuple` → A collection of values that cannot be changed easily.
- `raise` → Creates an error intentionally.
- `try` and `except` → Used for exception handling.
- `ValueError` → An error type used for invalid values.
- `**` operator → Power operation, for example `2 ** 3 = 8`.

Real-world analogy:
This behaves like a smart calculator. It does the math, but it also warns the user if they ask for an impossible operation.

---

## 10. determine_placement.py

### Program 10: Placement eligibility and category decision

What it does:
This program checks whether a candidate is eligible for placement based on marks, attendance, and backlog, and then finds the candidate category as fresher, junior, or experienced.

Code:
```python
def determine_placement(age, marks, attendance, experience, has_backlog):
	placement_eligible = marks >= 60 and attendance >= 75 and not has_backlog

	if experience == 0:
		candidate_category = "fresher"
	elif 1 <= experience <= 2:
		candidate_category = "junior"
	elif experience > 2:
		candidate_category = "experienced"
	else:
		raise ValueError("Experience cannot be negative")

	return {
		"placement eligible": "yes" if placement_eligible else "no",
		"candidate category": candidate_category,
	}


age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))
experience = int(input("Enter years of experience: "))
has_backlog = input("Does the candidate have a backlog? (true/false): ").strip().lower() == "true"

result = determine_placement(age, marks, attendance, experience, has_backlog)
for label, value in result.items():
	print(f"{label}: {value}")
```

Line-by-line explanation:
- `def determine_placement(age, marks, attendance, experience, has_backlog):` → Defines a function with five parameters.
- `placement_eligible = marks >= 60 and attendance >= 75 and not has_backlog` → Checks if the candidate meets the placement conditions.
- `if experience == 0:` → If experience is exactly 0, the candidate is a fresher.
- `candidate_category = "fresher"` → Stores that category.
- `elif 1 <= experience <= 2:` → If the experience is between 1 and 2, the category is junior.
- `candidate_category = "junior"` → Stores the junior category.
- `elif experience > 2:` → If experience is more than 2, the candidate is experienced.
- `candidate_category = "experienced"` → Stores that category.
- `else:` → If experience is negative, the program raises an error.
- `raise ValueError("Experience cannot be negative")` → Stops the program and shows an error message.
- `return { ... }` → Returns a dictionary with placement status and candidate category.
- `"placement eligible": "yes" if placement_eligible else "no"` → A short conditional expression. If eligible, it prints yes; otherwise no.
- `"candidate category": candidate_category` → Stores the category value.
- `age = int(input("Enter age: "))` → Reads age.
- `marks = float(input("Enter marks: "))` → Reads marks.
- `attendance = float(input("Enter attendance percentage: "))` → Reads attendance.
- `experience = int(input("Enter years of experience: "))` → Reads years of experience.
- `has_backlog = input(...).strip().lower() == "true"` → Reads backlog status and converts it to `True` or `False`.
- `result = determine_placement(age, marks, attendance, experience, has_backlog)` → Calls the function and stores the dictionary.
- `for label, value in result.items():` → Loops through the dictionary items.
- `print(f"{label}: {value}")` → Prints each label and its value.

How it works:
1. User enters age, marks, attendance, experience, and backlog status.
2. The function checks placement eligibility.
3. It decides the candidate category based on years of experience.
4. It returns a dictionary with both values.
5. The loop prints the output.

Example:
Input:
```
Enter age: 21
Enter marks: 85
Enter attendance percentage: 90
Enter years of experience: 1
Does the candidate have a backlog? (true/false): false
```

Expected output:
```
placement eligible: yes
candidate category: junior
```

Important concepts:
- `and` → All rules must be true for placement eligibility.
- `if/elif/else` → Used to classify candidates.
- `raise` → Creates an error for invalid negative experience.
- Dictionary → Stores multiple values together.

Important note:
- The function accepts an `age` parameter, but in this code it is never used in the actual decision. So the program checks marks, attendance, backlog, and experience, but not age. This is valid Python code, but it does not use the age value in the logic.

Real-world analogy:
This is like an HR or campus placement system that checks if a person is eligible and then places them into a level based on experience.

---

# Quick Revision

Here are the main Python concepts used across these files.

## 1. Variables
A variable is a name used to store a value.

Example:
```python
age = 21
name = "Alice"
```

- `age` stores a number.
- `name` stores a text value.

## 2. Data types
Different kinds of values have different types.

Examples:
- int → whole numbers like 10, 25
- float → decimal numbers like 12.5, 7.8
- str → text like "admin", "python"
- bool → True or False

## 3. Input and output
- `input()` is used to read value from the user.
- `print()` is used to display output.

Example:
```python
name = input("Enter your name: ")
print("Hello", name)
```

## 4. Operators
Operators do calculation or compare values.

Examples:
- Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparison: `==`, `>=`, `<=`, `>`, `<`
- Logical: `and`, `or`, `not`

## 5. if / elif / else
These are used to make decisions.

Example:
```python
if marks >= 75:
    print("Distinction")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")
```

## 6. Loops
A loop repeats a block of code again and again.

Example:
```python
for item in [1, 2, 3]:
    print(item)
```

In the files, loops are used mainly to print dictionary items.

## 7. Functions
A function is a reusable block of code.

Example:
```python
def add(a, b):
    return a + b
```

Functions help us organize code and avoid repetition.

## 8. Parameters and arguments
- Parameters are names listed in the function definition.
- Arguments are the values passed to the function when it is called.

Example:
```python
def check_marks(marks):
    ...

check_marks(80)
```

Here, `marks` is a parameter, and `80` is an argument.

## 9. return
`return` sends a result back from a function.

Example:
```python
def square(x):
    return x * x
```

The function gives the result back to the caller.

## 10. Built-in functions
Python already provides some useful functions.

Examples found in these files:
- `input()`
- `print()`
- `int()`
- `float()`
- `round()`

## 11. Lists
A list stores multiple values in one variable.

Example:
```python
required_skills = ["python", "SQL", "git", "Html"]
```

## 12. Tuples
A tuple is similar to a list, but it is usually not changed after creation.

Example:
```python
valid_operators = ("+", "-", "*", "/", "//", "%", "**")
```

## 13. Dictionaries
A dictionary stores data as key-value pairs.

Example:
```python
result = {
    "Addition": 10,
    "Subtraction": 6
}
```

Many files use dictionaries to return multiple answers together.

## 14. Strings
Strings are text values.

Example:
```python
username = "admin"
message = "Valid user"
```

## 15. Boolean values
Boolean means True or False.

Example:
```python
has_backlog = False
is_employee = True
```

## 16. Exception handling
`try` and `except` help handle errors so the program does not crash.

Example:
```python
try:
    print(10 / 0)
except ValueError:
    print("Error")
```

This is used in the operator calculator example.

## 17. Membership operator (`in`)
The `in` operator checks whether an item is present in a list.

Example:
```python
if "python" in ["python", "SQL", "git"]:
    print("Skill available")
```

## 18. Remainder operator (`%`)
The `%` operator gives the remainder after division.

Example:
```python
9 % 4 = 1
```

## 19. Floor division (`//`)
`//` divides and removes the decimal part.

Example:
```python
9 // 4 = 2
```

## 20. Power operator (`**`)
`**` means exponentiation.

Example:
```python
2 ** 3 = 8
```

## 21. Short conditional expression
A short `if ... else` can be written in one line.

Example:
```python
"Even" if number % 2 == 0 else "Odd"
```

This is used in the number-check program.

---

This file contains explanations for all Python programs found in the workspace. The programs are simple beginner examples that teach:
- calculation
- decision making
- input/output
- functions
- conditions
- loops
- lists and dictionaries
- error handling

If you study these examples one by one, you will understand many basic Python ideas.
