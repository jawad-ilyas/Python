# ✅ Python OOP Concepts – Expert Guide

This guide contains **expert-level Python OOP concepts** with practical examples, best practices, and outputs.

---

## 1. Operator Overloading

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)
```
```python
Vector(6, 8)
```

---

## 2. Method Resolution Order (MRO)

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass

d = D()
d.greet()
print(D.__mro__)  # Shows the method resolution order
```
```python
Hello from B
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

---

## 3. Descriptors

```python
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def __get__(self, instance, owner):
        print("Getting value")
        return self._temperature

    def __set__(self, instance, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        print("Setting value")
        self._temperature = value

class Thermometer:
    temp = Celsius()

thermo = Thermometer()
thermo.temp = 25
print(thermo.temp)
```
```python
Setting value
Getting value
25
```

---

## 4. Advanced Decorators

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello World!")

say_hello()
```
```python
Hello World!
Hello World!
Hello World!
```

---

## 5. Metaclasses

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
```
```python
Creating class MyClass
```

---

## 6. Abstract Base Classes (ABC) – Advanced

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

c = Car()
c.start()
```
```python
Car started
```

---

## 7. Singleton Design Pattern

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```
```python
True
```

---

## 8. Property Decorators with Validation (Advanced)

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

p = Person("Jawad", 25)
p.age = 30
print(p.age)
```
```python
30
```

---

## 9. Expert OOP Interview Questions

**Basics**

- Explain operator overloading with an example.  
- What is method resolution order (MRO) in Python?  
- What are descriptors and when are they used?  

**Advanced**

- Explain metaclasses and their use cases.  
- How do advanced decorators work with parameters?  
- Explain abstract base classes (ABC) and their importance.  
- How to implement Singleton and other design patterns in Python?  

**Best Practices**

- When to use private/protected attributes vs properties?  
- How to ensure OOP code is maintainable and scalable?  
- How to combine composition and inheritance effectively?  
