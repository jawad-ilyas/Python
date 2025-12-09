# ✅ Python OOP Concepts – Beginner Guide

This guide contains beginner-friendly examples of **Object-Oriented Programming (OOP) in Python**, including **classes, objects, methods, inheritance, encapsulation, and polymorphism**.

---

## 1. Classes and Objects

```python
# Define a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create objects
person1 = Person("Jawad", 25)
person2 = Person("Ali", 30)

# Call methods
person1.greet()
person2.greet()
```
```python
Hello, my name is Jawad and I am 25 years old.
Hello, my name is Ali and I am 30 years old.
```

---

## 2. Constructor (`__init__`)

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

## 3. Instance Variables vs Class Variables

```python
class Dog:
    species = "Canine"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

print(dog1.name, dog1.species)
print(dog2.name, dog2.species)
```
```python
Buddy Canine
Charlie Canine
```

---

## 4. Methods in Classes

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 6))
```
```python
8
24
```

---

## 5. Inheritance

```python
# Base class
class Animal:
    def speak(self):
        print("Animal speaks")

# Derived class
class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()
```
```python
Dog barks
```

---

## 6. Encapsulation

```python
class Person:
    def __init__(self, name, age):
        self.__name = name   # private attribute
        self.__age = age     # private attribute

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age > 0:
            self.__age = age

person = Person("Jawad", 25)
print(person.get_name())
person.set_age(30)
```
```python
Jawad
```

---

## 7. Polymorphism

```python
class Cat:
    def speak(self):
        print("Cat meows")

class Dog:
    def speak(self):
        print("Dog barks")

def animal_sound(animal):
    animal.speak()

cat = Cat()
dog = Dog()

animal_sound(cat)
animal_sound(dog)
```
```python
Cat meows
Dog barks
```

---

## 8. Special Methods

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

book = Book("Python Basics", "Jawad")
print(book)
```
```python
Python Basics by Jawad
```

---

## 9. Class & Static Methods

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def info(cls):
        print(f"This is class {cls.__name__}")

print(Math.add(5, 3))
Math.info()
```
```python
8
This is class Math
```

---

## 10. OOP Interview Questions

**Basics**

- What is OOP and its main principles?  
- What is a class and object?  
- What is the purpose of the `__init__` method?  

**Working with OOP**

- Difference between instance and class variables?  
- How does inheritance work in Python?  
- What is encapsulation and how do you implement it?  
- What is polymorphism and give an example?  

**Advanced**

- What are special methods (`__str__`, `__repr__`, `__len__`, etc.)?  
- Difference between `@staticmethod` and `@classmethod`?  
- How do you override methods in Python?
