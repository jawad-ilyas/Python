class Character : 
    def __init__(self , name , health , attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attackEnemy(self):
        print(f'{self.name} is attack with power {self.attack}')


warrior = Character('Thor' , 100 , 50)
mega = Character('Gandlalf' , 80 , 70)
archer = Character('Archer' , 80 , 90)

# warrior.attackEnemy()
# mega.attackEnemy()
# archer.attackEnemy()



"""    class is the blue print of the objects"""

# class Car :

#     def __init__(self , brand , color):
#         self.brand = brand
#         self.color = color

    
#     def set_details(self , brand , color):
#         self.brand = brand
#         self.color = color

#     def get_details(self):
#         print(f'{self.brand} and color is this {self.color}')


# car1 = Car("bmw" , "blue")

# # car1.set_details("tesla" , "red")
# # car1.get_details();

# print(car1.brand , car1.color)

"""
1- default constructor
2- parameterize constructor
3- default value constructor


"""


class Student : 
    def __init__(self, name , age , grade):
        self.name = name
        self.age = age
        self.grade = grade


student1 = Student("jawad" , 12 , "A")
student2 = Student("ahmad" , 12 , "c")

print(student1.name , student1.age ,student1.grade)
print(student2.name , student2.age ,student2.grade)




"""
polymorphism 

one name , many forms 

"""


class Bird:
    def sound(self):
        print ('Birds make sound')

class Crow(Bird):
    