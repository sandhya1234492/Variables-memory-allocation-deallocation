# Python Functions: Important Questions and Answers

## 1. What is a function?

A function is a named, reusable block of code that performs a particular task. It can receive input, work with that input, and optionally send a result back to the code that called it.

```python
def square(number):
	return number * number
```

Here, `square` is a function. It accepts a number and returns its square. Python also provides built-in functions such as `print()` and `len()`.

## 2. Why do we use functions?

Functions help us:

- Reuse code instead of writing the same logic repeatedly.
- Break a large program into smaller, understandable parts.
- Test and fix one task independently.
- Give meaningful names to operations, making code easier to read.
- Change an implementation in one place instead of updating repeated copies.

For example, a `calculate_total()` function can be called anywhere a total is needed.

## 3. How do you define a function?

Use the `def` keyword, followed by a function name, parentheses, and a colon. Indent the function body. A function body runs when the function is called, not merely when it is defined.

```python
def greet(name):
	message = f"Hello, {name}!"
	return message
```

The parameter list may be empty, and a `return` statement is optional. Function names conventionally use lowercase words separated by underscores.

## 4. How do you call a function?

Write the function name followed by parentheses. Supply any required arguments inside the parentheses.

```python
def greet(name):
	print(f"Hello, {name}!")

greet("Mina")
```

Defining `greet` creates the function; `greet("Mina")` calls it and executes its body. The call above prints `Hello, Mina!`.

## 5. What is a parameter?

A parameter is a name in a function definition that receives a value when the function is called. It acts as a local name within that function call.

```python
def double(value):
	return value * 2
```

`value` is a parameter. When `double(5)` is called, the parameter refers to the passed-in value `5` during that call.

## 6. What is an argument?

An argument is a value or expression supplied to a function when it is called.

```python
double(5)
```

In this call, `5` is the argument. An argument can be a literal, a variable, or an expression, such as `double(2 + 3)`.

## 7. Parameter vs argument?

A **parameter** appears in the function definition; an **argument** is supplied in the function call.

```python
def greet(name):  # name is a parameter
	print(f"Hello, {name}!")

greet("Mina")    # "Mina" is an argument
```

The parameter is the receiving name; the argument is the value or expression provided to that name.

## 8. What is the difference between `print()` and `return`?

`print()` displays text or a value, usually in the terminal. `return` ends the current function call and gives a value back to the caller, where it can be stored, combined, or used in another calculation.

```python
def add_and_print(a, b):
	print(a + b)  # displays the sum; the function itself returns None

def add_and_return(a, b):
	return a + b  # gives the sum back to the caller

result = add_and_return(2, 3)
print(result * 10)  # 50
```

Printing a result does not make that result the function's return value. A function can print and also return, but those are separate actions.

## 9. What happens if a function doesn’t have `return`?

When a function finishes without executing a `return` statement, Python returns `None` implicitly. A bare `return` also returns `None`.

```python
def show_message():
	print("Ready")

result = show_message()  # prints Ready
print(result)            # None
```

This is different from returning a displayed value: `print()` does not implicitly return what it prints.

## 10. Can a function return multiple values?

Yes. A function can return an expression containing multiple values. Python packages those values into a tuple, which callers can unpack into separate variables.

```python
def min_and_max(numbers):
	return min(numbers), max(numbers)

smallest, largest = min_and_max([4, 1, 9])
print(smallest, largest)  # 1 9
```

The function returns one tuple, `(1, 9)`, rather than multiple independent return objects. You can also receive it in one variable: `result = min_and_max([4, 1, 9])`.

## 11. What are default arguments?

A default argument is an argument whose parameter has a default value in the function definition. The caller may omit it; if omitted, the default is used.

```python
def greet(name, greeting="Hello"):
	print(f"{greeting}, {name}!")

greet("Mina")              # Hello, Mina!
greet("Mina", "Welcome")  # Welcome, Mina!
```

Parameters with defaults must follow parameters without defaults in the parameter list. Default values are evaluated once when the `def` statement runs, so avoid mutable defaults such as `items=[]`; use `None` and create a new list inside the function instead.

## 12. What are positional arguments?

Positional arguments are matched to parameters by their order in the call.

```python
def describe(name, age):
	print(f"{name} is {age} years old")

describe("Mina", 20)
```

Here, the first argument goes to `name` and the second goes to `age`. Changing their order can change the meaning of the call or cause a type or logic error.

## 13. What are keyword arguments?

Keyword arguments specify a parameter by name in the call, using `parameter=value`. Their order does not matter when each parameter is specified once.

```python
def describe(name, age):
	print(f"{name} is {age} years old")

describe(age=20, name="Mina")
```

Positional arguments can be combined with keyword arguments, but positional arguments must come first, and a parameter must not receive more than one value.

## 14. What is `*args`?

In a function definition, `*args` collects any extra positional arguments into a tuple. The name `args` is a convention; the `*` is what gives it this behavior.

```python
def add_all(*numbers):
	return sum(numbers)

print(add_all(2, 3, 5))  # 10
```

Here, `numbers` is the tuple `(2, 3, 5)`. A function can have regular parameters before `*args`. In a call, `*` can also unpack an iterable into positional arguments.

## 15. What is `**kwargs`?

In a function definition, `**kwargs` collects extra keyword arguments into a dictionary. The name `kwargs` is a convention; the two asterisks provide the behavior.

```python
def show_details(**details):
	for key, value in details.items():
		print(f"{key}: {value}")

show_details(name="Mina", age=20)
```

Inside the function, `details` is `{"name": "Mina", "age": 20}`. In a call, `**` can also unpack a dictionary into keyword arguments.

## 16. What is local scope?

Local scope is the scope associated with a function call. A name assigned inside a function is normally local to that function unless declared otherwise. It is not directly available outside the function.

```python
def calculate():
	total = 10
	return total

print(calculate())  # 10
# print(total)       # NameError: total is not defined here
```

Each function call has its own local execution context. A local variable can hide, or shadow, a global name with the same spelling inside that function.

## 17. What is global scope?

Global scope is the module-level scope: names assigned outside functions in a Python file are generally accessible throughout that module after they are defined.

```python
tax_rate = 0.1

def add_tax(price):
	return price * (1 + tax_rate)  # reads the global name
```

To reassign a module-level name from inside a function, declare it with `global`; this is usually best avoided in favor of passing values in and returning results. `global` is not needed just to read a global name. Python also has enclosing scopes for nested functions, and `nonlocal` can reassign a name in an enclosing function scope.

## 18. What is recursion?

Recursion is when a function calls itself, directly or indirectly, to solve a problem in smaller steps. A recursive function needs a **base case** that stops the calls; without one, calls continue until Python raises `RecursionError`.

```python
def factorial(number):
	if number < 0:
		raise ValueError("number must be non-negative")
	if number == 0:  # base case
		return 1
	return number * factorial(number - 1)

print(factorial(5))  # 120
```

Recursion can make naturally recursive problems clear, but it uses a call stack and Python does not optimize tail recursion. For many simple loops, iteration is more memory-efficient.

## 19. What is a lambda function?

A lambda is a small anonymous function created with the `lambda` keyword. Its body is a single expression, and that expression's value is returned automatically.

```python
square = lambda number: number * number
print(square(4))  # 16
```

Lambdas are useful for short functions passed to other functions, such as a sorting key: `sorted(words, key=lambda word: len(word))`. Use `def` for multi-step logic or when a descriptive function name improves readability.

## 20. What does it mean that functions are first-class objects in Python?

Functions are objects that can be treated like other values. You can assign a function to a variable, pass it as an argument, return it from another function, and store it in a data structure. Use the function name without parentheses when referring to the function itself; parentheses call it.

```python
def shout(text):
	return text.upper()

action = shout                 # assign the function object
print(action("hello"))         # call it through another name: HELLO

def apply(function, value):
	return function(value)     # receive and call a function

print(apply(shout, "hello"))   # HELLO
```

This property supports callbacks, decorators, and higher-order functions (functions that accept or return other functions).
