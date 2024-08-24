from math import sqrt


print("----CALCULADORA DE RAICES DE SEGUNDO GRADO----")
a=int(input("Ingrese 'a': "))
b=int(input("Ingrese 'b': "))
c=int(input("Ingrese 'c': "))
discriminante=b*b-4*a*c

if discriminante < 0:
    print("Su polinomio no tiene raices reales")

else:
    if discriminante == 0:
         r1=(-b+sqrt(discriminante))/(2*a)
         print("La raiz de su polinomio es: ", r1)
         
    else:
        if discriminante > 0:
            r1=(-b+sqrt(discriminante))/(2*a)
            print("La raiz 1 de su polinomio es: ", r1)
            
            r2=(-b-sqrt(discriminante))/(2*a)
            print("La raiz 2 de su polinomio es: ", r2)