from probabilidad.DiegoTelles_functions import *


def menu():
    while True: 
        #Menú
        print("Menú")
        print("1. ¿Qué es la probabilidad?")
        print("2. ¿Cómo se calcula?")
        print("3. Ejercicio de práctica")
        print("4. Exámen")
        print("5. Salir")
        eleccion=input("Selecciona un número ")

        #¿Qué es la probabilidad?
        if eleccion == "1":
            leer_probabilidad() 
        #¿Cómo se calcula?
        if eleccion == "2":
            leer_como_calcular()
            
        #Ejercicio
        if eleccion == "3":
            ejercicio()

        #Exámen
        if eleccion == "4":
            examenprobabilidad()
        
        if eleccion == "5":
            print("Saliendo...")
            break 
        
            

      