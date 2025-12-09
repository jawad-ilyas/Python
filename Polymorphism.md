# ✅ Python Polymorphism – Complete Guide

**Polymorphism** is an OOP concept that allows objects of **different classes to be treated uniformly**.  
It enables **flexible and reusable code**.

---

## 1. Method Overriding (Runtime Polymorphism)

- Child class can **override a parent method** while keeping the same method name.  

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Runtime polymorphism
def make_sound(animal):
    animal.speak()

d = Dog()
c = Cat()

make_sound(d)
make_sound(c)
```
```python
Dog barks
Cat meows
```

---

## 2. Operator Overloading (Compile-time Polymorphism)

- Python allows you to **define behavior for operators** in your classes.  

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
print(p3)
```
```python
Point(6, 8)
```

---

## 3. Duck Typing (Dynamic Polymorphism)

- **“If it looks like a duck and quacks like a duck, it’s a duck”** – Python uses **duck typing** instead of strict type checking.  

```python
class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def lift(obj):
    obj.fly()

b = Bird()
a = Airplane()

lift(b)
lift(a)
```
```python
Bird is flying
Airplane is flying
```

---

## 4. Polymorphism with Inheritance

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    print(shape.area())
```
```python
15
50.24
```

---

## 5. Polymorphism Interview Questions

**Basics**

- What is polymorphism in Python?  
- Explain runtime and compile-time polymorphism with examples.  

**Working with Polymorphism**

- What is method overriding?  
- How does operator overloading work in Python?  
- Explain duck typing in Python with an example.  

**Advanced**

- How does polymorphism improve code flexibility?  
- How does polymorphism work with abstract base classes?  
- Difference between polymorphism and inheritance.  
