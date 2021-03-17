# class Rectangulo:
    
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura
    
#     def area(self):
#         return self.base * self.altura
    

# class Cuadrado(Rectangulo):

#     def __init__(self, arista):
#         super().__init__(arista, arista)


# if __name__ == '__main__':
#     rectangulo = Rectangulo(4, 3)
#     print(rectangulo.area())

#     cuadrado = Cuadrado(8)
#     print(cuadrado.area())

#PRACTICA

# class Rectangulo:
        
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura
    
#     def area(self):
#         return self.base * self.altura

# class Cuadrado(Rectangulo):

#     def __init__(self, arista):
#         super().__init__(arista, arista)


# if __name__ == '__main__':

#     rectangulo = Rectangulo(3, 4)
#     cuadrado = Cuadrado(5)

#     print(rectangulo.area())
#     print(cuadrado.area())

#PRACTICA

# class Rectangulo:

#     def __init__(self, base, altura):
#         self.basecita = base
#         self.alturita = altura
    
#     @property
#     def area(self):
#         return self.basecita * self.alturita

# class Cuadrado(Rectangulo):
    
#     def __init__(self, lado):
#         super().__init__(lado,lado)


# if __name__ == '__main__':

#     rectangulo = Rectangulo(3, 4)
#     cuadrado = Cuadrado(10)

#     print(rectangulo.area)
#     print(cuadrado.area) 

# TACOS PRÁCTICA

class Taco:

    precio = 15

    def __init__(self, tortilla):
        self.tortilla = tortilla
        # self.precio = precio
    
    @staticmethod
    def salsa_de_la_que_pica(simon):
        if simon == True:
            return 'Aguas compadre'
        else:
            return 'OK'

    @staticmethod
    def con_verdura(shi):
        if shi == True:
            return 'cebollita y cilantro'
        else:
            return 'OK'


class Carne_Asada(Taco):

    def __init__(self, tortilla):
        super().__init__(tortilla)


class Pastor(Taco):

    def __init__(self, tortilla):
        super().__init__(tortilla)

class De_Tripita(Taco):

    precio = 18

    def __init__(self, tortilla):
        super().__init__(tortilla)


if __name__ == '__main__':

    taco_de_asada = Carne_Asada('harina')
    taco_de_pastor = Pastor('maiz')
    taco_de_tripa = De_Tripita('maiz')

    print(taco_de_asada.salsa_de_la_que_pica(True))
    print(taco_de_pastor.con_verdura(True))
    print(taco_de_pastor.precio)
    print(taco_de_tripa.precio)






    