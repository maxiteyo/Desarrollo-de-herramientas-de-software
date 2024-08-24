xmayor=0
ymayor=0

puntos=[[0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0]]


print("Ingrese el punto inicial (x,y): ", end=" ")
puntos[0][0]= input()
puntos[0][1]= input()
sumaInicial=int(puntos[0][0]) + int(puntos[0][1])


for i in range(4):
    print("Ingrese el punto (x,y) numero ",i+1," :", end=" ")
    puntos[i+1][0]=input()
    puntos[i+1][1]=input()

for i in range(4):
    suma=int(puntos[i+1][0]) + int(puntos[i+1][1])
    if(i == 0):
        xmayor=int(puntos[i+1][0])
        ymayor=int(puntos[i+1][1])
        sumaMayor=int(puntos[i+1][0]) + int(puntos[i+1][1])
        
    if(((abs(sumaInicial-suma)) < (abs(sumaInicial-sumaMayor))) | ((abs(suma-sumaInicial)) <  (abs(sumaInicial-sumaMayor)))):
        xmayor=int(puntos[i+1][0])
        ymayor=int(puntos[i+1][1])
        sumaMayor=int(puntos[i+1][0]) + int(puntos[i+1][1])
    
    

    
print(puntos)

print("El punto mas cercano es en (",str(xmayor),",",str(ymayor),")")



    
    





