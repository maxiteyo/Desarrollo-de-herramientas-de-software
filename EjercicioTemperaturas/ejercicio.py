#HAY 43259 TEMPERATURAS

nomb= dict() #diccionario con los nombres como clave



arch= open("registro_temperatura365d_smn.txt", "r", encoding="iso-8859-1")#Si no le agrego ese encoding no lo sabe leer
lista=arch.readlines()
l=list()  #lista que tiene cada dato de cada linea
listaNombres= list() #hago una lista aparte que contenga cada nombre de cada linea para poder mapear el diccionario

for i in range(len(lista)-3): #le resto 3 para no guardar en la lista los datos irrelevantes
    l.append(lista[i+3].split())
    

#print(l)

nombre=""
#GENERO EL DICCIONARIO CON SOLO LOS NOMBRES UNIDOS AHORA SI
for i in l:
    
    if i[1].isalpha() == True:
        
        for j in range(len(i)-1):
                nombre= nombre +" "+ i[j+1]
        
    else:        
        if i[2].isalpha() == True:
        
            for j in range(len(i)-2):
                nombre= nombre +" "+ i[j+2]
        else:
            for j in range(len(i)-3):# Le resto tres para saltearme los datos de las temperaturas y solo tomar los nombres
                nombre= nombre +" "+ i[j+3]
    listaNombres.append(nombre.lstrip())
    t=dict()
    listmax=list()
    listmin=list() 
    t["tmax"]=listmax
    t["tmin"]=listmin
    nomb[nombre.lstrip()] = t  #la funcion lstrip elimina todos los espacios en blanco al inicio del string (PROBLEMA SOLLUCIONADO)
    nombre=""
#CREO EL DICCIONARIO DE TMAX Y TMIN y lo asocio al diccionario de los nombres


for i in range(len(lista)-3):

    nomb[lista[i+3][21:].rstrip()]["tmax"].append(lista[i+3][8:14])
    nomb[lista[i+3][21:].rstrip()]["tmin"].append(lista[i+3][15:20])

print("\n")
#print(nomb)
#print(listaNombres)


lugar=input("Ingrese lugar donde quiere ver la temperatura: ")
temp=input("Ingrese que desea buscar (tmin/tmax): ")
dia=int(input("Ingrese cuantos dias atras quiere buscar (0 hoy): "))
print("La " + temp + " de " + lugar + " es: "+ nomb[lugar][temp][dia])

arch.close()