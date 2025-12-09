# list properties
# ----------------------
# 1- orderd
# 2 - mutable 
# 3- dynamic 
# 4- heterogeneous


# way to creating list
# 1 
my_list = [1, 2,3 , "jawad" , True]
# print( "list 1" , my_list)



# 2 - using list contructor
# double parantesis
mylist2 = list((1 ,2 ,35, 20 , "jawad" , False))
# print("list 2" ,mylist2)


# 3 -4 way to create list comprehension & range()
# print(mylist2[0])

# change the value into list
changeList = [1  , 2,3 ,4 ,5 ]
# print( "before " , changeList)

changeList[0] = "list is change using index"
# print( "after", changeList)

# other way to change list using slice 

changeList[0:2] = 10,20
# print("other way to change the list using slice " , changeList)


# concation the list 
list1 = [1,2,3,4,5]
list2 = [6,7,8,9 , 11]

result = list1 + list2
# print("result of concat the list" , result)


# how to repeat the list using  list * number
listForRepeat = ["list is repeating"]
# print("way to repeat the list  , but does not change the main list" ,listForRepeat * 3)




#  who to use the in and not in the list

listForIn = [1 ,2 ,3,4,5]
# check = int(input("enter a number to check = "))
# if check  in listForIn:
#     print("found")
# else: 
#     print("not found ")


# example of the not found 

# check = int(input("enter a number you want to check "))
# if check not in listForIn:
#     print("number is not found")
# else : 
#     print("number is found")


# list basically follow the shadow copy 
# listCopy = list1
# print("list copy 1 " , list1)
# print("list copy 2 " , listCopy)

# listCopy[0] = "change the value into copy list"
# print("list copy 1 after changing" , list1)
# print("list copy 2 after changing" , listCopy)



#using the copy variable for deep copy

# list1Clone = list1.copy();
# print("list copy 1 " , list1)
# print("list copy 2 " , list1Clone)

# list1Clone[0] = "change the value into copy list - values not change because we use the copy method , build in python"
# print("list copy 1 after changing" , list1)
# print("list copy 2 after changing" , list1Clone)



# methods into list 

# append method 
list1.append("this variable is append using the append method ")
# print("list1 print after append" , list1)


# extend method 

a= [1,2,3,4]
b = [3,4 ,2,1]
# a.extend(b)
# print(b)
# print(a)


# insert method
# if we wnat to insert at specfic position 
# b.insert( 1, " this values is insert by insert method")
# print(b)

# remove method 
# this is remove by data not index
# b.remove(4)
# print(b)


# pop method 
# in this method we need to pass the index
# b.pop(0)
# print("using the pop method also return the poped element " , b)


# clear method 
# used for the clear the list 
a = [1,2,43,5,6]
# a.clear()
# print(a)


# index method
# help me to find the index when we passing the data
# print("return the index of the given data" ,a.index(43))


# count method
# return the occurence of the any variable 
j = [ 1, 2, 3, 4, 1,1 ,24, 5 ,]
# print(a.count(224))


# sort 
# use for the sorting
# a.sort();
# print(a)


# reverse 
# a.reverse();
# print(a)

# min and max 
# print(min(j))
# print(max(j))


#common element 
# set function 
s1 = set(a)
s2 = set(b)

# s3 = s1.intersection(s2)
# print(list((s3)))



# range function 
# step , stop , increment 
number = list(range(0 , 100 , 5))
# print(number)


# list comprision 
"""
[express for item in interable  , if condition ]
expresion = x * 2 , 
item = 
iterable = 
condtion ?
"""

square = [i ** 2 for  i in   range(1 , 11 , 2) if i%2 != 0]
print(square)