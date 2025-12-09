# ✅ Python Beginner Concepts – Complete Guide

This guide contains all essential **Python beginner concepts** with practice examples, outputs, and interview questions.

---

## 1. Variables & Data Types

```python
# Variables
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

### Checking Data Types

```python
print(type(x))
print(type(name))
print(type(pi))
print(type(is_active))
```
```python
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
```

### Type Conversion

```python
a = float(x)
b = int(pi)
c = str(x)
print(a, b, c)
```
```python
10.0 3 '10'
```

---

## 2. Operators

```python
x = 10
y = 3

# Arithmetic
print(x + y, x - y, x * y, x / y, x // y, x % y, x ** y)

# Comparison
print(x == y, x != y, x > y, x < y, x >= y, x <= y)

# Logical
print(x > 5 and y < 5, x > 5 or y > 5, not(x > y))
```
```python
13 7 30 3.3333333333333335 3 1 1000
False True True False True False
True True False
```

---

## 3. Strings

```python
text = "Python"
print(text[0], text[-1])
print(text[1:4])
print(text[::-1])

name = "Jawad"
age = 25
print(f"My name is {name} and I am {age} years old")
```
```python
P n
yth
nohtyP
My name is Jawad and I am 25 years old
```

---

## 4. Tuples

```python
numbers_tuple = (10, 20, 30)
mixed_tuple = (1, "Jawad", True, 3.5)

print(numbers_tuple)
print(mixed_tuple)
print(numbers_tuple[0])
```
```python
(10, 20, 30)
(1, 'Jawad', True, 3.5)
10
```

---

## 5. Dictionaries

```python
person = {"name": "Jawad", "age": 25}
print(person["name"])
print(person.get("age"))

person["city"] = "Lahore"
print(person)
```
```python
Jawad
25
{'name': 'Jawad', 'age': 25, 'city': 'Lahore'}
```

---

## 6. Control Statements

```python
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

for i in range(1, 4):
    print(i)

i = 1
while i <= 3:
    print(i)
    i += 1
```
```python
x is greater than 5
1
2
3
1
2
3
```

---

## 7. Functions

```python
def greet(name="Guest"):
    """Function to greet a person"""
    print(f"Hello, {name}!")

greet()
greet("Jawad")

def add(a, b):
    return a + b

print(add(5, 3))
```
```python
Hello, Guest!
Hello, Jawad!
8
```

### Advanced Function Examples

```python
# Lambda Function
square = lambda x: x ** 2
print(square(5))

# Decorator
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def say_hello():
    print("Hello World!")

say_hello()
```
```python
25
Before function
Hello World!
After function
```

---

## 8. Lambda Functions

```python
add = lambda a, b: a + b
print(add(10, 5))

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
```
```python
15
[1, 4, 9, 16, 25]
[2, 4]
```

---

## 9. Interview Questions

**Variables & Data Types**

- What are Python variables?  
- Difference between mutable and immutable data types?  
- How to check type and convert data types?  

**Operators**

- Difference between `/` and `//`?  
- How do logical operators work in Python?  

**Strings**

- How do string indexing and slicing work?  
- What is string concatenation and formatting?  

**Tuples & Dictionaries**

- Difference between tuple and list?  
- How do you access, add, or update dictionary elements?  

**Control Statements**

- Difference between `if-else` and `if-elif-else`?  
- How do `break`, `continue`, and `pass` work?  

**Functions & Lambda**

- Difference between a regular function and lambda function?  
- What are decorators and generators?  
- How do default, positional, keyword, *args, **kwargs work?  
