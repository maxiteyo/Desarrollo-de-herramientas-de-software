nombres = []

#python3 inout2.py < nombres.txt

#Si en el archivo de nombres dejo la primera linea en blanco, solo aparece "Linea vacia"

try:
    tmp= input("Ingrese un nombre: ") #LEE LA PRIMERA LINEA DEL ARCHIVO
    while len(tmp) > 0:
        nombres.append(tmp)
        tmp = input("Ingrese un nombre: ")
    print("Linea vacia")   
except EOFError :
        #pass no hace nada, simplemente digo que se que hubo una expecion y no hago nada
        print("Encontre EOF (Final de archivo)")
        
print("\n")
for n in nombres :
    print("Hola "+ n + "!")
