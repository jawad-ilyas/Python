# ✅ Python Inheritance – Complete Guide

**Inheritance** is a core concept of **OOP** that allows a class (child/subclass) to **inherit attributes and methods** from another class (parent/superclass).  
It promotes **code reuse** and **modularity**.

---

## 1. Single Inheritance

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    pass

c = Child()
c.greet()
```
```python
Hello from Parent
```

---

## 2. Method Overriding

- Child class can **override parent methods**.  

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

c = Child()
c.greet()
```
```python
Hello from Child
```

---

## 3. Using `super()`

- `super()` allows access to **parent methods** from the child class.  

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

c = Child()
c.greet()
```
```python
Hello from Parent
Hello from Child
```

---

## 4. Multilevel Inheritance

```python
class Grandparent:
    def greet(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

c = Child()
c.greet()
```
```python
Hello from Grandparent
```

---

## 5. Multiple Inheritance

- A child class inherits from **more than one parent class**.  

```python
class Mother:
    def skills(self):
        print("Cooking")

class Father:
    def skills(self):
        print("Driving")

class Child(Mother, Father):
    pass

c = Child()
c.skills()
```
```python
Cooking
```
> **Note:** Python uses **Method Resolution Order (MRO)**. The method of the first parent class is called.

---

## 6. Hierarchical Inheritance

- Multiple child classes inherit from **one parent class**.  

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()
c1.greet()
c2.greet()
```
```python
Hello from Parent
Hello from Parent
```

---

## 7. Inheritance Interview Questions

**Basics**

- What is inheritance in Python?  
- What are the benefits of using inheritance?  

**Types of Inheritance**

- Explain single, multiple, multilevel, and hierarchical inheritance with examples.  
- What is method overriding and why is it used?  
- How does `super()` work in Python?  

**Advanced**

- What is Method Resolution Order (MRO)?  
- How does Python handle multiple inheritance conflicts?  
- Can a child class inherit from an abstract base class?  
