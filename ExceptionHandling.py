"""
Docstring for ExceptionHandling


a- compile time error 
b  - run time error 
c - logical error


try -except

nested try-except block
"""


# try:
#     print(1%0)
# except ZeroDivisionError :
#     print("error handling ")
# except ValueError : 
#     print ("string handing")
# finally:
#     print("task complete || alway runs ")


# nested try -except block

# try : 
#     num1 = int(input("enter numer 1"))
#     num2 = int(input("enter numer 2"))
#     try : 
#         result = num1 /num2
#     except ZeroDivisionError : 
#         print("zero error handling")
# except ValueError: 
#     print("you must provide a valid input")


def check_Password(password):
    if len(password) < 8:
        raise Exception("Error Password must be >=8 ")
    print("password is strong")

try:
    password = input("enter a password")
    check_Password(password)
except Exception as e :
    print(e)