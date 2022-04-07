#Muestra el mayor de los 3 numeros

mayor = 0
maximo = 3 
 
for i in range(maximo):
    numero = int(input('ingrese un numero:'))
    if numero > mayor:
        mayor = numero
 
print(mayor)