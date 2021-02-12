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

To understand the meaning of classes we have to understand th ebulti-in 
___init___(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or 
other operations that are necessary to do when the object is being 
created:
"""
# Create a class named Person, use the __init__() function to assign
# values for name and age:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
