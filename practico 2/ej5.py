cad=input("Ingrese una cadena: ")

min=0
may=0
sim=0

for i in cad:
    if i.isupper()==True:
        may += 1
    
    elif i.islower()==True:
        min += 1
        
    elif i.isalnum()==False: #si no es ni una letra ni un numero es porque es un simbolo 
        sim+= 1

print("Cantidad de minusculas: ", min)
print("Cantidad de mayusculas: ", may)
print("Cantidad de simbolos: ", sim)