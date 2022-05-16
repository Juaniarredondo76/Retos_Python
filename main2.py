from tkinter import E
from classes.Escuderia import Escuderia

lista=[]
costo=0
motor=0
opcion=0
piloto=0
r=0
m=0
f=0

while (opcion !=3):
    print("**********************************")
    print("           Bienvenido             ")
    print("              MENÚ                ")
    print("**********************************")
    print("1- ingreso datos de la escuderia: ")
    print("2- Comprobar cual es la escudería más cara")
    print("3. Comprobar cuantos escuderías tienen motor cuantas mercedes,  Ferrari y  renault")
    print("0--> SALIR ")
    print("************************************")

    opcion = int(input("digite el numero según la opcion: "))

    if (opcion == 1):

        escuderia=Escuderia()
        escuderia.nombre=input("digite el nombre de la escuderia : ")
        escuderia.motor=input("ingrese el motor(m=mercedes, f=Ferrari, r=renault) : ")
        escuderia.piloto=input("ingrese el piloto : ")
        escuderia.costo=int(input("ingrese costo anual de la escuderia : "))
        escuderia=Escuderia(nombre,motor,costo,piloto)
        costo.append(escuderia)
        motor.append(escuderia.motor)

    elif (opcion == 2):
        costoAnual=lista[0].costo
        nombre=lista[0].nombre

        print(costoAnual)

        for escuderia in lista:
            if (escuderia.tiempo > costoAnual):
                        costoAnual=escuderia.tiempo
            print("el mayor costo es:  ",costoAnual, " y el nombre de la escuderia es: ",nombre)

    elif(opcion ==3):

        f=motor.count("Ferrari")
        m=motor.count("Mercedes")
        r=motor.count("Renault")

        print('motores ferrari', f)
        print('motores renault', r)
        print('motores mercesdes', m)

    
    elif (opcion == 0):

        salir = True

    else:
       print("numero no valido")

