
# Python Lists Practice

## Introduction
This file contains Python exercises and examples for practicing **lists** and their associated methods. Lists in Python are:

- Ordered
- Mutable
- Dynamic
- Heterogeneous (can contain different data types)

The examples cover list creation, modification, concatenation, repetition, membership checking, copying, and common list methods.

---

## 1. Creating Lists

### Method 1: Using square brackets
```python
my_list = [1, 2, 3, "jawad", True]
print("List 1:", my_list)
```
**Explanation:** Creates a list with mixed data types.  
**Output:**
```
List 1: [1, 2, 3, 'jawad', True]
```

### Method 2: Using the `list()` constructor
```python
mylist2 = list((1, 2, 35, 20, "jawad", False))
print("List 2:", mylist2)
```
**Explanation:** Creates a list using the `list()` constructor with a tuple as input.  
**Output:**
```
List 2: [1, 2, 35, 20, 'jawad', False]
```

---

## 2. Accessing and Modifying Lists

### Accessing by index
```python
print("First element of list2:", mylist2[0])
```
**Explanation:** Accesses the first element of the list.  
**Output:**
```
First element of list2: 1
```

### Modifying by index
```python
changeList = [1, 2, 3, 4, 5]
print("Before:", changeList)

# Change the first element
changeList[0] = "list is changed using index"
print("After:", changeList)
```
**Output:**
```
Before: [1, 2, 3, 4, 5]
After: ['list is changed using index', 2, 3, 4, 5]
```

### Modifying by slice
```python
changeList[0:2] = 10, 20
print("After slice modification:", changeList)
```
**Output:**
```
After slice modification: [10, 20, 3, 4, 5]
```

---

## 3. Concatenation and Repetition
```python
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 11]

# Concatenate lists
result = list1 + list2
print("Concatenated list:", result)

# Repeat a list
listForRepeat = ["list is repeating"]
print("Repeated list:", listForRepeat * 3)
```
**Output:**
```
Concatenated list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
Repeated list: ['list is repeating', 'list is repeating', 'list is repeating']
```

---

## 4. Membership Checking
```python
listForIn = [1, 2, 3, 4, 5]

check = 3
if check in listForIn:
    print(f"{check} found")
else:
    print(f"{check} not found")

check = 10
if check not in listForIn:
    print(f"{check} not found")
else:
    print(f"{check} found")
```
**Output:**
```
3 found
10 not found
```

---

## 5. Copying Lists

### Shadow Copy
```python
listCopy = list1
listCopy[0] = "changed"
print("Original list after shadow copy modification:", list1)
```
**Explanation:** Both lists point to the same object; changes reflect in both.  

### Deep Copy
```python
list1Clone = list1.copy()
list1Clone[0] = "changed in clone"
print("Original list:", list1)
print("Cloned list:", list1Clone)
```
**Explanation:** Using `.copy()` creates an independent list.

---

## 6. Common List Methods

### Append
```python
list1.append("appended value")
print("After append:", list1)
```

### Extend
```python
a = [1, 2, 3, 4]
b = [3, 4, 2, 1]
a.extend(b)
print("After extend:", a)
```

### Insert
```python
b.insert(1, "inserted value")
print("After insert:", b)
```

### Remove
```python
b.remove(4)  # removes first occurrence of 4
print("After remove:", b)
```

### Pop
```python
popped_value = b.pop(0)
print("Popped value:", popped_value)
print("List after pop:", b)
```

### Clear
```python
a.clear()
print("After clear:", a)
```

### Index
```python
a = [1, 2, 43, 5, 6]
print("Index of 43:", a.index(43))
```

### Count
```python
j = [1, 2, 3, 4, 1, 1, 24, 5]
print("Count of 1 in list j:", j.count(1))
```

### Sort and Reverse
```python
a.sort()
print("Sorted list:", a)
a.reverse()
print("Reversed list:", a)
```

### Min and Max
```python
print("Min:", min(j))
print("Max:", max(j))
```

---

## 7. Common Elements using Sets
```python
s1 = set(a)
s2 = set(b)
common_elements = list(s1.intersection(s2))
print("Common elements:", common_elements)
```

---

## 8. Using `range()` Function
```python
numbers = list(range(0, 100, 5))
print("Numbers from 0 to 100 with step 5:", numbers)
```

---

## 9. List Comprehension
```python
square = [i ** 2 for i in range(1, 11, 2) if i % 2 != 0]
print("Squares of odd numbers from 1 to 10:", square)
```
**Explanation:**  
- Iterates over numbers 1 to 10 with step 2  
- Checks if the number is odd  
- Squares the number if condition is True  

**Output:**
```
Squares of odd numbers from 1 to 10: [1, 9, 25, 49, 81]
```

---

## Summary
This file demonstrates:

- List creation, modification, and slicing
- Concatenation, repetition, and membership checking
- Copying lists (shadow vs deep)
- Common list methods
- Using `range` and list comprehensions

These examples are perfect for practicing Python list operations.


# Python Lists - Interview Questions

## 1. Basics
- What are the key properties of a Python list?
- How is a Python list different from a tuple?
- Can a list store elements of different data types? Give an example.
- What is the difference between `[]` and `list()` when creating a list?

## 2. Access & Modification
- How do you access elements in a list using indexing and slicing?
- How can you modify a single element vs multiple elements in a list?
- What happens if you assign one list to another variable? Explain shadow copy vs deep copy.

## 3. Operations
- How do you concatenate two lists? How about repeating a list?
- How can you check if an element exists in a list? What is the difference between `in` and `not in`?
- How do you find the length of a list?

## 4. List Methods
- Explain the difference between `append()`, `extend()`, and `insert()` with examples.
- How do `remove()` and `pop()` differ?
- What does `clear()` do to a list?
- How do `index()` and `count()` methods work? Provide an example.
- How can you sort a list in ascending and descending order? How about reversing it?
- How do you find the minimum and maximum elements in a list?

## 5. Advanced Topics
- What is list comprehension and how is it different from a for-loop?
- How do you create a list using `range()`? Give an example with step size.
- How can you find common elements between two lists?
- Explain the difference between shallow copy and deep copy using examples.
- How do lists behave when used with mutable objects inside them? Give an example.

## 6. Practical/Scenario Questions
- Write a Python program to remove duplicates from a list.
- How would you merge two lists and sort the result in ascending order?
- How do you extract all odd numbers from a list using list comprehension?
- Explain how slicing works with negative indices in Python lists.
- How would you implement a stack using Python lists? Which methods would you use?

## 7. Conceptual Questions
- Why are lists mutable but tuples are not? What are the implications?
- When would you use a list over other data structures like sets or dictionaries?
- How does Python internally handle dynamic resizing of lists?
- Explain the time complexity of common list operations (indexing, append, insert, remove).
