# ✅ Python Functions – Complete Practice & Interview Guide

This guide contains Python practice examples for **Functions**, including creation, types of parameters, return values, scope, and lambda functions.

---

## 1. Defining a Function

```python
def greet():
    """This function prints a greeting"""
    print("Hello, Jawad!")

greet()
```
```python
Hello, Jawad!
```

---

## 2. Function Parameters

### 2.1 Positional Arguments
```python
def greet(name, age):
    print(f"My name is {name} and I am {age} years old")

greet("Jawad", 25)
```
```python
My name is Jawad and I am 25 years old
```

### 2.2 Keyword Arguments
```python
greet(age=25, name="Jawad")
```
```python
My name is Jawad and I am 25 years old
```

### 2.3 Default Arguments
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Ali")
```
```python
Hello, Guest!
Hello, Ali!
```

### 2.4 Arbitrary Arguments (*args)
```python
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1, 2, 3, 4))
```
```python
10
```

### 2.5 Arbitrary Keyword Arguments (**kwargs)
```python
def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person_info(name="Jawad", age=25, city="Lahore")
```
```python
name: Jawad
age: 25
city: Lahore
```

---

## 3. Return Statement

```python
def square(x):
    return x ** 2

result = square(5)
print(result)
```
```python
25
```

---

## 4. Lambda (Anonymous) Functions

```python
square = lambda x: x ** 2
print(square(6))

add = lambda a, b: a + b
print(add(5, 3))
```
```python
36
8
```

---

## 5. Scope of Variables

```python
x = 10  # global variable

def test():
    y = 5  # local variable
    print("Inside function:", x, y)

test()
print("Outside function:", x)
```
```python
Inside function: 10 5
Outside function: 10
```

---

## 6. Nested Functions

```python
def outer():
    print("Outer function")

    def inner():
        print("Inner function")
    
    inner()

outer()
```
```python
Outer function
Inner function
```

---

## 7. Function Annotations (Optional)

```python
def greet(name: str, age: int) -> str:
    return f"My name is {name} and I am {age} years old"

print(greet("Jawad", 25))
```
```python
My name is Jawad and I am 25 years old
```

---

## 8. Recursion

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
```
```python
120
```

---

## 9. Functions Interview Questions

**Basics**

- What is a function in Python?  
- How do you define and call a function?  
- What is the difference between parameters and arguments?  

**Working with Functions**

- Explain positional, keyword, default, *args, and **kwargs parameters.  
- How do return values work in functions?  
- What is a lambda function and when is it used?  

**Advanced**

- What is the scope of variables (local, global, nonlocal)?  
- Explain nested functions.  
- How does recursion work in Python?  
- What are function annotations? How are they useful?  


## 10. Advanced Function Topics

### 10.1 Docstrings

```python
def greet():
    """
    This function prints a greeting
    """
    print("Hi Jawad Mughal")

greet()
print(greet.__doc__)  # Access the docstring
```
```python
Hi Jawad Mughal
This function prints a greeting
```

---

### 10.2 Keyword & Default Arguments

```python
def greet(name="Unknown", city="Unknown City"):
    print(f"Welcome {name} to {city}")

# Keyword arguments (order doesn't matter)
greet(city="Lahore", name="Jawad")
# Using defaults
greet()
```
```python
Welcome Jawad to Lahore
Welcome Unknown to Unknown City
```

---

### 10.3 Return Statement

```python
def full_name(firstname, lastname):
    fullName = f"{firstname} {lastname}"
    return fullName

name = full_name("Jawad", "Ilyas")
print(name)
```
```python
Jawad Ilyas
```

---

### 10.4 Local vs Global Variables

```python
choice = "Global Choice"

def msg(choice):
    # 'choice' here is local to the function
    print("Inside function:", choice)

msg("Local Choice")
print("Outside function:", choice)
```
```python
Inside function: Local Choice
Outside function: Global Choice
```

---

### 10.5 Decorators

```python
def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello from the function!")

say_hello()
```
```python
Before the function
Hello from the function!
After the function
```

---

### 10.6 Generators (Yield)

```python
def count_down(num):
    while num > 0:
        yield num
        num -= 1

for n in count_down(5):
    print(n)
```
```python
5
4
3
2
1
```

---

### 10.7 Function Interview Questions (Advanced)

- What is a docstring and how do you access it?  
- How do keyword and default arguments work?  
- What is the difference between local and global variables?  
- What are decorators and why are they useful?  
- What is a generator and how does `yield` differ from `return`?  
