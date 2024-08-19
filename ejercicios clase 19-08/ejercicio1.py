# 1) Crear un programa que contenga las funciones:
# a) generarDatos(n) que devuelve una lista de n numeros enteros aleatorios entre 0 y 100
# b) guardarDatos(nombre, datos) que guarda los elementos de una lista en un archivo (uno por renglon)

import random

def generarDatos(n):
    l=[]
    for k in range(n):
        l.append(random.randint(0,100))
        
    return l

def guardarDatos(nombre, datos):
    arch=open(nombre,"w")
    for i in range(n):
        arch.write(str(datos[i]))
        arch.write("\n")    
    arch.close()
    
    
n=int(input("Ingrese un numero: "))
lista=generarDatos(n)
print(lista)
guardarDatos("ej1",lista)

