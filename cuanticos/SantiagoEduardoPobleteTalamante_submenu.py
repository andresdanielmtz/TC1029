import cuanticos.SantiagoEduardoPobleteTalamante_fun as nc

def submenu_ciencias():
    while True: 
            print("¡Escogiste Ciencias!")
            second_choice = int(input(("""Selecciona tu tópico: 
            1) Teoría 
            2) Ejercicio de números cuánticos
            3) Ejercicio de Bohr (Quiz)
            4) Salir de la sección de ciencias
            Opción: """)))
            if second_choice == 1:
                print("Escogiste: Teoría General ")
                nc.abrirarch()
            elif second_choice == 2:
                print("Escogiste: Ejercicio de números cuánticos ")
                nc.problemascuant()
            elif second_choice == 3:
                print("Escogiste: Ejercicio de Niels Bohr (Quiz) ")
                nc.problemasquiz()
            else:
                print("Escogiste: Salir de la sección de ciencias")
                break 