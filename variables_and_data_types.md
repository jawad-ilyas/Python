# ✅ Python Variables & Data Types – Complete Practice & Interview Guide

This guide contains Python practice examples for **Variables and Data Types**, including types, type conversion, naming rules, and common operations.

---

## 1. Variables in Python

- A **variable** is a named location used to store data in memory.  
- Variables **do not require explicit declaration**; assignment automatically creates a variable.

```python
# Assigning values to variables
x = 10
name = "Jawad"
pi = 3.14
is_active = True

print(x)
print(name)
print(pi)
print(is_active)
```
```python
10
Jawad
3.14
True
```

---

## 2. Variable Naming Rules

- Must start with a letter or underscore (`_`).  
- Can contain letters, numbers, and underscores.  
- **Case-sensitive** (`name` and `Name` are different).  
- Cannot use **Python keywords** as variable names.

```python
# Valid variable names
_age = 25
user1 = "Ali"
Name = "Jawad"

# Invalid examples (will cause error)
# 1name = "Ali"
# class = "Python"
```

---

## 3. Data Types in Python

Python has several **built-in data types**:

- **Numeric:** int, float, complex  
- **Text:** str  
- **Boolean:** bool  
- **Sequence:** list, tuple, range  
- **Set Types:** set, frozenset  
- **Mapping:** dict  
- **Binary:** bytes, bytearray, memoryview  

---

## 4. Checking Data Types

```python
x = 10
y = 3.14
name = "Jawad"
is_active = True

print(type(x))
print(type(y))
print(type(name))
print(type(is_active))
```
```python
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

---

## 5. Type Conversion (Casting)

```python
x = 10       # int
y = 3.14     # float

# int to float
a = float(x)
# float to int
b = int(y)
# int to string
c = str(x)
# string to int
d = int("20")

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
```
```python
10.0 <class 'float'>
3 <class 'int'>
'10' <class 'str'>
20 <class 'int'>
```

---

## 6. Multiple Assignment

```python
# Assign same value to multiple variables
a = b = c = 10
print(a, b, c)

# Assign multiple values to multiple variables
x, y, z = 1, 2, 3
print(x, y, z)
```
```python
10 10 10
1 2 3
```

---

## 7. Constants in Python

- Python **does not have built-in constant types**.  
- By convention, **all uppercase variable names** are treated as constants.

```python
PI = 3.1416
GRAVITY = 9.8
print(PI, GRAVITY)
```
```python
3.1416 9.8
```

---

## 8. Type Hints (Optional)

- Python 3.5+ supports **type hints** to indicate expected data type.

```python
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old"

print(greet("Jawad", 25))
```
```python
Hello Jawad, you are 25 years old
```

---

## 9. Common Data Type Examples

### Numeric Types
```python
x = 10      # int
y = 3.14    # float
z = 2 + 3j  # complex
```

### Strings
```python
name = "Jawad"
message = 'Hello World'
multi_line = """This is
a multi-line string"""
```

### Boolean
```python
is_active = True
is_closed = False
```

### List
```python
numbers = [1, 2, 3, 4]
```

### Tuple
```python
coords = (10, 20)
```

### Set
```python
unique_numbers = {1, 2, 3, 4}
```

### Dictionary
```python
person = {"name": "Jawad", "age": 25}
```

---

## 10. Variables & Data Types Interview Questions

**Basics**

- What is a variable in Python?  
- What are the different data types in Python?  
- Are Python variables strongly typed or dynamically typed?  
- How do you check the type of a variable?  

**Working with Data Types**

- How do you convert one data type to another?  
- What is the difference between mutable and immutable data types?  
- What are sequences and mappings in Python?  
- How do multiple assignment and unpacking work?  

**Advanced**

- What are constants in Python? How are they represented?  
- How do type hints work and why are they useful?  
- Give examples of mutable vs immutable data types in Python.  
