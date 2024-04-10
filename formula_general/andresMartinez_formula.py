import time


def error_message():
    print("Por favor escoge una opción válida, ¡gracias! \n")


def teoria():
    prob_theory = open(
        "formula_general/AndresMartinez_teoria_probabilidad.txt", "r", encoding="utf8")
    read_prob_theory = prob_theory.read()
    print(read_prob_theory)

def quiz():
    print("Escogiste quiz... ¡Hora de las preguntas!")
    name = input("¿Cuál es tu nombre?\n")
    grade = 0 
    equations_set = [
        "x^2 + 14x + 49",
        "x^2 + 8x + 16",
        "x^2 + 9x + 18",
        "x^2 + 16x + 4",
    ]

    primer_set = [
        "1) x = -7 ",
        "2) x1 = -14, x2 = 7 ",
        "3) x1 = 49, x2 = 14",
    ]

    segundo_set = [
        "1) x1 = -9, x2 = 1",
        "2) x1 = -4 ",
        "3) x1 = 4, x2 = 8",
    ]

    tercer_set = [
        "1) x1 = -3, x2 = -6",
        "2) x1 = -4, x2 = 2",
        "3) x1 = 4, x2 = 8",
    ]

    cuarto_set = [
    "1) x1 = 3, x2 = 14",
    "2) x1 = 16, x2 = 24",
    "3) x1 = 8, x2 = 8",
    ]

    # 1 
    # 2 
    # 1 
    try:
        lect_resultados = open(
            "formula_general/AndresMartinez_resultados_formula.txt", "a", encoding="utf-8")
    except FileNotFoundError: # si no hay archivo, lo crea : ) 
        lect_resultados = open(
            "formula_general/AndresMartinez_resultados_formula.txt", "w", encoding="utf-8")
    for i in range(len(equations_set)):
        print("¿Cuál es la respuesta de la siguiente ecuación?")
        if i == 0: 
            print("x^2 + 14x + 49 \n")
            for j in primer_set:
                print(j)
            x = int(input("Elige una opción: \n"))
            if x-1 == primer_set.index("1) x = -7 "):
                grade += 1 
        elif i == 1:
            print("x^2 + 8x + 16 \n")
            for j in segundo_set:
                print(j)
            x = int(input("Elige una opción: \n"))
            if x-1 == segundo_set.index("2) x1 = -4 "):
                grade += 1
        elif i == 2:
            print("x^2 + 9x + 18 \n")
            for j in tercer_set:
                print(j)
            x = int(input("Elige una opción: \n"))
            if x-1 == tercer_set.index("1) x1 = -3, x2 = -6"):
                grade += 1
        elif i == 3:
            print("x^2 + 16x + 4 \n")
            for j in cuarto_set:
                print(j)
            x = int(input("Elige una opción: \n"))
            if x-1 == cuarto_set.index("3) x1 = 8, x2 = 8"):
                grade += 1
    grade = (grade/3) * 100
    fecha = time.asctime(time.localtime(time.time()))
    print("Calculando...")
    time.sleep(2)
    print("Tu calificación es: " + str(grade) + "%")
    lect_resultados.write(f"""Nombre: {name} 
    Fecha: {fecha}
    Grade: {grade}
    \n""")
    contin = input("Presiona ENTER para continuar. \n")


def ejercicios():
    grade = 0
    print("Escogiste Ejercicio... ¡Hora de las preguntas!")

    question = int(input("""
    ¿Cuál es la respuesta de la siguiente ecuación?

                    4x^2 + 8x + 16

    1) x1 = -0.58578... , x2 = -3.4142...
    2) x1 = 0.49921, x2 = 12.6231
    3) x1 = 4, x2 = 8\n"""))

    if question == 1:  # cambiar
        grade += 1
        print("¡la respuesta es correcta! ")
    elif question == 1 or question == 2:
        print("""La respuesta es... incorrecta.
        Recuerda reemplazar las variables ax^2 + bx + c en la formula general...\n""")

    question = int(input("""
    ¿Por qué aparecen dos resultados cada que utilizamos la formula general en las ecuaciones cuadráticas?

    1) Porque el símbolo ± en la formula general genera dos resultados distintos.
    2) Porque utilizamos dos formulas diferentes dos veces para cada ecuación.
    3) Porque se ve mejor. \n"""))

    if question == 1:  # cambiar
        grade += 1
        print("¡la respuesta es correcta! ")
    elif question == 1 or question == 2:
        print("""La respuesta es... incorrecta.
        Recuerda que el símbolo ± es para que apliques las mismas variables en dos ecuaciones distintas: Una donde uses + y otra donde uses -. \n""")

    grade = str(round((grade / 3) * 100))
    print(f"Tu calificación es: {grade}\n")
    conti = input("Presiona ENTER para continuar. \n")

def ejercicios():
    name = input("¿Cuál es tu nombre? \n")
    result = open(
        "formula_general/AndresMartinez_resultados_formula.txt", "a", encoding="utf-8")

    grade = 0
    print("Escogiste Quiz... ¡Hora de las preguntas!")
    question = int(input("""
    ¿Cuál es la respuesta de la siguiente ecuación?

                    x^2 + 16x + 4

    1) x1 = 3, x2 = 14
    2) x1 = 16, x2 = 24
    3) x1 = 8, x2 = 8\n"""))

    if question == 3:
        grade += 1  # add
        print("¡La respuesta es correcta! \n")
    elif question == 1 or question == 2:
        print("""La respuesta es... incorrecta.
        Recuerda reemplazar las variables ax^2 + bx + c en la formula general...\n""")

    question = int(input("""
    ¿Cuál es la respuesta de la siguiente ecuación?

                    4x^2 + 8x + 16

    1) x1 = -0.58578... , x2 = -3.4142...
    2) x1 = 0.49921, x2 = 12.6231
    3) x1 = 4, x2 = 8\n"""))

    if question == 1:  # cambiar
        grade += 1
        print("¡la respuesta es correcta! ")
    elif question == 1 or question == 2:
        print("""La respuesta es... incorrecta.
        Recuerda reemplazar las variables ax^2 + bx + c en la formula general...\n""")

    question = int(input("""
    ¿Por qué aparecen dos resultados cada que utilizamos la formula general en las ecuaciones cuadráticas?

    1) Porque el símbolo ± en la formula general genera dos resultados distintos.
    2) Porque utilizamos dos formulas diferentes dos veces para cada ecuación.
    3) Porque se ve mejor. \n"""))

    if question == 1:  # cambiar
        grade += 1
        print("¡la respuesta es correcta! ")
    elif question == 1 or question == 2:
        print("""La respuesta es... incorrecta.
        Recuerda que el símbolo ± es para que apliques las mismas variables en dos ecuaciones distintas: Una donde uses + y otra donde uses -. \n""")

    grade = str(round((grade / 3) * 100))
    print(f"Tu calificación es: {grade}\n")
