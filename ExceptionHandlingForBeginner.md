# ✅ Python Exception Handling – Beginner Guide

**Exception handling** in Python is a mechanism to **handle runtime errors** so that the program can continue executing instead of crashing.  

---

## 1. Basic try-except

```python
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter an integer.")
```
```python
# Example Input: abc
Invalid input! Please enter an integer.
```

---

## 2. Handling Multiple Exceptions

```python
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    print("Result:", result)
except ValueError:
    print("Invalid input! Please enter integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```
```python
# Example Input: 5, 0
Cannot divide by zero.
```

---

## 3. Using else

- The `else` block **executes if no exception occurs**.

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", num)
```
```python
# Example Input: 10
You entered: 10
```

---

## 4. Using finally

- The `finally` block **always executes**, regardless of exceptions.

```python
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input!")
finally:
    print("Execution complete.")
```
```python
# Example Input: abc
Invalid input!
Execution complete.
```

---

## 5. Raising Exceptions

- Use `raise` to **manually throw an exception**.

```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older")
    print("Access granted")

check_age(16)
```
```python
# ValueError: Age must be 18 or older
```

---

## 6. Custom Exception Class

```python
class MyError(Exception):
    pass

def test(value):
    if value < 0:
        raise MyError("Value cannot be negative")
    print("Value is:", value)

test(-5)
```
```python
# __main__.MyError: Value cannot be negative
```

---

## 7. Exception Handling Interview Questions

**Basics**

- What is exception handling in Python?  
- What is the difference between syntax errors and exceptions?  
- Why do we use try-except blocks?  

**Working with Exceptions**

- How do you handle multiple exceptions?  
- What is the purpose of `else` and `finally`?  
- How do you raise your own exceptions?  

**Advanced**

- What is a custom exception?  
- Can you catch all exceptions at once?  
- How can exception handling improve program reliability?
