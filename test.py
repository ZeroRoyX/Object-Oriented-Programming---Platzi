# # Almost everything in Python is an object, with its properties and methods.
# # # A Class is like an object constructor, or a "blueprint" for creating objects.

# # class MyClass:
# #     x = 5

# # # Now we can use the class named MyClass to create objects:
# # # Create an object named p1, and print the value of x:

# # p1 = MyClass()
# # print(p1.x)

# """
# The examples above are classes and objects in their simplest form, and
# are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in 
# ___init___(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or 
# other operations that are necessary to do when the object is being 
# created:
# """
# # Create a class named Person, use the __init__() function to assign
# # values for name and age:


# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# # p1 = Person("John", 36)

# # print(p1.name)
# # print(p1.age)


# # Note: The __init__() function is called automatically every time the class
# # is being used to create a new object.

# # OBJECT METHODS

# """
# Objects can also contain methods. Methods in objects are fuctions that belong
# to the object.

# Insert a function that prints a greeting, and execute it on the p1 object:
# """


# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
    
# #     def myfunc(self):
# #         print("Hello, my name is " + self.name)
# #         print("My age is " + str(self.age))

# # p1 = Person("John", 36)
# # p1.myfunc()


# # Note: The self parameter is a reference to the current instance of the class, 
# # and is used to access variables that belong to the class.

# # THE SELF PARAMETER

# """
# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.

# It does not have to be named self, you can call it whatever you like,
# but it has to be the first parameter of any function in the class:

# Use the words mysillyobject and abc instead of self:
# """


# class Person:
#     def __init__(mysillyobject, name, age):
#         mysillyobject.name = name
#         mysillyobject.age = age

#     def myfunc(abc):
#         print("Hello, my name is " + abc.name)

# p1 = Person("Juan", 38)
# p1.myfunc()


# """
# MODIFY OBJECT PROPERTIES

# You can modify properties on objects like this:

# Set the age of p1 to 40:
# """


# p1.age = 40
# print(p1.age)


# """
# DELETE OBJECT PROPERTIES

# You can delete properties on objects by using the del keyword:

# Delete the age property from p1 object:
# """


# del p1.age
# print(p1.age)



# """
# THE PASS STATEMENT

# class definitions cannot be empty, but if you for some reason have a
# class definition with no content, put in the pass statement to avoid 
# getting an error.
# """


# class Person:
#     pass


# class Hotel:
#     def __init__(self, max_guest_number, parking_spaces):
#         self.maxgnumber = max_guest_number
#         self.parking = parking_spaces
#         self.guests = 0
        
#     def add_guest(self, guest_qty):
#         self.guests += guest_qty

#     def checkout(self, guest_qty):
#         self.guests -= guest_qty

#     def occupation(self):
#         return self.guests

# hotel = Hotel(50, 20)
# # print(hotel.maxgnumber)
# hotel.add_guest(3)
# hotel.checkout(1)
# hotel.occupation()
# print(hotel.occupation())


# Exercise: Making a Soda Inventory Program by ZeroRoyX

class Beverage_Refrigerator:
    def __init__(self, max_beverage_bottles, levels):
        self.maxbottles = max_beverage_bottles
        self.levels = levels
        self.bottles = 0

    def add_bottle(self, number_bottles):
        self.bottles += number_bottles

    def take_bottle(self, number_bottles):
        self.bottles -= number_bottles

    def available(self):
        return self.bottles

fridge_1 = Beverage_Refrigerator(60,3)
fridge_1.add_bottle(40)
fridge_1.take_bottle(28)
print(fridge_1.available()) 

