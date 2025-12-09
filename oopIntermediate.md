# ✅ Python OOP Concepts – Intermediate Guide

This guide contains **intermediate-level Python OOP concepts** with practical examples and outputs.

---

## 1. Multiple Inheritance

```python
class Person:
    def greet(self):
        print("Hello from Person")

class Employee:
    def work(self):
        print("Working...")

class Manager(Person, Employee):
    pass

m = Manager()
m.greet()
m.work()
```
```python
Hello from Person
Working...
```

---

## 2. Method Overriding

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()
```
```python
Dog barks
```

---

## 3. Property Decorators

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            print("Radius must be positive")

c = Circle(5)
print(c.radius)
c.radius = 10
print(c.radius)
```
```python
5
10
```

---

## 4. Dunder (Magic) Methods

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return len(self.title)

book = Book("Python Intermediate", "Jawad")
print(book)
print(len(book))
```
```python
Python Intermediate by Jawad
19
```

---

## 5. Abstraction (Using `abc` Module)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(5, 3)
print(r.area())
```
```python
15
```

---

## 6. Encapsulation with Private & Protected Attributes

```python
class Person:
    def __init__(self, name, age):
        self._name = name       # protected
        self.__age = age        # private

    def get_age(self):
        return self.__age

p = Person("Jawad", 25)
print(p._name)       # Accessible but should not be modified
print(p.get_age())   # Access private attribute via method
```
```python
Jawad
25
```

---

## 7. Class & Static Methods (Intermediate Usage)

```python
class Employee:
    company_name = "TechCorp"

    def __init__(self, name):
        self.name = name

    @classmethod
    def set_company(cls, name):
        cls.company_name = name

    @staticmethod
    def greet():
        print("Welcome to the company!")

e = Employee("Ali")
Employee.greet()
Employee.set_company("NewTech")
print(Employee.company_name)
```
```python
Welcome to the company!
NewTech
```

---

## 8. Composition (Has-A Relationship)

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car is ready to go")

my_car = Car()
my_car.start()
```
```python
Engine started
Car is ready to go
```

---

## 9. Polymorphism (Advanced)

```python
class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane:
    def fly(self):
        print("Airplane can fly")

def lift(obj):
    obj.fly()

b = Bird()
a = Airplane()
lift(b)
lift(a)
```
```python
Bird can fly
Airplane can fly
```

---

## 10. Intermediate OOP Interview Questions

**Basics**

- What is multiple inheritance and how is it handled in Python?  
- How do you override methods in Python?  

**Working with OOP**

- How do `@property`, `@staticmethod`, and `@classmethod` differ?  
- Explain private vs protected attributes and encapsulation.  
- What is the purpose of dunder (magic) methods like `__str__` and `__len__`?  

**Advanced**

- How does abstraction work using the `abc` module?  
- Explain composition (has-a) vs inheritance (is-a).  
- How is polymorphism implemented in Python?  
