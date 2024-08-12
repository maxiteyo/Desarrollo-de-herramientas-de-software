print("#" * 15)
for x in [3, 4, 5, 6]: #Lee lo que esta en la lista(lo que esta ente corchetes)
    print(x)
    
print("#" * 15)

for x in (3, 4.25, "Hola", True):
    print(x) #si hago print(x+5) los primeros dos elementos los va a sumar, pero al llegar al string falla
    

print("#" * 15)

for x in range(5): #corre hasta 5
    print(x)

    
print("#" * 15)

for x in range(15, 21): #del 15 al 20
    print(x)

print("#" * 15)
for x in range(-5, 1): 
    print(x)
    
print("#" * 15)
for x in range(-5, 6, 2): #Va de 2 en 2 
    print(x)
    
print("#" * 15)
for x in range(5, -6, -2): #Va de adelante para atras 
    print(x)