import random

def insertion_sort(list):
    for i in range(1, len(lista)):
        current_value = lista[i]
        # i = i
        
        while i > 0 and lista[i - 1] > current_value:
            print(current_value, i)
            print(lista)
            lista[i] = lista[i - 1]
            i -= 1

        print(current_value, i)
        print(lista)
        lista[i] = current_value
        print(current_value, i)
        print(lista)
        
    return lista

if __name__ == '__main__':
    list_size = int(input('Elige el tamaño de la lista: '))

    lista = [random.randint(0, 100) for i in range(list_size)]

    lista_ordenada = insertion_sort(lista)

    print(lista_ordenada)