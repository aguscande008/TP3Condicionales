#1) 
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

#2)
nota = float(input("Ingrese su nota: "))
if nota >= 6: 
    print ("Aprobado!")
else: 
    print ("Desaprobado!")

#3)
par = int(input("Ingrese un número par: "))
if par % 2 == 0: 
    print ("Ha ingresado un número par") 
else: 
    print ("Por favor ingrese un número par")

#4)
edaad = int(input("Ingrese su edad: "))
if edaad < 12:
    print ("Niño/a")
elif edaad >= 12 and edaad < 18: 
    print("Adolescente")
elif edaad >= 18 and edaad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string. 