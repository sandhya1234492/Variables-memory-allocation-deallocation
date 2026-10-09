# Basic Python Programs

## 1. Reverse a String

This program builds the reversed string one character at a time without using a
built-in reverse function.

```python
text = input("Enter a string: ")
reversed_text = ""

for character in text:
    reversed_text = character + reversed_text

print("Reversed string:", reversed_text)
```

## 2. Check Whether a Number Is a Palindrome

A palindrome number reads the same forwards and backwards. Negative numbers
are not considered palindromes by this program.

```python
number = int(input("Enter a number: "))
original_number = number
reversed_number = 0

if number >= 0:
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

if original_number >= 0 and original_number == reversed_number:
    print("Palindrome number")
else:
    print("Not a palindrome number")
```

## 3. Find the Largest Number in a List

This program compares each list item with the current largest value. It does
not use `max()`.

```python
numbers = [12, 45, 7, 89, 34]

if not numbers:
    print("The list is empty.")
else:
    largest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number

    print("Largest number:", largest)
```

## 4. Count Vowels in a String

The string is converted to lowercase so both uppercase and lowercase vowels
are counted.

```python
text = input("Enter a string: ")
vowel_count = 0

for character in text.lower():
    if character in "aeiou":
        vowel_count += 1

print("Number of vowels:", vowel_count)
```

## 5. Calculate the Factorial of a Number

The factorial function multiplies all positive integers up to the given
number. Zero factorial is 1; negative numbers are rejected.

```python
def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for value in range(1, number + 1):
        result *= value

    return result


number = int(input("Enter a non-negative integer: "))
print("Factorial:", factorial(number))
```