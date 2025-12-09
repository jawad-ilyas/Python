def greet() :
    """
    Docstring for greet
    """ 
    print("hi jawad mughal")

# greet()


# parameter and arguments 

def greet(name) : # parameter
    print("my name is this " + name)

# greet("jawad") # argument 


"""
argument typs

positional arguments
keyword
default
"""

# postional argument
# names may be different into argument and paramter but , should be place as there postions



# keyword arguement means
# when you pass argument you should place like parameter variablename=""
# soo now position not matter


# def greet(name , city) : 
#     print(f'welcome {name} to city {city}')

# greet(name="jawad" , city="lahore")
# greet( city="lahore",name="ilyas" ,)


# default arguemnt , set value at the parameter position 
# def greet(name="unkown" , city="unkown city") : 
#     print(f'welcome {name} to city {city}')

# greet(name="jawad"   , city="lahore ")
# greet( city="lahore",name="ilyas" ,)


# return statement 
# to exit the function 
# also want to return the result 

def fullNameFun (firstname , lastName):
    fullName = f'{firstname} {lastName}'
    return fullName

# print(fullNameFun("jawad" , "ilyas"))


# local variables

def msg():
    # local variables 
    choice = "i love coading"
    # print(choice)

# msg()

""" throw error because choice isnot present into global scope """
# print(choice)


# global variables



def msg(choice):
    # local variables 
    # choice = "i love coading"
    print(choice)


"""present into global scope"""
choice = "12121212"
# msg(choice)




# decorator
# means defined fuction inside the main function 
# without the changing the main function code


def my_decorator(func):
    def wrapper():
        print("something is happening before the funcion is called")
        func()
        print("something is happening after the funcion is called")
    return wrapper


@my_decorator
def say_hello():
    print("hello the wrapper")


# say_hello()


# genertors 
# yield keyword 
def count_down(nums):
    while nums > 0:
        yield num
        num -= 1

for number in count_down(5):
    print(number)
