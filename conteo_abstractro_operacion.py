def f(x):

    respuesta = 0
    loop = 0

    for i in range(1000):
        # print(i)
        respuesta += 1

    for i in range(x):
        respuesta += x

    for i in range(x):
        for j in range(x):
            # loop = loop + 1
            # print(i, j)
            # print(loop)
            respuesta += 1
            respuesta += 1
            # print(respuesta)

    return respuesta

if __name__ == '__main__':
    
    x = 1000
    f(x)            
    print(f(x))

