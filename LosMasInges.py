import math
import general_functions  # func.py
import formula_general.andresMartinez_formula_submenu as calculo_submenu  # andrés
import cuanticos.SantiagoEduardoPobleteTalamante_submenu as cuanticos_submenu
import lectura.MartinTanori_submenu as lectura_submenu
import probabilidad.DiegoTelles_submenu as probabilidad_submenu
import quiz

# Proyecto Final Agosto Diciembre 2022
# Pensamiento Computacional en la Ingenieria
# Prof. Luis Carlos Felix Herrán
#
# Andrés Martínez - A00227463
# Santiago Poblete - A01254609
# Diego Telles - A01254736
# Martín Tánori - A01252900

while True:
    try:   
        choice = int(input("""
        Por favor escoge una de las opciones:
        1) Matematicas
        2) Ciencias
        3) Lectura
        4) Quiz Final
        5) Acerca de...
        6) Salir 

        Opcion: """))
        if choice == 1:  # matemáticas: andrés y diego
            print("¡Escogiste Matemáticas!")
            second_choice = int(input(("""Selecciona tu tópico: 
            1) Resolver ecuaciones cuadráticas con la fórmula general
            2) Nociones de probabilidad 
            
            Opción: \n""")))
            if second_choice == 1:
                calculo_submenu.eleccion()  # :)
            else:
                print("Escogiste: Nociones de probabilidad ")
                probabilidad_submenu.menu()
        elif choice == 2:  # ciencias: santiago
            print("¡Escogiste Ciencias!")
            cuanticos_submenu.submenu_ciencias()

        elif choice == 3:  # lectura: martin
            print("¡Escogiste Lectura!")
            lectura_submenu.submenu_lectura()

        elif choice == 4:  # quiz parcial
            quiz.quiz()
        elif choice == 5:  # creditos..!
            general_functions.creditos()
        elif choice == 6:  # salir
            print("Saliendo... \n")
            break
        else:
            print("Por favor escoge una opción correcta, ¡gracias!")
    except ValueError:
        print("Por favor escoge una opción correcta, ¡gracias!")
        
