# # # # FUNCIONES COMO OBJETOS DE PRIMERA-CLASE

# # # def presentarse(nombre):
# # #     return f'Me llamo {nombre}'

# # # def estudiemos_juntos(nombre):
# # #     return f'¡Hey {nombre}, aprendamos Python!'

# # # def consume_funciones(funcion_entrante):
# # #     return funcion_entrante("Roy")

# # # if __name__ == '__main__':
    
# # #     print(consume_funciones(presentarse))
# # #     print(consume_funciones(estudiemos_juntos))

# # # # FUNCIONES ANIDADAS

# # # def funcion_mayor():
# # #     print("Esta es una función mayor y su mensaje de salida.")

# # #     def librerias():
# # #         print("Algunas librerías de Python son: Scikit-learn, Numpy y TensorFlow.")
    
# # #     def frameworks():
# # #         print("Algunos frameworks de Python son: Django, Dash y Flask.")
    
# # #     frameworks()
# # #     librerias()

# # # funcion_mayor()


# # # DECORADOR

# # def funcion_decoradora(funcion):
# #     def wrapper():
# #         print('Este es el último mensaje...')
# #         funcion()
# #         print('Este es el primer mensaje ;)')
# #     return wrapper()

# # @funcion_decoradora
# # def zumbido():
# #     print('Buzzzzzz')

# # # zumbido = funcion_decoradora(zumbido)

# # # zumbido()


# # ### GETTERS AND SETTERS

# # # Clases sin getters y setters

# # class Miles:
# #     def __init__(self, distance = 0):
# #         self.distance = distance
    
# #     def km_converter(self):
# #         return (self.distance * 1.609344)

# # plane = Miles()
# # plane.distance = 200

# # print(plane.distance)
# # print(plane.km_converter())

# # Utilizando getters y setters

# class Miles:
#     def __init__(self, distance = 0):
#         self.distance = distance

#     def km_converter(self):
#         return (self. distance * 1.609344)
    
#     # Método getter
#     # Obtendrá el valor de la distancia que
#     def get_distance(self):
#         return self._distance

#     # Método setter
#     # Se encargará de añadir una restricción.
#     def set_distance(self, value):
#         if value < 0:
# #             raise ValueError("No es posible convertir distancias menores a 0.")
# #         self._distance = value

# # car = Miles(200)
# # print(car.distance)


# # FUNCIÓN property()


# class Millas:
#     def __init__(self):
#         self._distancia = 0
    
#     # Función para obtener el valor de _distancia
#     def obtener_distancia(self):
#         print("Llamada al método getter")
#         return self._distancia

#     # Función para definir el valor de _distancia
#     def definir_distancia(self, recorrido):
#         print("LLamada al método setter")
#         self._distancia = recorrido

#     # Función para eliminar el atributo _distancia
#     def eliminar_distancia(self):
#         del self._distancia
    
#     distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)

# # Creamos un nuevo objeto
# avion = Millas()

# # Indicamos la distancia
# avion.distancia = 200

# # Obtenemos su atributo distancia
# print(avion.distancia)



class Perros(object): #Declaramos la clase principal Perros
    def __init__(self, nombre, peso): #Definimos los parámetros 
        self.__nombre = nombre #Declaramos los atributos (privados ocultos)
        self.__peso = peso
    @property
    def nombre(self): #Definimos el método para obtener el nombre
        "Documentación del método nombre bla bla" # Doc del método
        return self.__nombre #Aquí simplemente estamos retornando el atributo privado oculto
#Hasta aquí definimos los métodos para obtener los atributos ocultos o privados getter.
#Ahora vamos a utilizar setter y deleter para modificarlos
    @nombre.setter #Propiedad SETTER
    def nombre(self, nuevo):
        print ("Modificando nombre..")
        self.__nombre = nuevo
        print ("El nombre se ha modificado por")
        print (self.__nombre) #Aquí vuelvo a pedir que retorne el atributo para confirmar
    @nombre.deleter #Propiedad DELETER
    def nombre(self): 
        print("Borrando nombre..")
        del self.__nombre
        
        #Hasta aquí property#
    def peso(self):    #Definimos el método para obtener el peso
        return self.__peso #Aquí simplemente estamos retornando el atributo privado
#Instanciamos
Tomas = Perros('Tom', 27)
print (Tomas.nombre) #Imprimimos el nombre de Tomas. Se hace a través de getter
#Que en este caso como esta luego de property lo toma como el primer método..
Tomas.nombre = 'Tomasito' #Cambiamos el atributo nombre que se hace a través de setter
del Tomas.nombre #Borramos el nombre utilizando deleter