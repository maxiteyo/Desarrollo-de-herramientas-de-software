cadena= input("Ingrese una cadena con letras y numeros: ")

numeros= []
for i in cadena:
    if i.islower()==False & i.isupper()==False:
        numeros.append(i)

suma=0
for i in range(len(numeros)):
    suma+=int(numeros[i])
    
print("La suma de los numeros de la cadena es: ", suma)
    
        
