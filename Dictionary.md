# ✅ Python Dictionaries – Complete Practice & Interview Guide

This guide contains Python practice examples for **Dictionaries**, including their properties, creation, accessing values, updating, deleting, built-in functions, and differences compared to lists/tuples.

Dictionaries are:

- **Mutable** (can be changed)  
- **Unordered** (in Python < 3.7) / Ordered (Python >= 3.7)  
- **Key-value pairs**  
- Created using **curly braces `{}`**  

---

## 1. Dictionary Properties

```python
# Dictionary properties:
# 1. Mutable
# 2. Key-value pairs
# 3. Keys must be unique and immutable
# 4. Values can be of any type
```

---

## 2. Creating Dictionaries

### 2.1 Basic Dictionary
```python
person = {"name": "Jawad", "age": 25, "city": "Lahore"}
print(person)
```
```python
{'name': 'Jawad', 'age': 25, 'city': 'Lahore'}
```

### 2.2 Using dict() Constructor
```python
person = dict(name="Ali", age=30, city="Karachi")
print(person)
```
```python
{'name': 'Ali', 'age': 30, 'city': 'Karachi'}
```

### 2.3 Empty Dictionary
```python
empty_dict = {}
print(empty_dict)
```
```python
{}
```

---

## 3. Accessing Dictionary Elements

### 3.1 Using Keys
```python
person = {"name": "Jawad", "age": 25}
print(person["name"])
print(person["age"])
```
```python
Jawad
25
```

### 3.2 Using get() Method
```python
print(person.get("name"))
print(person.get("salary", "Not Found"))
```
```python
Jawad
Not Found
```

---

## 4. Updating Dictionary

### 4.1 Add or Update Key
```python
person["age"] = 26   # update
person["city"] = "Islamabad"  # add
print(person)
```
```python
{'name': 'Jawad', 'age': 26, 'city': 'Islamabad'}
```

### 4.2 Using update()
```python
person.update({"age": 27, "country": "Pakistan"})
print(person)
```
```python
{'name': 'Jawad', 'age': 27, 'city': 'Islamabad', 'country': 'Pakistan'}
```

---

## 5. Removing Elements

```python
person.pop("city")
print(person)
```
```python
{'name': 'Jawad', 'age': 27, 'country': 'Pakistan'}
```

```python
person.popitem()  # removes last inserted item
print(person)
```
```python
{'name': 'Jawad', 'age': 27}
```

```python
del person["age"]
print(person)
```
```python
{'name': 'Jawad'}
```

```python
person.clear()
print(person)
```
```python
{}
```

---

## 6. Dictionary Methods

### 6.1 keys(), values(), items()
```python
person = {"name": "Jawad", "age": 25}
print(person.keys())
print(person.values())
print(person.items())
```
```python
dict_keys(['name', 'age'])
dict_values([Jawad, 25])
dict_items([('name', 'Jawad'), ('age', 25)])
```

### 6.2 len()
```python
print(len(person))
```
```python
2
```

### 6.3 Nested Dictionary
```python
students = {
    "student1": {"name": "Ali", "age": 20},
    "student2": {"name": "Bilal", "age": 22}
}
print(students["student1"]["name"])
```
```python
Ali
```

---

## 7. Dictionary vs List/Tuple

| Feature        | Dictionary          | List/Tuple           |
|----------------|-------------------|--------------------|
| Mutability     | ✅ Mutable         | List ✅ / Tuple ❌  |
| Order          | Python >=3.7 Ordered | Ordered           |
| Access         | By key             | By index           |
| Syntax         | `{key: value}`     | `[] / ()`          |
| Use Case       | Key-value storage  | Sequence data      |

---

## 8. Full Dictionary Practice Example

```python
person = {"name": "Jawad", "age": 25, "city": "Lahore"}
print(person)
print("Name:", person["name"])
print("Length:", len(person))

person["age"] = 26
person["country"] = "Pakistan"
print("Updated:", person)

person.pop("city")
print("After pop:", person)

# Nested example
students = {
    "student1": {"name": "Ali", "age": 20},
    "student2": {"name": "Bilal", "age": 22}
}
print("Nested Example:", students["student2"]["name"])
```
```python
{'name': 'Jawad', 'age': 25, 'city': 'Lahore'}
Name: Jawad
Length: 3
Updated: {'name': 'Jawad', 'age': 26, 'city': 'Lahore', 'country': 'Pakistan'}
After pop: {'name': 'Jawad', 'age': 26, 'country': 'Pakistan'}
Nested Example: Bilal
```

---

## 9. Dictionary Interview Questions

**Basics**

- What are dictionaries in Python?  
- How are dictionaries different from lists and tuples?  
- Are dictionaries ordered or unordered?  
- Can dictionary keys be mutable?  

**Working with Dictionaries**

- How do you create a dictionary?  
- How do you access values using keys?  
- How do you update, add, and remove elements?  
- How do you iterate over keys, values, and items?  

**Advanced**

- What is a nested dictionary?  
- How can dictionaries be used in real-world scenarios?  
- How does dictionary performance compare to lists for lookups?  
