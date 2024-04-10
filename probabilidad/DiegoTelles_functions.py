import time


# Ejercicio de práctica
def ejercicio():
    print("Seleccionaste el apartado de 'Ejercicio de práctica'. ")
    nombredos = input(
        "¿Cómo te gustaría que se llamara la persona del ejercicio? ")
    respuesta = input(nombredos + " esta lanzando dardos a unos globos, de los cuales 7 contienen un papel dentro, ¿cuál es la probabilidad de que " +
                      nombredos + " le dispare a un globo con un papel si hay 28 globos? ")
    if respuesta == "1/4":
        print("Correcto!")
    elif respuesta == "7/28":
        print("Recuerda simplificar la fracción.")
        respuestados = input("¿Cuál es la probabilidad? ")
        if respuestados == "1/4":
            print("Correcto!")
    else:
        print("Recuerda dividir el numero seleccionado entre el total y despues simplificarlo. ")
        respuestatres = input("¿Cuál es la probabilidad? ")
        if respuestatres == "1/4":
            print("Correcto!")
        elif respuestatres == "7/28":
            print("Recuerda simplificar la fracción.")
            respuestacuatro = input("¿Cuál es la probabilidad? ")
            if respuestacuatro == "1/4":
                print("Correcto!")
            else:
                print("Te recomendamos volver a leer la explicación.")
    question = input(""". Lupita tiene 14 regalos, 5 de ellos son pelotas , 2 muñecas, 3 pinturas y 4 son camisetas. Si Lupita reparte los regalos de manera al azar entre sus alumnos, ¿cuál es la probabilidad de que a un alumno no le toquen las camisetas?
        a) 4/14
        b) 2/7
        c) 5/7
        d) 3/4\n""")
    if question.lower() == "c":
        print("¡La respuesta es correcta!")
    else:
        print(
            "La respuesta es incorrecta... procura volver a leer el problema detenidamente.")
    question = input(""". Pedro juega a la loteria junto con sus otros 4 amigos, despues de 5 minutos uno de sus amigos se aburrió y dejo de jugar y a otro de sus amigos se le pasó una carta, ¿cuál es la probabilidad de que Pedro gane?
        a) 1/5
        b) 3/5
        c)1/2
        d) 1/3\n""")
    if question.lower() == "d":
        print("¡La respuesta es correcta!")
    else:
        print(
            "La respuesta es incorrecta... procura volver a leer el problema detenidamente.")
    print("Has termindo los ejercicios, ¡bien hecho! \n")


def leer_probabilidad():
    fh = open("probabilidad/DiegoTelles_functions.py", "r", encoding="utf-8")
    teoria = fh.read()
    print(teoria)
    fh.close()
    print("\n")


def leer_como_calcular():
    fh2 = open("probabilidad/DiegoTelles_ejemplo.txt", "r", encoding="utf-8")
    ejemplo = fh2.read()
    print(ejemplo)
    fh2.close()
    print("\n")


def examenprobabilidad():
    name = input("¿Cuál es tu nombre? \n")
    w = open("probabilidad/DiegoTelles_result.txt", "a", encoding="utf-8")
    fecha = time.asctime(time.localtime(time.time()))
    calificacionexamen = 0
    print("A continuación se te presentará un exámen, el cuál contará de 5 preguntas.")
    respuestaexamenuno = input(
        "Arturo tiene 18 canicas, 5 son azules, 9 verdes y 4 rojas. ¿Cuál es la probabilidad de que Arturo saque una canica azul al azar? ")
    if respuestaexamenuno == "5/18":
        calificacionexamen = calificacionexamen + 20
    respuestaexamendos = input(
        "¿Cuál es la probabilidad en porcentaje de que Sofia escoja un número par al azar del 1 al 10?. No escribas el signo de porcentaje. ")
    if respuestaexamendos == "50":
        calificacionexamen = calificacionexamen + 20
    respuestaexamentres = input(
        "¿Cuál es la probabilidad de que Santiago saque de un cajón una prenda azul o verde, si hay 7 azules, 8 verdes, 3 blancas y 2 negras? ")
    if respuestaexamentres == "3/4":
        calificacionexamen = calificacionexamen + 20
    if respuestaexamentres == "15/20":
        calificacionexamen = calificacionexamen + 10
    respuestaexamencuatro = input(
        "¿Cuál es la probabilidad en porcentaje de que me de toque un boleto rojo, si las opciones son rojo, azul, blanco y verde?. No escribas el signo de porcentaje. ")
    if respuestaexamencuatro == "25":
        calificacionexamen = calificacionexamen + 20
    respuestaexamencinco = input(
        "¿Cuál es la probabilidad de que Ernesto escoja al azar un numero impar del 1 al 20? ")
    if respuestaexamencinco == "1/2":
        calificacionexamen = calificacionexamen + 20
    if respuestaexamencinco == "10/20":
        calificacionexamen = calificacionexamen + 10
    print("Tu calificación es de:", calificacionexamen)
    w.write(f"""Nombre: {name} 
    Fecha: {fecha}
    Grade: {calificacionexamen}
    \n""")
    if calificacionexamen > 60:
        print("Tu calificación es aprobatoria!")
    if calificacionexamen < 60:
        print("Tu calificación no es aprobatoria")
