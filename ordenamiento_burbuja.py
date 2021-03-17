# import random

# def ordenamiento_de_burbuja(lista):
#     n = len(lista)
#     counter = 0

#     for i in range(n):
#         for j in range(n - i - 1):
#             print(i,j)
#             print(lista)
#             counter += 1
#             if lista[j] > lista[j + 1]:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
            
#     print(counter)
#     return lista


# if __name__ == '__main__':
#     tamano_lista = int(input("Qué tamaño de lista quieres?: "))
#     # objetivo = int(input("Qué número quieres buscar?: "))

#     lista = [random.randint(0,100) for i in range(tamano_lista)]
#     # print(lista)

#     lista_ordenada = ordenamiento_de_burbuja(lista)
#     print(lista_ordenada)


# PRACTICE
import random

def bubble_sort(list):
    n = list_size
    counter = 0

    for i in range(n - 1, 0, -1):
        for j in range(i):
            print(i, j)
            counter += 1
            print(lista)
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    print(counter)
    return lista




if __name__ == '__main__':
    list_size = int(input('¿De qué tamaño quieres la lista?: '))

    lista = [random.randint(0, 100) for i in range(list_size)]

    sorted_list = bubble_sort(lista)
    print(sorted_list)