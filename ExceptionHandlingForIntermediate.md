# ✅ Python Exception Handling – Intermediate Guide

Intermediate exception handling focuses on **advanced techniques** like nested exceptions, chaining, context managers, and logging for better error management in Python programs.

---

## 1. Nested try-except

- Use **nested try-except blocks** to handle exceptions at multiple levels.

```python
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    try:
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero (inner block)")
except ValueError:
    print("Invalid input (outer block)")
```
```python
# Example Input: 5, 0
Cannot divide by zero (inner block)
```

---

## 2. Exception Chaining

- Use `raise ... from` to **maintain original exception context**.

```python
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        raise ValueError("Invalid division") from e

divide(5, 0)
```
```python
# ValueError: Invalid division
# The original ZeroDivisionError is preserved in the traceback
```

---

## 3. Using `with` Statement (Context Managers)

- Ensures **resources are properly managed** (like files or network connections).  
- Automatically handles exceptions and cleanup.

```python
try:
    with open("nonexistent_file.txt", "r") as f:
        data = f.read()
except FileNotFoundError as e:
    print("File not found:", e)
```
```python
File not found: [Errno 2] No such file or directory: 'nonexistent_file.txt'
```

---

## 4. Logging Exceptions

- Use the `logging` module to **log exceptions** instead of printing.

```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    num = int("abc")
except ValueError as e:
    logging.error("An error occurred", exc_info=True)
```
```python
ERROR:root:An error occurred
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
ValueError: invalid literal for int() with base 10: 'abc'
```

---

## 5. Custom Exception Handling with Advanced Logic

```python
class NegativeNumberError(Exception):
    pass

def process_number(n):
    if n < 0:
        raise NegativeNumberError(f"Negative number not allowed: {n}")
    return n * 2

try:
    print(process_number(-10))
except NegativeNumberError as e:
    print("Custom Exception Caught:", e)
```
```python
Custom Exception Caught: Negative number not allowed: -10
```

---

## 6. Best Practices for Intermediate Exception Handling

- Always **catch specific exceptions** instead of using a generic `except:`.  
- Use **nested try-except** for layered error handling.  
- Log exceptions using `logging` for debugging in production.  
- Use **`finally` or context managers** to release resources reliably.  
- Raise **custom exceptions** for better readability and maintainability.

---

## 7. Intermediate Exception Handling Interview Questions

**Basics**

- How is exception chaining done in Python?  
- How do context managers help in exception handling?  

**Working with Exceptions**

- How can you log exceptions in Python?  
- Why is it better to catch specific exceptions rather than a generic `except`?  
- How do nested try-except blocks work?  

**Advanced**

- How do you create and use custom exceptions?  
- How can exception handling improve production-level Python applications?  
- Explain the difference between `raise` and `raise ... from`.
