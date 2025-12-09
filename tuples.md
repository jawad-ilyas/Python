# ✅ Python Tuples – Complete Practice & Interview Guide

This guide contains Python practice examples for **Tuples**, including their properties, creation, accessing values, unpacking, built-in functions, and differences compared to lists.

Tuples are:

- **Immutable** (cannot be changed)  
- **Ordered**  
- **Heterogeneous**  
- Created using **parentheses `()`**

---

## 1. Tuple Properties

```python
# Tuple properties:
# 1. Immutable
# 2. Ordered
# 3. Heterogeneous
# 4. Uses parentheses ()
```

---

## 2. Creating Tuples

### 2.1 Basic Tuple
```python
numbers_tuple = (10, 20, 30)
print(numbers_tuple)
```
```python
(10, 20, 30)
```

### 2.2 Heterogeneous Tuple
```python
mixed_tuple = (1, "Jawad", True, 3.5)
print(mixed_tuple)
```
```python
(1, 'Jawad', True, 3.5)
```

### 2.3 Tuple Packing
```python
packed = 5, 10, 15
print(packed)
```
```python
(5, 10, 15)
```

### 2.4 Single-element Tuple
```python
single = (10,)
print(single)
```
```python
(10,)
```

---

## 3. Accessing Tuple Elements

```python
a = (10, 20, 30)
print(a[0])
print(a[1])
print(a[-1])
```
```python
10
20
30
```

---

## 4. Tuple Methods & Built-in Functions

### 4.1 len()
```python
print(len((10, 20, 30)))
```
```python
3
```

### 4.2 count()
```python
tuple_data = (1, 2, 2, 3, 2, 4)
print(tuple_data.count(2))
```
```python
3
```

### 4.3 index()
```python
names = ("Ali", "Bilal", "Jawad", "Ali")
print(names.index("Jawad"))
```
```python
2
```

### 4.4 min() and max()
```python
values = (5, 10, 2, 8)
print(min(values))
print(max(values))
```
```python
2
10
```

### 4.5 sorted()
```python
values = (4, 1, 3, 2)
sorted_list = sorted(values)
print(sorted_list)
```
```python
[1, 2, 3, 4]
```

---

## 5. Tuple Unpacking

```python
a, b, c = (10, 20, 30)
print(a, b, c)
```
```python
10 20 30
```

---

## 6. Nested Tuples

```python
nested = (10, (20, 30), ("A", "B"))
print(nested[1][0])
print(nested[2][1])
```
```python
20
B
```

---

## 7. Tuple vs List

| Feature       | Tuple           | List        |
|---------------|----------------|------------|
| Mutability    | ❌ Immutable    | ✅ Mutable  |
| Performance   | Faster          | Slower     |
| Syntax        | `()`            | `[]`       |
| Use Case      | Constant/Fixed data | Dynamic data |

---

## 8. Full Tuple Practice Example

```python
my_tuple = (10, 20, 30, 40)

print("Tuple:", my_tuple)
print("First Element:", my_tuple[0])
print("Length:", len(my_tuple))
print("Max Value:", max(my_tuple))
print("Min Value:", min(my_tuple))

a, b, c, d = my_tuple
print("Unpacked:", a, b, c, d)

nested = (1, (2, 3), (4, 5))
print("Nested Example:", nested[1][1])
```
```python
Tuple: (10, 20, 30, 40)
First Element: 10
Length: 4
Max Value: 40
Min Value: 10
Unpacked: 10 20 30 40
Nested Example: 3
```

---

## 9. Tuple Interview Questions

**Basics**

- What are tuples in Python?  
- How are tuples different from lists?  
- Are tuples mutable or immutable?  
- Can tuples store different data types?  

**Working with Tuples**

- How do you create a single-element tuple?  
- How do you access elements in a tuple?  
- What is tuple packing and unpacking?  
- How do you find the length of a tuple?  

**Functions & Methods**

- What does `index()` do in a tuple?  
- What is the difference between `count()` and `index()`?  
- Can we sort a tuple directly? Why / Why not?  

**Scenario / Practical**

- When would you choose a tuple instead of a list?  
- How can a tuple be used as a dictionary key?  
- Demonstrate tuple unpacking with an example.  

**Advanced**

- Can tuples contain other tuples? Give an example.  
- How does immutability affect tuple performance?  
- How do nested tuples work?
