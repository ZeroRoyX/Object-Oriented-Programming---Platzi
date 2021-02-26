
# class Coordenada:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def distancia(self, otra_coordenada):
#         x_diff = (self.x - otra_coordenada.x)**2
#         y_diff = (self.y - otra_coordenada.y)**2

#         return (x_diff + y_diff)**0.5

# if __name__ == '__main__':
#     coord_1 = Coordenada(3, 30)
#     coord_2 = Coordenada(4, 8)

#     print(coord_1.distancia(coord_2))
#     # print(isinstance(coord_2, Coordenada))

 
# # PRÁCTICA


class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, another_coord):
        dif_x = (self.x - another_coord.x)**2
        dif_y = (self.y - another_coord.y)**2

        return(dif_x + dif_y)**0.5


if __name__ == "__main__":
    # Definir las x's y y's por medio de inputs
    
    # first_xy = int(input('Define las primeras coordenadas'))
    # second_xy = int(input('Define las segundas coordenadas'))
    # third_xy = int(input('Define las segundas coordenadas'))
    # forth_xy = int(input('Define las segundas coordenadas'))
    
    coord1 = Coordenada(2, 2)
    coord2 = Coordenada(6, 6)

    print(coord1.distance(coord2))