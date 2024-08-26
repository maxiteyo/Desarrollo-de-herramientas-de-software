palabra= input("Ingrese una palabra: ")

palabraAuxiliar= palabra[::-1]

if palabra == palabraAuxiliar:
    print("Su cadena ingresada (",palabra,") es un palindromo")
    
else:
    print("Su cadena ingresada (",palabra,") NO es un palindromo")