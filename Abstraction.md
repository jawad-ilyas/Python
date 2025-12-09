# ✅ Python Abstraction – Complete Guide

**Abstraction** in OOP is the concept of **hiding the internal implementation** and showing only the **essential features** of an object.  
In Python, abstraction is implemented using **abstract classes** and **abstract methods** from the `abc` module.

---

## 1. Abstract Classes

- Abstract classes **cannot be instantiated**.  
- They provide a **blueprint for other classes**.  

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

# v = Vehicle()  # This will raise an error
```
```python
# TypeError: Can't instantiate abstract class Vehicle with abstract methods start
```

---

## 2. Abstract Methods

- Abstract methods are **methods without implementation**.  
- Subclasses **must override** abstract methods.  

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

c = Car()
b = Bike()

c.start()
b.start()
```
```python
Car started
Bike started
```

---

## 3. Partially Implemented Abstract Classes

- Abstract classes can also have **implemented methods** along with abstract methods.  

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print("This is a geometric shape.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(5, 3)
print(r.area())
r.describe()
```
```python
15
This is a geometric shape.
```

---

## 4. Why Use Abstraction?

- To **hide unnecessary details** from the user.  
- To **enforce a contract** for subclasses (all subclasses must implement abstract methods).  
- Makes code **modular, reusable, and maintainable**.

---

## 5. Abstraction Interview Questions

**Basics**

- What is abstraction in Python?  
- How is abstraction implemented in Python?  
- Can you instantiate an abstract class?  

**Working with Abstraction**

- What are abstract methods?  
- What happens if a subclass does not implement all abstract methods?  
- Can abstract classes have regular (non-abstract) methods?  

**Advanced**

- Difference between abstraction and encapsulation?  
- How does abstraction help in large projects?  
- Provide a real-world example of abstraction.
