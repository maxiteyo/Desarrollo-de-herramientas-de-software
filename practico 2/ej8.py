cadena=input("Ingrese una cadena con palabras separadas: ")
n=int(input("Ingrese un numero: "))

l=cadena.split()
mayor=0
menor=0
igual=0

for i in range(len(l)):
    if len(l[i]) == n:
        igual += 1
        
    elif len(l[i]) < n:
        menor += 1
        
    elif len(l[i]) > n:
        mayor += 1
        
print("Hay ",igual,"palabra/s iguale/s")
print("Hay ",menor,"palabra/s menor/es")
print("Hay ",mayor,"palabra/s mayor/es")