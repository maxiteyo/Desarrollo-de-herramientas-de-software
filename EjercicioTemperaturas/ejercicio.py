#HAY 43259 TEMPERATURAS

nomb= dict() #diccionario con los nombres como clave



arch= open("testTemperaturas.txt", "r", encoding="iso-8859-1")#Si no le agrego ese encoding no lo sabe leer
lista=arch.readlines()
l=list()  #lista que tiene cada dato de cada linea
listaNombres= list() #hago una lista aparte que contenga cada nombre de cada linea para poder mapear el diccionario

for i in range(len(lista)-3): #le resto 3 para no guardar en la lista los datos irrelevantes
    l.append(lista[i+3].split())
    

print(l)

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
    nomb[nombre.lstrip()] = None  #la funcion lstrip elimina todos los espacios en blanco al inicio del string (PROBLEMA SOLLUCIONADO)
    nombre=""
#CREO EL DICCIONARIO DE TMAX Y TMIN y lo asocio al diccionario de los nombres

cont=-1
for j in range(len(lista)-3):
    
    cont+=1
    t= dict() #diccionario con las temperaturas maximas y minimas como clave. Se crea aca ya que los diccionarios se pasan por referencia. Si creo uno mismo para todos cuando modifico un valor cambia para todos
    posiciones = [i for i, char in enumerate(lista[j+3]) if char == ' ']
    print(f'Posiciones de los espacios en blanco: {posiciones}')
    if(posiciones[2] == 10):
        t["tmax"]=None
        
    else:
        if(posiciones[2] != 10):
            aux=lista[j+3].split()
            t["tmax"]=aux[1] 
            
            
    if(posiciones[5] == 17 | posiciones[9] == 17):
        t["tmin"]=None
    
    else: 
        if(posiciones[9] != 17 & posiciones[2]==10):
            aux=lista[j+3].split()
            t["tmin"]=aux[1]
            
    nomb[listaNombres[cont]]=t
    


#DICCIONARIO "PRINCIPAL" QUE VA A TENER LAS 365 TEMPERATURAS DE CADA LOCALIDAD



print("\n")
print(nomb)
print(listaNombres)

arch.close()