import formula_general.andresMartinez_formula as mate
import general_functions as gf 

def eleccion():
    while True:
        try:
            c = int(input("""
        -----------------------------------
        ¡Hola! Escogiste: Resolver ecuaciones cuadráticas con la fórmula general
        -----------------------------------
        Por favor escoge una de las siguientes opciones:

        1) Teoría
        2) Ejercicios 
        3) Quiz
        4) Ver calificaciones previas... 
        5) Salir
        \n"""))
            if c == 1:
                mate.teoria()
            elif c == 2:
                mate.ejercicios()
                break
            elif c == 3:
                mate.quiz()
                break
            elif c == 4: 
                gf.result_andres()
            elif c == 5: 
                print("Saliendo...")
                break 
            else:
                mate.error_message()
        except ValueError:
            mate.error_message()
