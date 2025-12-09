# ✅ Python Strings – Complete Practice & Interview Guide

This guide contains Python practice examples for **Strings**, including creation, accessing characters, slicing, built-in methods, and formatting.

---

## 1. Creating Strings

```python
# Using single or double quotes
str1 = 'Hello'
str2 = "World"

# Multi-line string using triple quotes
str3 = """This is
a multi-line
string"""

print(str1)
print(str2)
print(str3)
```
```python
Hello
World
This is
a multi-line
string
```

---

## 2. String Indexing

```python
text = "Python"

print(text[0])   # First character
print(text[-1])  # Last character
print(text[1:4]) # Slice from index 1 to 3
```
```python
P
n
yth
```

---

## 3. String Slicing

```python
text = "PythonProgramming"

print(text[0:6])   # Python
print(text[6:])    # Programming
print(text[:6])    # Python
print(text[-6:])   # mming
print(text[::2])   # Every 2nd character
print(text[::-1])  # Reverse string
```
```python
Python
Programming
Python
mming
Pto rgamn
gnimmargorP
```

---

## 4. String Methods

### 4.1 Case Methods
```python
s = "python"
print(s.upper())  # PYTHON
print(s.capitalize())  # Python
print(s.title())  # Python
```
```python
PYTHON
Python
Python
```

### 4.2 Strip Methods
```python
s = "   hello world   "
print(s.strip())   # Remove spaces
print(s.lstrip())  # Remove left spaces
print(s.rstrip())  # Remove right spaces
```
```python
hello world
hello world   
   hello world
```

### 4.3 Split & Join
```python
s = "Python is fun"
words = s.split()  # Split into list
print(words)

joined = "-".join(words)  # Join list into string
print(joined)
```
```python
['Python', 'is', 'fun']
Python-is-fun
```

### 4.4 Find & Replace
```python
s = "Python Programming"
print(s.find("Pro"))    # index of "Pro"
print(s.replace("Python", "Java"))
```
```python
7
Java Programming
```

### 4.5 Other Useful Methods
```python
s = "hello world"
print(s.count("l"))   # Count occurrences
print(s.startswith("he"))
print(s.endswith("ld"))
print(s.isalpha())    # False because of space
```
```python
3
True
True
False
```

---

## 5. String Concatenation & Repetition

```python
a = "Hello"
b = "World"

print(a + " " + b)  # Concatenation
print(a * 3)        # Repetition
```
```python
Hello World
HelloHelloHello
```

---

## 6. String Formatting

### 6.1 Using f-strings (Python 3.6+)
```python
name = "Jawad"
age = 25
print(f"My name is {name} and I am {age} years old")
```
```python
My name is Jawad and I am 25 years old
```

### 6.2 Using format()
```python
print("My name is {} and I am {} years old".format(name, age))
print("My name is {n} and I am {a} years old".format(n=name, a=age))
```
```python
My name is Jawad and I am 25 years old
My name is Jawad and I am 25 years old
```

### 6.3 Using % Operator
```python
print("My name is %s and I am %d years old" % (name, age))
```
```python
My name is Jawad and I am 25 years old
```

---

## 7. Escape Sequences

| Sequence | Description         |
|----------|-------------------|
| `\n`     | New line           |
| `\t`     | Tab                |
| `\\`     | Backslash          |
| `\'`     | Single quote       |
| `\"`     | Double quote       |

```python
print("Hello\nWorld")
print("Python\tProgramming")
```
```python
Hello
World
Python  Programming
```

---

## 8. String Interview Questions

**Basics**

- How do you create a string in Python?  
- How is string indexing and slicing done?  
- What are mutable and immutable data types?  

**Working with Strings**

- How do you convert a string to upper/lower case?  
- How do split() and join() work?  
- How do you find, replace, and count characters in a string?  
- Explain string concatenation and repetition.  

**Advanced**

- How does f-string formatting work?  
- What are escape sequences?  
- How can strings be reversed in Python?  
