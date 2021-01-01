


def ingresoDatos(cantidadNumeros):
    numeros=[]
    suma=0
    for i in range(0,cantidadNumeros):
        numero=int(input("ingresa el numero"+str(i)+":"))
        numeros.append(numero)
        suma=suma+numero

    promedio=suma/cantidadNumeros
    print("el promedio es",promedio)

    for i in range(0,cantidadNumeros):
        if numeros[i]>11:
            print("numero aprobado",numeros[i])
        else:
            print("numoer no aprobado",numeros[i])


    mayor=0
    for i in range(0,cantidadNumeros):
        if numeros[i]>mayor:
            mayor=numeros[i]

    menor=99999
    for i in range(0,cantidadNumeros):
        if numeros[i]<menor:
            menor=numeros[i]



    print("el numero mayor es:",mayor)
    print("el numero menor es:",menor)
    print("la posicion del numero mayor es: ", numeros.index(mayor))


cantidadNumeros=int(input("ingresa cantidad de numeros: "))
ingresoDatos(cantidadNumeros)


