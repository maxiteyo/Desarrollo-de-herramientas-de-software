nombres = []
for c in range(5):
    nombres.append(input("Ingrese un nombre: "))
    
for n in nombres :
    print ("Hola " + n + "!")
    
    #python3 inout.py < nombres.txt  ------> Desde el archivo se inyecta la informacion al programa
    
    #python3 inout.py > salida.txt ------> Inyecto la salida en un archivo
    
    # python3 inout.py < nombres.txt > salida.txt -----> hace ambos a la vez
    
    #####   maximo@maximo-P07CFL:~/DHS/Desarrollo-de-herramientas-de-software/clase02-09$ python3 inout.py > salida.txt 
    # Hacer cd DHS/Desarrollo-de-herramientas-de-software/clase02-09  para poder hacerlo
    
    # python3 inout.py < nombres.txt | grep Hola ----->la | es el pipeling, es una tuberia. Hace lo primero y posteriormente ejecuta el comando grep (Limpia y muestra las lineas que tienen Hola)
    