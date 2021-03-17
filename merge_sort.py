import random

# def merge_sort(listilla):
#     if len(listilla) > 1:
#         # print(len(lista))
#         mid = len(listilla) // 2
#         print(mid)
#         lefthalf = listilla[:mid]
#         print(lefthalf)
#         righthalf = listilla[mid:]

#         # Llamada recursiva en cada mitad
#         merge_sort(lefthalf)
#         merge_sort(righthalf)
        
#         # Iteradores para recorrer las dos sublistas
#         i = 0
#         j = 0
#         # Iterador para la lista principal
#         k = 0

#         while i < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 listilla[k] = lefthalf[i]
#                 i += 1
            
#             else:
#                 listilla[k] = righthalf[j]
#                 j += 1

#             k += 1
        
#         while i < len(lefthalf):
#             listilla[k] = lefthalf[i]
#             i += 1
#             k += 1

#         while j < len(righthalf):
#             listilla[k] = righthalf[j]
#             j += 1
#             k += 1

#     return listilla
        
# if __name__ == '__main__':
#     list_size = int(input('Define el tamaño de la lista: '))

#     lista = [random.randint(0, 100) for i in range(list_size)]

#     lista_ordenada = merge_sort(lista)
#     print(lista_ordenada)


PRACTICE

def merge_sort(my_list):
    length = len(my_list)

    if length > 1:
        mid = length // 2
        left = my_list[:mid]
        right = my_list[mid:]
        print(left, '*' * 5, right)
        

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1

        print(f'Left-half: {left}, right-half: {right}')
        print(my_list)
        print('-' * 50)

        
    return my_list
        

if __name__ == '__main__':
    list_size = int(input('¿De qué tamaño deseas la lista?: '))
    lista = [random.randint(0, 100) for i in range(list_size)]
    lista_ordenada = merge_sort(lista)
    print(lista_ordenada)






