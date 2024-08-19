# 2) Crear un programa que contenga las funciones

# a) leerDatos(nombre) que lee los datos contenidos en un archivo
# b) convertirDatos(entrada) que transforma los datos leidos del archivo en una lista de enteros
# c) convertirDatosLambda(entrada) que transforma los datos leidos del archivo en una lista de enteros mediante listas por compresion
# d) noRepetidos(datos) que devuelve una lista de los elementos no repetidos (no usar for-in)

def leerDatos(nombre):
    
    arch= open(nombre, "r")
    print(arch.read())
    arch.close()

def convertirDatos(entrada):
    
    arch= open(entrada, "r")
    texto= arch.read() #guardo el String en una variable
    lista= texto.split() #separo y guardo en una lista cada palabra del String
    for i in range(len(lista)):
        lista[i]=int(lista[i])  #paso a entero cada elemento
        
    arch.close()
    return lista

def noRepetidos(datos):
    
    arch= open(datos, "r")
    texto= arch.read() #guardo el String en una variable
    lista= texto.split() #separo y guardo en una lista cada palabra del String
    c=set(lista) #creo un conjunto con la lista de Strings (no permite elementos repetidos asi que los filtra)
    lista=list(c) #vuelco a convertir a lista el conjunto de la linea anterior, como lo pide el ejercicio (devolver una lista)
    arch.close()
    return lista

# a)    
leerDatos("ejercicio2.txt")

# b)
lista=convertirDatos("ejercicio2.txt") #FUNCIONA SOLO SI EL CONTENIDO DE ejercicio2.txt son numeros
print(lista)

# c)


# d) 

lista=noRepetidos("ejercicio2.txt")
print(lista)