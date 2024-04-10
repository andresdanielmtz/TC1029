import time


def quiz():
    result = open("resultados.txt", "w", encoding="utf-8")
    cal = 0
    name = input("¿Cuál es tu nombre?\n")
    result.write("Nombre: " + name + "\n")
    while True:

        print("Bienvenido al quiz...! ¿Estás preparado?\n")
        time.sleep(1)
        print("Selecciona una de las siguientes opciones, gracias. \n")
        first = int(input("""¡Pregunta #1!
        Resuelve la siguiente ecuación utilizando la formula general: 

                             x^2 + 10x + 25 = 0 

        1) -5
        2) -10, -15
        3) -5, 5
        
        Opción: \n """))
        if first == 1:
            cal += 10
            result.write("La primera respuesta estuvo bien, +10 puntos. \n")

        print("Lee el siguiente texto: \n")
        l = open("lectura/lectura_publicidad.txt", "r")
        le = l.read()
        print(le)
        l.close()

        second = int(input("""¡Pregunta #2!

            ¿Cuánto es el porcentaje de la población que vive en la pobreza en el país?

        1) 12.4% 
        2) 30%
        3) 24.8%
        
        Opción: \n """))
        if second == 3:
            cal += 10
            result.write("La segunda respuesta estuvo bien, +10 puntos. \n")

        third = int(input("""¡Pregunta #3!
        
                ¿Qué es la probabilidad? 
        1) La probabilidad es una medida de la certidumbre de que ocurra un evento.
        2) La probabilidad es una rama de las matemáticas que busca explicar sucesos paranormales.
        3) La probabilidad no existe.
        
        Opción: \n """))
        if third == 1:
            cal += 10
            result.write("La tercera respuesta estuvo bien, +10 puntos. \n")

        print("¡Felicidades! Terminaste el quiz\n")
        print("Tu resultado es de...\n")
        time.sleep(3)

        result.write("Tu calificación es: " + str(cal/3))
        if cal > 20:
            # 30/3 = 10, 20/3 = 6.666, 10/3 = 3.333
            print("Felicidades! Tu calificacion es de:", (cal/3))
        else:
            print("Tu calificacion es de:", (cal/3))
        break

# aqui deberiamos de poner la funcion completa del quiz
