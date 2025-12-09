# ✅ Python Operators – Complete Practice & Interview Guide

This guide contains Python practice examples for **Operators**, including arithmetic, comparison, logical, assignment, bitwise, membership, and identity operators.

---

## 1. Arithmetic Operators

| Operator | Description         | Example       |
|----------|-------------------|---------------|
| `+`      | Addition           | `x + y`       |
| `-`      | Subtraction        | `x - y`       |
| `*`      | Multiplication     | `x * y`       |
| `/`      | Division           | `x / y`       |
| `//`     | Floor Division     | `x // y`      |
| `%`      | Modulus (Remainder)| `x % y`       |
| `**`     | Exponentiation     | `x ** y`      |

```python
x = 10
y = 3

print(x + y)   # 13
print(x - y)   # 7
print(x * y)   # 30
print(x / y)   # 3.3333...
print(x // y)  # 3
print(x % y)   # 1
print(x ** y)  # 1000
```
```python
13
7
30
3.3333333333333335
3
1
1000
```

---

## 2. Comparison Operators

| Operator | Description       | Example      |
|----------|-----------------|--------------|
| `==`     | Equal            | `x == y`     |
| `!=`     | Not equal        | `x != y`     |
| `>`      | Greater than     | `x > y`      |
| `<`      | Less than        | `x < y`      |
| `>=`     | Greater or equal | `x >= y`     |
| `<=`     | Less or equal    | `x <= y`     |

```python
x = 10
y = 3

print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False
```
```python
False
True
True
False
True
False
```

---

## 3. Logical Operators

| Operator | Description       | Example       |
|----------|-----------------|---------------|
| `and`    | Logical AND      | `x > 0 and y < 5` |
| `or`     | Logical OR       | `x > 0 or y > 5`  |
| `not`    | Logical NOT      | `not(x > y)`      |

```python
x = 10
y = 3

print(x > 0 and y < 5)   # True
print(x > 0 or y > 5)    # True
print(not(x > y))         # False
```
```python
True
True
False
```

---

## 4. Assignment Operators

| Operator | Description         | Example       |
|----------|-------------------|---------------|
| `=`      | Assign             | `x = 5`       |
| `+=`     | Add and assign     | `x += 3`      |
| `-=`     | Subtract and assign| `x -= 2`      |
| `*=`     | Multiply and assign| `x *= 2`      |
| `/=`     | Divide and assign  | `x /= 2`      |
| `//=`    | Floor divide assign| `x //= 3`     |
| `%=`     | Modulus assign     | `x %= 4`      |
| `**=`    | Exponent assign    | `x **= 2`     |

```python
x = 5
x += 3
print(x)  # 8
x *= 2
print(x)  # 16
x %= 5
print(x)  # 1
```
```python
8
16
1
```

---

## 5. Bitwise Operators

| Operator | Description        | Example |
|----------|------------------|---------|
| `&`      | AND               | `x & y` |
| `|`      | OR                | `x | y` |
| `^`      | XOR               | `x ^ y` |
| `~`      | NOT               | `~x`    |
| `<<`     | Left shift        | `x << 1`|
| `>>`     | Right shift       | `x >> 1`|

```python
x = 10  # 1010 in binary
y = 4   # 0100 in binary

print(x & y)  # 0
print(x | y)  # 14
print(x ^ y)  # 14
print(~x)     # -11
print(x << 1) # 20
print(x >> 1) # 5
```
```python
0
14
14
-11
20
5
```

---

## 6. Membership Operators

| Operator | Description                 | Example          |
|----------|----------------------------|----------------|
| `in`     | True if value is in sequence| `5 in [1,2,5]` |
| `not in` | True if value is not in seq | `3 not in [1,2,5]` |

```python
numbers = [1, 2, 5, 7]

print(5 in numbers)       # True
print(3 not in numbers)   # True
```
```python
True
True
```

---

## 7. Identity Operators

| Operator | Description             | Example         |
|----------|------------------------|----------------|
| `is`     | True if same object     | `x is y`       |
| `is not` | True if not same object | `x is not y`   |

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)      # True
print(x is z)      # False
print(x is not z)  # True
```
```python
True
False
True
```

---

## 8. Operators Interview Questions

**Basics**

- What are operators in Python?  
- What is the difference between arithmetic, comparison, and logical operators?  
- How does Python handle operator precedence?  

**Working with Operators**

- What is the difference between `/` and `//`?  
- What are bitwise operators and how are they used?  
- How do membership and identity operators work?  

**Advanced**

- Give examples of combining logical and comparison operators.  
- How do bitwise operators differ from logical operators?  
- Explain short-circuit evaluation in `and` and `or`.
