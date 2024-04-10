import time


def abrirarch():
    fh = open("cuanticos/SantiagoEduardoPoblete_teoria.txt",
              "r", encoding="utf-8")
    numcuant = fh.read()
    print(numcuant)
    fh.close()
    print("\n")


def problemascuant():
    name = input("Cual es tu nombre? ")
    correctas = 0
    r = open("cuanticos/SantiagoEduardoPoblete_resultados.txt",
             "a", encoding="utf-8")
    print("El ejercicio evaluara tu conocimiento de cada tipo de numero atomico")
    print("Pregunta 1:")

    print("El numero atómico l es el que corresponde a…\n""1) Los niveles de energía de un electrón.\n""2) La geometría o forma del orbital.\n""3) La orientación espacial de los orbitales.\n""4) El momento angular intrínseco del electrón.""\n")
    pregunta1 = int(input())
    if pregunta1 == 2:
        print("Respuesta correcta!")
        correctas = correctas + 25
    else:
        print("Respuesta incorrecta :/...")
        print(
            "La respuesta correcta era: Número cuántico secundario (l) [spdf]")
        print("- Conocido también como momento angular. Corresponde a la geometría o forma del orbital.")

    print("Pregunta 2")
    print("El numero atómico m es el que corresponde a…\n""1) Los niveles de energía de un electrón.\n""2) La geometría o forma del orbital.\n""3) La orientación espacial de los orbitales.\n""4) El momento angular intrínseco del electrón.""\n")

    pregunta2 = int(input())

    if pregunta2 == 3:
        print("Respuesta correcta!")
        correctas = correctas + 25
    else:
        print("Respuesta incorrecta :/...")
        print("La respuesta correcta era: Número cuántico magnético (m)")
        print("- Corresponde a la orientación espacial de los orbitales.")
    print("Pregunta 3")
    print("El numero atómico s es el que corresponde a…\n""1) Los niveles de energía de un electrón.\n""2) La geometría o forma del orbital.\n""3) La orientación espacial de los orbitales.\n""4) El momento angular intrínseco del electrón.""\n")
    pregunta3 = int(input())

    if pregunta3 == 4:
        print("Respuesta correcta!")
        correctas = correctas + 25
    else:
        print("Respuesta incorrecta :/...")
        print("La respuesta correcta era: Número cuántico spin (s)")
        print("- Describe el momento angular intrínseco del electrón.")

    print("Pregunta 4")
    print("El numero atómico s es el que corresponde a…\n""1) Los niveles de energía de un electrón.\n""2) La geometría o forma del orbital.\n""3) La orientación espacial de los orbitales.\n""4) El momento angular intrínseco del electrón.""\n")
    pregunta4 = int(input())

    if pregunta4 == 1:
        print("Respuesta correcta!")
        correctas = correctas + 25
    else:
        print("Respuesta incorrecta :/...")
        print(
            "La respuesta correcta era : Número cuántico principal (n) [horizontales/periodos en la tabla periodica]")
        print("- Corresponde a los niveles de energía de un electrón.")

    print("Tu calificacion en este ejercicio es de ", correctas, "%")
    r.write(f"""Name: {name} """)


def problemasquiz():
    name = input("Cual es tu nombre? \n")
    correctas = 0
    r = open("cuanticos/SantiagoEduardoPoblete_resultados.txt",
             "a", encoding="utf-8")
    print("El quiz evaluara tu conocimiento de los temas de ciencias.")
    print("Pregunta 1:")

    print("Los electrones describen _______ circulares en torno al núcleo del átomo sin irradiar energía…\n""1) Órbitas.\n""2) Geometrías.\n""3) Las orientaciones.\n""4) Las figuras.""\n")
    pregunta1 = int(input())
    if pregunta1 == 1:
        correctas = correctas + 14

    print("Pregunta 2")
    print("Bohr propuso su modelo atómico en el año…\n""1) 1913.\n""2) 1319.\n""3) 1931.\n""4) 1941.""\n")

    pregunta2 = int(input())

    if pregunta2 == 1:
        correctas = correctas + 14

    print("Pregunta 3")
    print("El electrón solo emite o absorbe ______ en los saltos de una órbita permitida a otra...\n""1) Luz.\n""2) Fuego.\n""3) Energía.\n""4) Electrones.""\n")
    pregunta3 = int(input())

    if pregunta3 == 3:
        correctas = correctas + 14
    
    print("Pregunta 4:")

    print("El numero atómico l es el que corresponde a…\n""1) Los niveles de energía de un electrón.\n""2) La geometría o forma del orbital.\n""3) La orientación espacial de los orbitales.\n""4) El momento angular intrínseco del electrón.""\n")
    pregunta4 = int(input())
    if pregunta4 == 2:
        correctas = correctas + 14


    print("Pregunta 5")
    print("El numero atómico m es el que corresponde a…\n""1) Los niveles de energía de un electrón.\n""2) La geometría o forma del orbital.\n""3) La orientación espacial de los orbitales.\n""4) El momento angular intrínseco del electrón.""\n")

    pregunta5 = int(input())

    if pregunta5 == 3:
        correctas = correctas + 14

    print("Pregunta 6")
    print("El numero atómico s es el que corresponde a…\n""1) Los niveles de energía de un electrón.\n""2) La geometría o forma del orbital.\n""3) La orientación espacial de los orbitales.\n""4) El momento angular intrínseco del electrón.""\n")
    pregunta6 = int(input())

    if pregunta6 == 4:
        correctas = correctas + 14


    print("Pregunta 7")
    print("El numero atómico s es el que corresponde a…\n""1) Los niveles de energía de un electrón.\n""2) La geometría o forma del orbital.\n""3) La orientación espacial de los orbitales.\n""4) El momento angular intrínseco del electrón.""\n")
    pregunta7 = int(input())

    if pregunta7 == 1:
        correctas = correctas + 14

    print("Tu calificacion en este quiz es de ", correctas, "%")
    fecha = time.asctime(time.localtime(time.time()))
    r.write(f"""Nombre: {name} 
        Fecha: {fecha}
        Grade: {correctas}
        \n""")