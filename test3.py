# class Dog:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def bark(self):
#         return 'Woof woof!'

#     def doginfo(self):
#         print(self.name + ' is ' + str(self.age) + ' year(s)-old.') 

#     def birthday(self):
#         self.age += 1
   
#     def set_buddy(self, buddy):
#         self.buddy = buddy
#         buddy.buddy = self


# chester = Dog('Chester', 8)
# pekas = Dog('Pecas', 7)

# # chester.age = 9

# # print(chester.bark())
# # chester.doginfo()
# # chester.birthday()

# # print(chester.age)

# chester.set_buddy(pekas)

# print(chester.buddy.name)
# print(chester.buddy.age)
# chester.buddy.doginfo()



class Person:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        # self.email = self.first + '.' + self.last + '@email.com'
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # The method (inside) can have a different name, but the setter should
    # have the name from the method which will modify.
    @fullname.setter
    def anothername(self, name):
        self.first, self.last = name.split()
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    
    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)
    
p1 = Person('Juan', 'Perez', 35)
print(p1.email)
p1.anothername = 'Benito Bodoque'
print(p1.fullname)
print(p1.first)
print(p1.email)
print(p1)
# text = 'utu pusu rukutu pusu'
# t1, t2, t3, t4 = text.split()

# # print(t1 + t4)

# print(text.split())

# grocery = 'Milk, Chicken, Bread'
# print(grocery.split(', '))
# print(grocery.split(':'))