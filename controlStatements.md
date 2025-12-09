# ✅ Python Control Statements – Complete Practice & Interview Guide

This guide contains Python practice examples for **Control Statements**, including conditional statements, loops, and control flow tools.

---

## 1. If Statement

```python
x = 10

if x > 5:
    print("x is greater than 5")
```
```python
x is greater than 5
```

---

## 2. If-Else Statement

```python
x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
```
```python
x is less than or equal to 5
```

---

## 3. If-Elif-Else Statement

```python
x = 10

if x < 5:
    print("x is less than 5")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is greater than 5 but not 10")
```
```python
x is equal to 10
```

---

## 4. Nested If Statements

```python
x = 15

if x > 10:
    if x % 2 == 0:
        print("x is greater than 10 and even")
    else:
        print("x is greater than 10 and odd")
```
```python
x is greater than 10 and odd
```

---

## 5. Loops

### 5.1 While Loop

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```
```python
1
2
3
4
5
```

### 5.2 For Loop (using range)

```python
for i in range(1, 6):
    print(i)
```
```python
1
2
3
4
5
```

### 5.3 For Loop (iterating over a list)

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
```python
apple
banana
cherry
```

---

## 6. Break, Continue, and Pass

### 6.1 Break Statement
```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```
```python
1
2
```

### 6.2 Continue Statement
```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```
```python
1
2
4
5
```

### 6.3 Pass Statement
```python
for i in range(1, 4):
    if i == 2:
        pass  # do nothing
    print(i)
```
```python
1
2
3
```

---

## 7. Nested Loops

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```
```python
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

---

## 8. Control Statements Interview Questions

**Basics**

- What are control statements in Python?  
- How is `if-else` different from `if-elif-else`?  
- What are nested if statements and when are they used?  

**Working with Loops**

- What is the difference between `for` and `while` loops?  
- How do you exit a loop prematurely?  
- How do `break` and `continue` work?  

**Advanced**

- Explain the use of `pass` in Python.  
- How can nested loops be used in real-world scenarios?  
- What is loop-else in Python and how does it work?  
