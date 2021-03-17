import random

# # def binary_search(item_list, item):
# #     first = 0
# #     last = len(item_list) - 1
# #     found = False

# #     while(first <= last and not found):
# #         print(f'El limite inferior es {first} y el exterior es {last}')
# #         mid = (first + last) // 2
# #         print(f'El mid es {mid}.')
# #         if item_list[mid] == item:
# #             print(item_list[mid])
# #             found = True
# #         else:
# #             if item < item_list[mid]:
# #                 last = mid - 1
# #             else:
# #                 first = mid + 1

# #     return found 

# # lista = sorted([random.randint(0, 100) for i in range(10)])
# # print(lista)

# # print(binary_search(lista, 3))
# # print(binary_search(lista, 10))


# # PLATZI'S EXERCISE:

# # def busqueda_binaria(list, objective, low, high, counter):
# #     # low = 0
# #     # high = len(lista) - 1
# #     counter += 1
# #     print(f'buscando {objective} entre {list[low]} y {list[high]} en {counter} intentos.')
# #     print(f'Los indices son {low} y {high}.')

# #     if low > high:
# #         return False

# #     mid = (low + high) // 2

# #     if lista[mid] == objective:
# #         return True

# #     elif lista[mid] < objective:
# #         return busqueda_binaria(lista, objective, mid + 1, high, counter)
        
# #     else:
# #         return busqueda_binaria(lista, objective, low, mid - 1, counter)
        


# # if __name__ == "__main__":
# #     list_size = int(input('De qué tamaño es la lista?: '))
# #     objective = int(input('Qué número quieres encontrar?: '))

# #     lista = sorted([random.randint(0, 100) for i in range(list_size)])

# #     found = busqueda_binaria(lista, objective, 0, len(lista) - 1, 0)

# #     print(lista)
# #     print(found)
# #     print(f'El elemento {objective} {"está" if found else "no está"} en la lista.')

# # VARIANTE
# counter = 0

# def busqueda_binaria(list, objective, low, high):
#     # low = 0
#     # high = len(lista) - 1
#     global counter
#     counter += 1 
#     print(f'buscando {objective} entre {list[low]} y {list[high]} en {counter} intentos.')
#     print(f'Los indices son {low} y {high}.')

#     if low > high:
#         return False

#     mid = (low + high) // 2
    

#     if lista[mid] == objective:
#         return True

#     elif lista[mid] < objective:
#         return busqueda_binaria(lista, objective, mid + 1, high)
        
#     else:
#         return busqueda_binaria(lista, objective, low, mid - 1)
        


# if __name__ == "__main__":
#     list_size = int(input('De qué tamaño es la lista?: '))
#     objective = int(input('Qué número quieres encontrar?: '))

#     lista = sorted([random.randint(0, 100) for i in range(list_size)])

#     found = busqueda_binaria(lista, objective, 0, len(lista) - 1)

#     print(lista)
#     print(found)
#     print(f'El elemento {objective} {"está" if found else "no está"} en la lista.')


# PRACTICE

def binary_search(lista, objective):
    low = 0
    high = len(lista) - 1
    found = False
    counter = 0

    while low <= high and not found:
        counter += 1
        print(f'Searching for {objective} between {lista[low]} and {lista[high]}.')
        print(f'Index between {low} and {high}.')
        print(f'Number of searching tries: {counter}.')

        mid = (low + high) // 2
        print(mid)
        
        if lista[mid] == objective:
            found = True
        
        else:
            if lista[mid] < objective:
                low = mid + 1

            else:
                high = mid - 1

    return found

if __name__ == "__main__":
    list_size = int(input('De qué tamaño es la lista?: '))
    objective = int(input('Qué número quieres encontrar?: '))

    lista = sorted([random.randint(0, 100) for i in range(list_size)])

    encontrado = binary_search(lista, objective)

    print(lista)
    print(encontrado)
    print(f'El elemento {objective} {"está" if encontrado else "no está"} en la lista.')