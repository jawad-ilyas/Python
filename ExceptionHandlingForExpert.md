# ✅ Python Exception Handling – Expert Guide

Expert-level exception handling focuses on **robust error management** in complex applications, using **custom hierarchies, context managers, logging, and retry strategies**.

---

## 1. Custom Exception Hierarchies

- Create a **base exception class** and derive specialized exceptions for better structure.

```python
class AppError(Exception):
    """Base class for all application-specific errors"""
    pass

class DatabaseError(AppError):
    """Raised for database-related errors"""
    pass

class NetworkError(AppError):
    """Raised for network-related errors"""
    pass

def connect_to_db():
    raise DatabaseError("Database connection failed")

try:
    connect_to_db()
except AppError as e:
    print("Application Error Caught:", e)
```
```python
Application Error Caught: Database connection failed
```

---

## 2. Advanced Context Managers (`contextlib`)

- Custom context managers for **resource management**.

```python
from contextlib import contextmanager

@contextmanager
def managed_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()
        print(f"{filename} closed.")

with managed_file("example.txt", "w") as f:
    f.write("Hello World!")
```
```python
example.txt closed.
```

---

## 3. Retry Logic with Exceptions

- Automatically retry operations on transient errors.

```python
import time

def retry(func, retries=3, delay=1):
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    raise Exception("All retries failed")

count = 0
def flaky_operation():
    global count
    count += 1
    if count < 3:
        raise ValueError("Temporary failure")
    return "Success"

result = retry(flaky_operation)
print(result)
```
```python
Attempt 1 failed: Temporary failure
Attempt 2 failed: Temporary failure
Success
```

---

## 4. Logging Exceptions in Production

- Integrate **exception handling with logging** for monitoring.

```python
import logging

logging.basicConfig(filename="app.log", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("Division error occurred", exc_info=True)
```
```python
# Logs detailed traceback in 'app.log'
```

---

## 5. Chaining Exceptions for Debugging

- Preserve original exception context for better debugging.

```python
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        raise RuntimeError("Division failed") from e

try:
    divide(5, 0)
except RuntimeError as e:
    print(e)
```
```python
Division failed
```

---

## 6. Best Practices for Expert Exception Handling

- **Create a structured hierarchy** for custom exceptions.  
- **Use context managers** for all resources (files, DB connections).  
- **Log exceptions** with full traceback for debugging.  
- **Use retry logic** for transient operations (network, DB).  
- **Use exception chaining** (`raise ... from`) to preserve context.  
- Catch **specific exceptions**; avoid bare `except:`.  
- Fail fast in production while giving meaningful error messages.

---

## 7. Expert Exception Handling Interview Questions

**Advanced Concepts**

- How do you design a custom exception hierarchy?  
- What is exception chaining and why is it important?  
- How do context managers simplify exception handling?  
- How can retry logic be implemented with exceptions?  
- How do you integrate logging with exception handling in production systems?  

**Practical Applications**

- Explain exception handling strategies for distributed systems.  
- How do you ensure resources are safely released in Python?  
- How can exception handling improve maintainability and reliability in large codebases?
