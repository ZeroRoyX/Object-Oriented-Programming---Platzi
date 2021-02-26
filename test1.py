# class Persona:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def saluda(self, another_p):
#         print('Hola ' + another_p.name + ' me llamo ' + self.name + '.')

# rodrigo = Persona('Rodrigo', 34)
# aracely = Persona('Aracely', 35)

# rodrigo.saluda(aracely)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greetings(self, a_person):
#         print(f'Hola {a_person.name}! mucho gusto, me llamo {self.name}.')

# rodrigo = Person("Rodrigo", 34)
# aracely = Person("Portacely", 36)

# rodrigo.greetings(aracely)


class Dog:
    def __init__(self, name, breed, age, height):
        self.name = name
        self.breed = breed
        self.age = age
        self.height = height
    
    def dog_name(self):
        print("My dog's name is " + self.name + " and he is a " + self.breed + ". He is " + str(self.age) + " years-old and he is " + self.height + ' size.')
        
Chester = Dog("Chester", "Beagle", 8, "medium")
# Blacky = Dog("Blacky", "Rottweiler", 5, "tall")
# Chester.dog_name()
# Blacky.dog_name()

print(Chester.dog_name())