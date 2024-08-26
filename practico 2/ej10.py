cadena1= input("Ingrese la cadena 1: ")
cadena2= input("Ingrese la cadena 2: ")

l1= cadena1.split()
l2= cadena2.split()
coincidencias= []
indice=0
coinc=0
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            coinc+=1
    coincidencias.append(coinc)
    coinc=0
     

mayor=0
for i in range(len(coincidencias)):
    if i==0 :
        mayor= coincidencias[i]
    
    elif coincidencias[i] > mayor:
        mayor= coincidencias[i]
        indice=i
        
print("La palabra con mayor coincidencia es:",l1[indice], "teniendo",mayor, "coincidencias")