# Almost everything in Python is an object, with its properties and methods.
# # A Class is like an object constructor, or a "blueprint" for creating objects.

# class MyClass:
#     x = 5

# # Now we can use the class named MyClass to create objects:
# # Create an object named p1, and print the value of x:

# p1 = MyClass()
# print(p1.x)

"""
The examples above are classes and objects in their simplest form, and
are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in 
___init___(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or 
other operations that are necessary to do when the object is being 
created:
"""
# Create a class named Person, use the __init__() function to assign
# values for name and age:


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)


# Note: The __init__() function is called automatically every time the class
# is being used to create a new object.

# OBJECT METHODS

"""
Objects can also contain methods. Methods in objects are fuctions that belong
to the object.

Insert a function that prints a greeting, and execute it on the p1 object:
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello, my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


# Note: The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.