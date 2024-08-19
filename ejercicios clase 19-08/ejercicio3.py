# 3) Crear un programa que contenga las funciones

# a) leerDocumento(nombre) que lee los datos contenidos en un archivo de texto conformados por palabras
# b) palabraLongitud(texto) que devuelve un mapa de las palabras distintas y la cantidad de letras que tiene
# c) contarPalabras(texto) que devuelve el numero de palabras
# d) contarPalabrasDistintas(texto) que devuelve el numero de palabras distintas
# e) promedioLetras(palabras) que devuelve la cantidad promedio de letras entre todas las palabras
# f) Imprimir en pantalla la cantidad de palabras, cantidad de palabras no repetidas, cantidad de caracteres, cantidad promedio de caracteres por palabra

def leerDocumento(nombre):
    
    arch= open(nombre, "r")
    print(arch.read())
    arch.close()
    
def palabraLongitud(texto):
    
    d= dict()
    lista=texto.split()
    
    for i in range(len(lista)):
        d[lista[i]]=len(lista[i])
    
    return d

def contarPalabras(texto):
    
    l=texto.split()
    
    return len(l)

def contarPalabrasDistintas(texto):
    
    l=texto.split()
    s=set(l)
    return len(s)
        
def promedioLetras(palabras):
    
    l=palabras.split()
    suma=0
    for i in range(len(l)):
        suma+=len(l[i])
        
    print("\nSuma de todas las letras(Cant. caracteres)", suma)
    return suma/len(l)
    
    
# a)

leerDocumento("ejercicio3.txt")

# b) 

diccionario= palabraLongitud("hola como estas por ejemplo")
print(diccionario)

# c)

cantidad= contarPalabras("esto es una prueba")
print("\ncontarPalabras()= ", cantidad)

# d) 

cantidadDistintas= contarPalabrasDistintas("me me voy a mi casa casa")
print("\ncontarPalabrasDistintas()= ", cantidadDistintas)

# e) 

promLet= promedioLetras("sumame estas letritas")
print("promedioLetras()= ",promLet)


# f) 

texto= input("\nIngrese una oracion de palabras: ")


print("\nCantidad de palabras: ",contarPalabras(texto))
print("Cantidad de palabras no repetidas: ", contarPalabrasDistintas(texto))
print("Cantidad promedio de caracteres entre todas las palabras: ", promedioLetras(texto))