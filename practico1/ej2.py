pesos= 1510

desglose=0

desglose=int(pesos/1000)
resto=pesos%1000

if desglose > 0:
    print("Hay ",desglose," billete/s de $1000")

desglose=int(resto/500)
resto=resto%500

if desglose > 0:
    print("\nHay ",desglose," billete/s de $500")
    
desglose=int(resto/200)
resto=resto%200

if desglose > 0:
    print("\nHay ",desglose," billete/s de $200")
    
desglose=int(resto/100)
resto=resto%100

if desglose > 0:
    print("\nHay ",desglose," billete/s de $100")
    
desglose=int(resto/10)
resto=resto%10

if desglose > 0:
    print("\nHay ",desglose," moneda/s de $10")
    
desglose=int(resto/5)
resto=resto%5

if desglose > 0:
    print("\nHay ",desglose," moneda/s de $5")
    
desglose=int(resto/2)
resto=resto%2

if desglose > 0:
    print("\nHay ",desglose," moneda/s de $2")
    
desglose=int(resto/1)
resto=resto%1

if desglose > 0:
    print("\nHay ",desglose," moneda/s de 1")



