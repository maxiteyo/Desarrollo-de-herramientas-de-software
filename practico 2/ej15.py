mail=input("Ingrese un mail (JhonDoe@gmail.com): ")

contrasenia= input("Ingrese una contraseña (debe tener al menos una letra mayúscula, una minúscula, un número o un símbolo): ")

mailValido=1
contValida=1

if mail.count("@")==0:
    print("A su mail ingresado le falta el '@'")
    mailValido=0
    
    
if mail.count(".")==0:
    print("A su mail no tiene ningun punto")
    mailValido=0

hayMayus=False
hayMin=False
hayNum=False
haySimb=False

for i in contrasenia:
    if i.isupper()==True:
        hayMin=True
        
    if i.islower()==True:
        hayMayus=True
        
    if i.isdigit()==True:
        hayNum=True
        
    if i.isalpha()==False & i.isdigit()==False & i.isspace()==False :
        haySimb=True


if hayMayus==False:
    print("A su contraseña le hace falta una mayuscula")
    contValida=0
    
if hayMin==False:
    print("A su contraseña le hace falta al menos una minuscula")
    contValida=0
    
if hayNum==False | haySimb==False:
    print("A su contraseña le hace falta al menos un numero o un simbolo")
    contValida=0

if mailValido==1:
    print("El mail ingresado es valido")
    
if contValida==1:
    print("La contraseña ingresada es valida")