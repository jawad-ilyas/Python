# ✅ Python Classes & Objects – Complete Guide

**Classes** are blueprints for creating objects.  
**Objects** are instances of classes that can hold data and behavior.

---

## 1. Creating a Class

```python
class Person:
    pass  # Empty class
```

---

## 2. Creating an Object

```python
class Person:
    pass

# Create an object
p1 = Person()
print(type(p1))
```
```python
<class '__main__.Person'>
```

---

## 3. Instance Variables

- Attributes specific to each object.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Jawad", 25)
p2 = Person("Ali", 30)

print(p1.name, p1.age)
print(p2.name, p2.age)
```
```python
Jawad 25
Ali 30
```

---

## 4. Instance Methods

- Functions defined inside a class that operate on **instance data**.  

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p1 = Person("Jawad", 25)
p1.greet()
```
```python
Hello, my name is Jawad and I am 25 years old.
```

---

## 5. Class Variables

- Shared across all objects of the class.

```python
class Dog:
    species = "Canine"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

d1 = Dog("Buddy")
d2 = Dog("Charlie")

print(d1.name, d1.species)
print(d2.name, d2.species)
```
```python
Buddy Canine
Charlie Canine
```

---

## 6. Constructors (`__init__`)

- Special method that **initializes objects** at creation.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"Car: {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla")
car1.info()
```
```python
Car: Toyota Corolla
```

---

## 7. Object Methods with `self`

- `self` represents the **current object**.

```python
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(5, 3))
```
```python
8
```

---

## 8. Deleting Objects

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Jawad")
print(p.name)
del p
# print(p.name)  # This will raise an error
```
```python
Jawad
# NameError: name 'p' is not defined
```

---

## 9. Classes & Objects Interview Questions

**Basics**

- What is a class and an object?  
- How do you create an object in Python?  
- What is the purpose of the `__init__` constructor?  

**Working with Classes**

- What is the difference between class and instance variables?  
- What is `self` in Python?  
- How do you define instance methods?  

**Advanced**

- Can we have multiple constructors in Python?  
- How do you delete objects in Python?  
- How are classes and objects used in real-world applications?
