# Python Interview Questions and Answers

1. What is the difference between local and global variables in Python?

   A local variable is declared inside a function and can be used only inside that function. A global variable is declared outside any function and can be accessed throughout the program. Local variables are created when the function is called and destroyed when it exits. Global variables exist for the lifetime of the program unless modified or deleted. If we want to change a global variable inside a function, we use the `global` keyword.

   Example:
   ```python
   x = 10  # global variable

   def demo():
       y = 5  # local variable
       print(x, y)

   demo()
   ```

2. What is the difference between positional, keyword, and default arguments?

   Positional arguments are passed to a function in the same order as the parameters are defined. Keyword arguments are passed by name, so the order does not matter. Default arguments are parameters that already have a value, so the user does not need to pass them every time.

   Example:
   ```python
   def add(a, b=0):
       return a + b

   print(add(3, 4))      # positional arguments
   print(add(a=3, b=4))  # keyword arguments
   print(add(3))         # uses default b=0
   ```

3. *args and **kwargs: What are they, and when do we use them?

   `*args` collects extra positional arguments into a tuple. `**kwargs` collects extra keyword arguments into a dictionary. They are used when a function needs to accept a variable number of inputs.

   Example:
   ```python
   def show(*args, **kwargs):
       print(args)
       print(kwargs)

   show(1, 2, 3, name="Alice", age=25)
   ```

   `*args` is useful for unknown numbers of positional values, and `**kwargs` is useful for unknown named values.

4. What is the difference between return and print() in Python?

   `print()` displays output on the screen, but it does not send the value back to the program. `return` sends a value back from a function to the place where the function was called. The returned value can be stored in a variable or used in another expression.

   Example:
   ```python
   def add(a, b):
       return a + b

   result = add(3, 4)
   print(result)
   ```

   Here, `return` gives the result to the caller, while `print()` only shows it.

5. What is a lambda function in Python, and how is it different from a normal function?

   A lambda function is a small anonymous function written in one line using the `lambda` keyword. It is usually used for short operations. A normal function is defined using `def` and can contain multiple statements, a docstring, and more complex logic.

   Example:
   ```python
   square = lambda x: x * x
   print(square(5))
   ```

   Normal functions are better for reusable and complex logic, while lambda functions are suitable for quick, simple tasks such as sorting or filtering data.
