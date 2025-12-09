# ===============================
# Python Functions – Complete Examples
# ===============================

# 1️⃣ Basic Function
def greet():
    """This function says hi"""
    print("Hi Jawad Mughal!")

greet()  # Output: Hi Jawad Mughal!


# 2️⃣ Function with Parameters and Arguments
def greet_name(name):  # 'name' is a parameter
    print("My name is " + name)

greet_name("Jawad")  # Output: My name is Jawad


# 3️⃣ Types of Arguments

# Positional Arguments
def greet_city(name, city):
    print(f"Welcome {name} to {city}")

greet_city("Jawad", "Lahore")  # Output: Welcome Jawad to Lahore

# Keyword Arguments
greet_city(city="Lahore", name="Ilyas")  # Output: Welcome Ilyas to Lahore

# Default Arguments
def greet_default(name="Unknown", city="Unknown City"):
    print(f"Welcome {name} to {city}")

greet_default()  # Output: Welcome Unknown to Unknown City
greet_default("Jawad", "Lahore")  # Output: Welcome Jawad to Lahore


# 4️⃣ Return Statement
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

name = full_name("Jawad", "Ilyas")
print(name)  # Output: Jawad Ilyas


# 5️⃣ Local vs Global Variables
choice = "I love coding"  # Global variable

def show_message():
    message = "Hello"  # Local variable
    print(message)
    print(choice)  # Can access global variable

show_message()
# print(message)  # ❌ Error: message is local


# ===============================
# 6️⃣ Decorators
# ===============================

# Simple Decorator
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before the function runs
# Hello!
# After the function runs

# Decorator with Arguments
def repeat(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@repeat
def greet_person(name):
    print(f"Hi {name}")

greet_person("Jawad")
# Output:
# Hi Jawad
# Hi Jawad


# ===============================
# 7️⃣ Generators
# ===============================

# Simple Generator
def count_down(num):
    while num > 0:
        yield num
        num -= 1

for n in count_down(5):
    print(n)
# Output:
# 5
# 4
# 3
# 2
# 1

# Generator vs List
# List uses memory for all items
numbers_list = [i for i in range(1, 10)]
print(numbers_list)

# Generator uses lazy evaluation
def big_numbers():
    for i in range(1, 10):
        yield i

for n in big_numbers():
    print(n)

# Infinite Generator
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
