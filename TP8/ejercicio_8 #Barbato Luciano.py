#ejercicio 8
#Datos usuario 
#Barbato Luciano

from operator import contains


dato = input("Ingresa apellido y nombre: ") 
nacimiento = input("ingrese su año de nacimiento: ")

def obtener_vocales(frase):
    vocales = "aeiouAEIOU"

    return [a for a in frase if a in vocales]


texto = "Barbato Luciano"

print(obtener_vocales(texto))

usuario = ("Ingrese su usuario")

if usuario == "luciano":

  contraseña = input("Ingrese su contraseña")
  if contraseña == "123456#":

   print ("Los datos son correctos")

  else:
      print ("La contraseña es incorrecta")

else: 
    print ("El usuario es correcto")           

signos = 0
contraseña = input("ingrese su contraseña: ")

while 7 > len (contraseña) <=16:
    contraseña = input("ingrese su contraseña: ")
    for caracter in contraseña:
        if caracter == "#" or caracter == "$" or caracter == "!" or caracter == "%" or caracter == "&":
         signos += 1
        
print ("Hola", dato)
