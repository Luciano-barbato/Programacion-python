 #Ejercicio_1 Barbato Luciano 
      
from dataclasses import asdict


nombre = input("Ingrese el nombre del alumno: ")

print ("\n1 ->Lengua \n2 ->Matematica \n3 ->Fisica \n")

opcion = int(input("ingrese su opcion de materia:"))
#Lengua
if opcion == 1:
   print ("\nIngrese las notas de Lengua\n")                           
   parcial1=float(input("Ingrese parcial1: "))
   parcial2=float(input("Ingrese parcial2: "))
   parcial3=float(input("Ingrese parcial3: ")) 
   sumalengua=(parcial1 +parcial2 +parcial3)
   promediolengua= sumalengua/3

   print("Selecione Materias: \n")
   print("Presiona 2 Para Matematica ")
   print("Presiona 3 Para Fisica ")

   opcion2 = int(input("¿Cúal es tu opción deseada?:"))

   print(f"su promedio es {promediolengua}")
   if promediolengua >=8:
    print("lengua promocionada")
   elif promediolengua <8 and promediolengua >=6:
    print("lengua aprobado")
   else : 
    print("lengua desaprobado")


   materia = int(input("ingrese su opcion"))

   #Matematica
   if opcion2 == 2:
      print ("\nIngrese las notas de Matematica")                  
      parcial1=float(input("Ingrese parcial1: "))
      parcial2=float(input("Ingrese parcial2: "))
      parcial3=float(input("Ingrese parcial3: ")) 

      sumamatematica=(parcial1 +parcial2 +parcial3)
      promediomatematica= sumamatematica/3

      
    
      print("\n Solo falta ingresar una materia:")
      print("Ingrese las notas de Fisica: \n")
    
      parcial1=float(input("Ingrese parcial1: "))
      parcial2=float(input("Ingrese parcial2: "))
      parcial3=float(input("Ingrese parcial3: ")) 

      sumafisica=(parcial1 +parcial2 +parcial3)
      promediofisica= sumafisica/3

      print(f"su promedio es {promediofisica}")
      if promediofisica >=8:
       print("fisica promociona")
      elif promediofisica <8 and promediofisica >=6:
       print("fisica aprobado")
      else :
       print("fisica desaprobado")
   
     #Fisica
   elif opcion2 == 3:

      print ("\nIngrese las notas de Fisica")                 
      parcial1=float(input("Ingrese parcial1: "))
      parcial2=float(input("Ingrese parcial2: "))
      parcial3=float(input("Ingrese parcial3: ")) 

      sumafisica=(parcial1 +parcial2 +parcial3)
      promediofisica= sumafisica/3

      print(f"su promedio es {promediofisica}")
      if promediofisica >=8:
       print("fisica promociona")
      elif promediofisica <8 and promediofisica >=6:
       print("fisica aprobado")
      else :
       print("fisica desaprobado")

      print("\nSolo falta ingresar una materia:")
      print("Ingrese las notas de Matemática: \n")
                      
      parcial1=float(input("Ingrese parcial1: "))
      parcial2=float(input("Ingrese parcial2: "))
      parcial3=float(input("Ingrese parcial3: ")) 

      sumamatematica=(parcial1 +parcial2 +parcial3)
      promediomatematica= sumamatematica/3

      print(f"su promedio es {promediomatematica}")
      if promediomatematica >=8:
       print("matematica promociona")
      elif promediomatematica <8 and promediomatematica >=6:
       print("matematica aprobado")
      else :
       print("matematica desaprobado")

   else:
        print("OPCIÓN INCORRECTA!")

elif opcion == 2:
    print ("\nIngrese las notas de Matematica")                  
    parcial1=float(input("Ingrese parcial1: "))
    parcial2=float(input("Ingrese parcial2: "))
    parcial3=float(input("Ingrese parcial3: ")) 

    sumamatematica=(parcial1 +parcial2 +parcial3)
    promediomatematica= sumamatematica/3

    print(f"su promedio es {promediomatematica}")
    if promediomatematica >=8:
     print("matematica promociona")
    elif promediomatematica <8 and promediomatematica >=6:
       print("matematica aprobado")
    else :
       print("matematica desaprobado")

    print("Selecione Materias: \n")
    print("Presiona 1 Para Lengua")
    print("Presiona 3 Para Fisica\n")
    opcion3 = int(input("¿Cúal es tu opción deseada?:"))

    if opcion3 == 1:
       print ("\nIngrese las notas de Lengua\n")                           
       parcial1=float(input("Ingrese parcial1: "))
       parcial2=float(input("Ingrese parcial2: "))
       parcial3=float(input("Ingrese parcial3: ")) 
       sumalengua=(parcial1 +parcial2 +parcial3)
       promediolengua= sumalengua/3

       print(f"su promedio es {promediolengua}")
       if promediolengua >=8:
        print("lengua promocionada")
       elif promediolengua <8 and promediolengua >=6:
        print("lengua aprobado")
       else : 
        print("lengua desaprobado")

       print("\nSolo falta ingresar una materia:")
       print ("\nIngrese las notas de Fisica")

       parcial1=float(input("Ingrese parcial1: "))
       parcial2=float(input("Ingrese parcial2: "))
       parcial3=float(input("Ingrese parcial3: ")) 

       sumafisica=(parcial1 +parcial2 +parcial3)
       promediofisica= sumafisica/3

       print(f"su promedio es {promediofisica}")
       if promediofisica >=8:
        print("fisica promociona")
       elif promediofisica <8 and promediofisica >=6:
        print("fisica aprobado")
       else :
        print("fisica desaprobado")
    
    elif opcion3 == 3:
        
       print ("\nIngrese las notas de Fisica")                 
       parcial1=float(input("Ingrese parcial1: "))
       parcial2=float(input("Ingrese parcial2: "))
       parcial3=float(input("Ingrese parcial3: ")) 

       sumafisica=(parcial1 +parcial2 +parcial3)
       promediofisica= sumafisica/3

       print(f"su promedio es {promediofisica}")
       if promediofisica >=8:
        print("fisica promociona")
       elif promediofisica <8 and promediofisica >=6:
        print("fisica aprobado")
       else :
        print("fisica desaprobado") 

        print("\nSolo falta ingresar una materia:")
        print("Ingrese las notas de Lengua: \n")
                           
       parcial1=float(input("Ingrese parcial1: "))
       parcial2=float(input("Ingrese parcial2: "))
       parcial3=float(input("Ingrese parcial3: ")) 
       sumalengua=(parcial1 +parcial2 +parcial3)
       promediolengua= sumalengua/3

       print(f"su promedio es {promediolengua}")
       if promediolengua >=8:
        print("lengua promocionada")
       elif promediolengua <8 and promediolengua >=6:
        print("lengua aprobado")
       else : 
        print("lengua desaprobado")

       
    else:
        print("OPCIÓN INCORRECTA!")

elif opcion == 3:
    
    print ("\nIngrese las notas de Fisica")                 
    parcial1=float(input("Ingrese parcial1: "))
    parcial2=float(input("Ingrese parcial2: "))
    parcial3=float(input("Ingrese parcial3: ")) 

    sumafisica=(parcial1 +parcial2 +parcial3)
    promediofisica= sumafisica/3

    print(f"su promedio es {promediofisica}")
    if promediofisica >=8:
     print("fisica promociona")
    elif promediofisica <8 and promediofisica >=6:
        print("fisica aprobado")
    else :
        print("fisica desaprobado")

    print("Selecione Materias: \n")
    print("Presiona 1 Para Lengua ")
    print("Presiona 2 Para Matematica\n")
    opcion4 = int(input("¿Cúal es tu opción deseada?:"))
  
    if opcion4 == 1:
    
     print ("\nIngrese las notas de Lengua\n")                           
     parcial1=float(input("Ingrese parcial1: "))
     parcial2=float(input("Ingrese parcial2: "))
     parcial3=float(input("Ingrese parcial3: ")) 
     sumalengua=(parcial1 +parcial2 +parcial3)
     promediolengua= sumalengua/3

     print(f"su promedio es {promediolengua}")
     if promediolengua >=8:
      print("lengua promocionada")
     elif promediolengua <8 and promediolengua >=6:
      print("lengua aprobado")
     else : 
      print("lengua desaprobado")
    
     print("\nSolo falta ingresar una materia:")
     print("Ingrese las notas de Matemática: \n")

     parcial1=float(input("Ingrese parcial1: "))
     parcial2=float(input("Ingrese parcial2: "))
     parcial3=float(input("Ingrese parcial3: ")) 

     sumamatematica=(parcial1 +parcial2 +parcial3)
     promediomatematica= sumamatematica/3

     print(f"su promedio es {promediomatematica}")
     if promediomatematica >=8:
      print("matematica promociona")
     elif promediomatematica <8 and promediomatematica >=6:
       print("matematica aprobado")
     else :
       print("matematica desaprobado")

    elif opcion4 == 2:
       print ("\nIngrese las notas de Matematica")                  
       parcial1=float(input("Ingrese parcial1: "))
       parcial2=float(input("Ingrese parcial2: "))
       parcial3=float(input("Ingrese parcial3: ")) 

       sumamatematica=(parcial1 +parcial2 +parcial3)
       promediomatematica= sumamatematica/3

       print(f"su promedio es {promediomatematica}")
       if promediomatematica >=8:
        print("matematica promociona")
       elif promediomatematica <8 and promediomatematica >=6:
        print("matematica aprobado")
       else :
        print("matematica desaprobado") 
       
       print("\nSolo falta ingresar una materia:")
       print("Ingrese las notas de Lengua: \n")

       parcial1=float(input("Ingrese parcial1: "))
       parcial2=float(input("Ingrese parcial2: "))
       parcial3=float(input("Ingrese parcial3: ")) 
       sumalengua=(parcial1 +parcial2 +parcial3)
       promediolengua= sumalengua/3

       print(f"su promedio es {promediolengua}")
       if promediolengua >=8:
        print("lengua promocionada")
       elif promediolengua <8 and promediolengua >=6:
        print("lengua aprobado")
       else : 
        print("lengua desaprobado")
    else:
        print("OPCIÓN INCORRECTA!")


if promediolengua >=8 and promediomatematica >=8 and promediofisica >=8:
   
 print ("Estas promocionada")

if promediolengua >=6 and promediomatematica >=6 and promediofisica >=6:
  
 print ("Estas aprobado") 

if promediolengua <6 and promediomatematica <6 and promediofisica <6:

 print ("Estas desaprobado")

print ("Fin del ciclo")
