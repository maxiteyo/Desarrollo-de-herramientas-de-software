nombre=input("Ingrese el nombre de un archivo: ")

l= nombre.split(".")

print("El nombre de la cadena separado de su extension es: ", end=" ")
for i in range(len(l)-1):
    print(l[i])


print("El nombre de la extension es: ",l[len(l)-1])