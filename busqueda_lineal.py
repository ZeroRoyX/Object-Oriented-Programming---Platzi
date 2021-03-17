# # import random

# # # def busqueda_lineal(lista, objetivo):
# # #     match = False

# # #     for i in lista:
# # #         print(i)
# # #         if i == objetivo:
# # #             match = True
# # #             break

# # #     return match

    
# # # if __name__ == '__main__':
# # #     tamano_de_lista = int(input('De que tamano sera la lista?: '))
# # #     objetivo = int(input('Que numero quieres encontrar?: '))

# # #     lista = [random.randint(1, 100) for i in range(tamano_de_lista)]

# # #     print(lista)
# # #     encontrado = busqueda_lineal(lista, objetivo)
# # #     print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')

# # # EXERCISES

# # # squares = []
# # # for i in range(10):
# # #     squares.append(i * i)

# # # print(squares)

# # # # List comprehension

# # # squares = [i for i in range(10)]
# # # print(squares)


# # # fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
# # # newlist = []

# # # for x in fruits:
# # #     if "e" in x:
# # #         newlist.append(x)

# # # print(newlist)

# # # fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# # # newlist = [x for x in fruits if 'a' in x]

# # # print(newlist)



# # #  lista = [random.randint(1, 100) for i in range(tamano_de_lista)]

# # # lista = []
# # # for i in range(10):
# # #     lista.append(random.randint(1,100))
# # # print(lista)

# fruta = ['manzana', 'platano', 'cereza', 'kiwi', 'mango']

# nueva_lista = []

# for i in fruta:
#     if 'z' in i:
#         nueva_lista.append(i)

# print(nueva_lista)

# # fruta = ['manzana', 'platano', 'cereza', 'kiwi', 'mango']

# # nueva_lista = [i for i in fruta if 'z' in i]

# # print(nueva_lista)

# # EXERCISE 

# import random

# def busqueda_lineal(lista, objetivo):
#     match = False

#     for i in lista:
#         if i == objetivo:
#             match = True
#             break
    
#     return match


# if __name__ == '__main__':

#     tamano_lista = int(input('De qué tamaño será la lista?: '))
#     objetivo = int(input('Qué número estás buscando?: '))
    
#     lista = []
#     for i in range(tamano_lista):
#         lista.append(random.randint(0,100))

#     # lista = [random.randint(0,100) for i in range(tamano_lista)]

#     print(lista)

#     found = busqueda_lineal(lista, objetivo)

#     print(f'El elemento {objetivo} {"está" if found else "no está"} en la lista.')


# h_letters = []

# for letters in 'Aracely':
#     h_letters.append(random.randint(0,10))

# # print(h_letters)

# h_letters = [letters for letters in 'Aracely es bonita']
# print(h_letters)
# print(len(h_letters))

# def busqueda_lineal(lista, objetivo):
#     match = False
    
#     for i in lista:
#         print(i)
#         if i == objetivo:
#             match = True
#             break

#     return match

# if __name__ == '__main__':

#     tamano_lista = int(input('De qué tamaño quieres que sea la lista?: '))
#     objetivo = int(input('Qué número deseas buscar?: '))

#     lista = [random.randint(0, 100) for i in range(tamano_lista)]

#     search = busqueda_lineal(lista, objetivo)
#     print(lista)
#     print(f'El numero {objetivo} {"esta" if search else "no esta"} en la lista.')

# import random

# def busqueda_lineal(lista, objetivo):
#     match = False

#     for i in lista:
#         print(i)
#         if i == objetivo:
#             match = True
#             break

#     return match

# if __name__ == '__main__':
#     tamano_lista = int(input('Elige el tamano de la lista: '))
#     objetivo = int(input('Elige el numero que estas buscando: '))

#     # lista = [random.randint(0, 100) for i in range(tamano_lista)]
#     lista = []
#     for i in range(tamano_lista):
#         lista.append(random.randint(0, 100))

#     print(lista)

#     found = busqueda_lineal(lista, objetivo)
#     print(f'El {objetivo} {"esta" if found else "no esta"} en la lista.')

import random

def busqueda_lineal(lista, objetivo):
    match = False

    for i in lista:
        print(i)
        if i == objetivo:
            match = True
            break
    
    return match

if __name__ == '__main__':
    tamano_lista = int(input('Que tamano de lista quieres?: '))
    objetivo = int(input('Elige el numero que estas buscando: '))

    # lista = [random.randint(0, 100) for i in range(tamano_lista)]
    lista = []
    for i in range(tamano_lista):
        lista.append(random.randint(0,100))

    print(lista)
    # busqueda_lineal(lista, objetivo)
    found = busqueda_lineal(lista, objetivo)

    # print(f'El {objetivo} {"esta" if found else "no está"} en la lista.')





