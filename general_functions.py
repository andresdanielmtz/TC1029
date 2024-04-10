import time


def creditos():
    print("""Proyecto Final
            Pensamiento Computacional en la Ingenieria
            Prof. Luis Carlos Felix Herrán
            
            Andrés Martínez - A00227463
            Santiago Poblete - A01254609
            Diego Telles - A01254736
            Martín Tánori - A01252900 

            ¡Muchas gracias! \n
            """)
    time.sleep(3)

def result_andres():
    try:
        o_formula_general = open(
            "formula_general/AndresMartinez_resultados_formula.txt", "r", encoding='utf-8')
        print("Resultado de Numeros Cuánticos: \n" + o_formula_general.read())
        o_formula_general.close()
    except FileNotFoundError:
        print("No hemos podido encontrar el archivo...")

def result_diego():
    try:
        o_probabilidad = open(
            "probabilidad/DiegoTelles_result.txt", "r", encoding='utf-8')
        print("Resultado de Probabilidad: \n" + o_probabilidad.read())
        o_probabilidad.close()
    except FileNotFoundError:
        print("No hemos podido encontrar el archivo...")

def result_martin():
    try:
        o_lectura = open("lectura/MartinTanori_resultados.txt",
                         "r", encoding='utf-8')
        print("Resultado de Lectura: \n" + o_lectura.read())
        o_lectura.close()
    except FileNotFoundError:
        print("No hemos podido encontrar el archivo...")

def result_santiago():
    try:
        o_cuanticos = open(
            "cuanticos/SantiagoEduardoPoblete_resultados.txt", "r", encoding='utf-8')
        print("Resultado de Números Cuánticos: \n" + o_cuanticos.read())
        o_cuanticos.close()
    except FileNotFoundError:
        print("No hemos podido encontrar el archivo...")


def print_results():
    try:
        o_cuanticos = open(
            "cuanticos/SantiagoEduardoPoblete_resultados.txt", "r", encoding='utf-8')
        print("Resultado de Números Cuánticos: \n" + o_cuanticos.read())
        o_cuanticos.close()

        o_probabilidad = open(
            "probabilidad/DiegoTelles_result.txt", "r", encoding='utf-8')
        print("Resultado de Probabilidad: \n" + o_probabilidad.read())
        o_probabilidad.close()

        o_lectura = open("lectura/MartinTanori_resultados.txt",
                         "r", encoding='utf-8')
        print("Resultado de Lectura: \n" + o_lectura.read())
        o_lectura.close()

        o_formula_general = open(
            "formula_general/AndresMartinez_resultados_formula.txt", "r", encoding='utf-8')
        print("Resultado de Numeros Cuánticos: \n" + o_formula_general.read())
        o_formula_general.close()

        o_quiz_final = open("resultados.txt", "r", encoding='utf-8')
        print("Resultado de Quiz Final: \n" + o_quiz_final.read())
        o_quiz_final.close()


    except FileNotFoundError:
        print("No hemos podido encontrar el archivo...")
