print("Hola señor vas a ingresar dos numero:")
n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
suma = n1 + n2 
print("La suma de los dos es: ",suma)

if n1==n2:
    print("Hola señor los 2 numeros son iguales")
elif n1>n2:
    print(f"Hola señor el numero {n1} es mayor que {n2}")
else:
    print(f"Hola señor el numero {n2} es mayor que {n1}")