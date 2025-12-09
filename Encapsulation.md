# ✅ Python Encapsulation – Complete Guide

Encapsulation is a key concept in **Object-Oriented Programming (OOP)**.  
It **restricts direct access** to some attributes and methods of a class to **protect the data**, usually using **private or protected variables**.  

---

## 1. Public Attributes

- Public attributes are accessible from **inside and outside the class**.  

```python
class Person:
    def __init__(self, name, age):
        self.name = name    # public
        self.age = age      # public

p = Person("Jawad", 25)
print(p.name)
print(p.age)

# Modify attributes
p.age = 30
print(p.age)
```
```python
Jawad
25
30
```

---

## 2. Protected Attributes

- Protected attributes are indicated by a **single underscore `_`**.  
- Can be accessed from subclasses but **should not be accessed directly outside the class**.  

```python
class Person:
    def __init__(self, name, age):
        self._name = name    # protected
        self._age = age      # protected

p = Person("Jawad", 25)
print(p._name)
print(p._age)
```
```python
Jawad
25
```

---

## 3. Private Attributes

- Private attributes are indicated by **double underscore `__`**.  
- **Cannot be accessed directly from outside the class**.  

```python
class Person:
    def __init__(self, name, age):
        self.__name = name    # private
        self.__age = age      # private

p = Person("Jawad", 25)
# print(p.__name)  # This will throw an error
```
```python
# AttributeError: 'Person' object has no attribute '__name'
```

---

## 4. Accessing Private Attributes (Getter & Setter)

```python
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

p = Person("Jawad", 25)
print(p.get_name())  # Access private attribute
p.set_age(30)        # Modify private attribute
```
```python
Jawad
```

---

## 5. Using Property Decorators

- Python provides **@property** to define **getter**  
- **@<property>.setter** to define **setter**  

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
print(p.age)
p.age = 30
print(p.age)
```
```python
25
30
```

---

## 6. Encapsulation Interview Questions

**Basics**

- What is encapsulation in Python?  
- How do public, protected, and private attributes differ?  
- Why is encapsulation important in OOP?  

**Working with Encapsulation**

- How do you access private attributes?  
- What are getter and setter methods?  
- How do property decorators simplify encapsulation?  

**Advanced**

- How does encapsulation help with data validation?  
- Can encapsulation prevent accidental changes to data?  
- Explain encapsulation with real-world examples.
