"""
python Dictionary

1- Definition & characteristics
    key-value paris
    unordered (before python 3.7)
    mutable
2- creation 
     using {} braces
     using dict() constructor 
3- operatioins
     adding items
     updateing items
     deleting items
4- dictionary methods 
    get() , keys() , values () , items () , pop() , popitems() , clear() 
5- comprehensions
    Dictioinary Comprehension 
6- Nested Dictionaries
7- common use cases

"""


# creating first dictionary 

# my_dic = {

#     "name" : "jawad" , 
#     "age" : 20,
#     "gender" : "male"

# }

# print(my_dic)


# add into dictionary 

# my_dict = {
#     'Fruites' : ['bannan' , 'Apple' , 'Orange'] , 
#     'category' : 'Fruit',
# }
# print(my_dict)

# my_dict['price'] = 5000
# print(my_dict)


# update the dictionary 
# my_dict = {
#     'name' : 'python' , 
#     'version' : 3.5
# }
# print(my_dict)

# my_dict['version'] = 4.0

# print(my_dict['version'])


# delete into items 

# my_dict = { 'name' : 'python' , 'version' : 3.7 , 'use_cases' : ['ai' , 'ml' , 'dsa']}
# print(my_dict)

# del my_dict['version']

# print(my_dict)


# methods into dictionary

profile = {
    'name' : 'jawad' , 
        'age' : 300 , 
        'salary' : 25000
}

# get method  --- used for the retrive the value of the key
# we can also pass the second argument into get method , use defined error if key not found 
# print(profile.get('name' , 'name key is not present int dictionary '))



# keys are used for the get total keys presnet into dictionary 

# print(profile.keys())


# value () method used for the get values

# print(profile.values())


# items () , pop() , popitems() , clear() 



# items() -- return the keys and values
# print(profile.items())

# pop() - remove the element , from dictionary  atlest passing the keys name 

# print(profile.pop('name'))



# popItem()
# remove the laste items from the dictionary 

# print(profile.popitem())


# clear() --- means remove the all dictionary

# print(profile.clear())


for k in profile.keys():
    print(k)
for k in profile.values():
    print(k)
for k in profile.items():
    print(k)



