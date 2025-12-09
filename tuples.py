# ===============================
# Python Tuples – Complete Practice & Interview Guide
# ===============================

# Introduction:
# Tuples are immutable, ordered, heterogeneous, and created using parentheses ()

# -------------------------------
# 1. Tuple Properties
# -------------------------------
# 1. Immutable
# 2. Ordered
# 3. Heterogeneous
# 4. Uses parentheses ()

# -------------------------------
# 2. Creating Tuples
# -------------------------------

# 2.1 Basic Tuple
numbers_tuple = (10, 20, 30)
print("Basic Tuple:", numbers_tuple)

# 2.2 Heterogeneous Tuple
mixed_tuple = (1, "Jawad", True, 3.5)
print("Heterogeneous Tuple:", mixed_tuple)

# 2.3 Tuple Packing
packed = 5, 10, 15
print("Tuple Packing:", packed)

# 2.4 Single-element Tuple
single = (10,)
print("Single-element Tuple:", single)
# Note: (10) is not a tuple, (10,) is a tuple

# -------------------------------
# 3. Accessing Tuple Elements
# -------------------------------
a = (10, 20, 30)
print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-1])

# -------------------------------
# 4. Tuple Methods & Built-in Functions
# -------------------------------

# 4.1 len()
print("Length of tuple:", len((10, 20, 30)))

# 4.2 count()
tuple_data = (1, 2, 2, 3, 2, 4)
print("Count of 2:", tuple_data.count(2))

# 4.3 index()
names = ("Ali", "Bilal", "Jawad", "Ali")
print("Index of 'Jawad':", names.index("Jawad"))

# 4.4 min() and max()
values = (5, 10, 2, 8)
print("Minimum:", min(values))
print("Maximum:", max(values))

# 4.5 sorted()
values = (4, 1, 3, 2)
sorted_list = sorted(values)
print("Sorted list from tuple:", sorted_list)

# -------------------------------
# 5. Tuple Unpacking
# -------------------------------
a, b, c = (10, 20, 30)
print("Unpacked Tuple:", a, b, c)

# -------------------------------
# 6. Nested Tuples
# -------------------------------
nested = (10, (20, 30), ("A", "B"))
print("Nested Tuple element 1:", nested[1][0])  # 20
print("Nested Tuple element 2:", nested[2][1])  # B

# -------------------------------
# 7. Tuple vs List
# -------------------------------
# Feature        Tuple           List
# Mutability     ❌ Immutable    ✅ Mutable
# Performance    Faster          Slower
# Syntax         ()              []
# Use Case       Constant data   Dynamic data

# -------------------------------
# 8. Full Tuple Practice Example
# -------------------------------
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

# -------------------------------
# 9. Tuple Interview Questions
# -------------------------------
# Basics:
# - What are tuples in Python?
# - How are tuples different from lists?
# - Are tuples mutable or immutable?
# - Can tuples store different data types?

# Working with Tuples:
# - How do you create a single-element tuple?
# - How do you access elements in a tuple?
# - What is tuple packing and unpacking?
# - How do you find the length of a tuple?

# Functions & Methods:
# - What does index() do in a tuple?
# - What is the difference between count() and index()?
# - Can we sort a tuple directly? Why / Why not?

# Scenario / Practical:
# - When would you choose a tuple instead of a list?
# - How can a tuple be used as a dictionary key?
# - Demonstrate tuple unpacking with an example.

# Advanced:
# - Can tuples contain other tuples? Give an example.
# - How does immutability affect tuple performance?
# - How do nested tuples work?
