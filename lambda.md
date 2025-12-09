# ✅ Python Lambda Functions – Complete Practice & Interview Guide

This guide contains Python practice examples for **Lambda Functions** in Python, including syntax, use cases, and advanced examples.

---

## 1. What is a Lambda Function?

- A **lambda function** is a **small anonymous function**.  
- Can take **any number of arguments** but only **one expression**.  
- Syntax:

```python
lambda arguments: expression
```

---

## 2. Basic Lambda Function

```python
square = lambda x: x ** 2
print(square(5))
```
```python
25
```

---

## 3. Lambda with Multiple Arguments

```python
add = lambda a, b: a + b
print(add(10, 15))
```
```python
25
```

---

## 4. Lambda Inside a Function

```python
def make_incrementer(n):
    return lambda x: x + n

increment_by_5 = make_incrementer(5)
print(increment_by_5(10))
```
```python
15
```

---

## 5. Using Lambda with `map()`

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)
```
```python
[1, 4, 9, 16, 25]
```

---

## 6. Using Lambda with `filter()`

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
```
```python
[2, 4]
```

---

## 7. Using Lambda with `reduce()`

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)
```
```python
120
```

---

## 8. Sorting with Lambda

```python
students = [("Ali", 25), ("Bilal", 22), ("Jawad", 24)]
# Sort by age
students_sorted = sorted(students, key=lambda x: x[1])
print(students_sorted)
```
```python
[('Bilal', 22), ('Jawad', 24), ('Ali', 25)]
```

---

## 9. Lambda vs Regular Function

```python
# Regular function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

print(square(5))
print(square_lambda(5))
```
```python
25
25
```

---

## 10. Lambda Function Interview Questions

**Basics**

- What is a lambda function in Python?  
- What are the differences between a lambda and a regular function?  

**Working with Lambda**

- How do you use lambda functions with `map()`, `filter()`, and `reduce()`?  
- Can a lambda function have multiple arguments?  
- Can a lambda function contain statements?  

**Advanced**

- How do you use lambda inside another function?  
- Give an example of sorting a list of tuples using lambda.  
- When is it better to use a lambda function instead of a regular function?  
