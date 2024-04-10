import time 
import random 

def lectura_teoria():
    intro_lect_txt=open('lectura/MartinTanori_read.txt','r', encoding="utf8")
    intro_lect=intro_lect_txt.read()
    print(intro_lect)
    intro_lect_txt.close()

def lectura_quiz():
    lect_resultados = open("lectura/MartinTanori_resultados.txt", "a", encoding="utf8")  
    print("Estás iniciando el quiz de Lectura")
    time.sleep(2) 
    name = input("Escribe tu nombre aquí: \n ")
    grade = 0 
    question = input("""¿Cuál es el tema principal que desarrolla el texto?
    A) Los contenidos discriminatorios en la publicidad en el país.
    B) La aceptación de los roles tradicionales en la población.
    C) Los problemas de identidad en las promociones de venta.
    """)
    if question.lower() == "a":
        grade += 1 
    question = input("""2. Se infiere del texto que los anunciantes de bienes de consumo masivo: 
    A) Promueven la equidad de género premiando el mejor aviso.
    B) Deben sancionar a las empresas que discriminan al comprador.
    C) Carecen de una pauta común en sus campañas publicitarias.

    """)
    if question.lower() == "c":
        grade += 1 
    question = input("""Si se realizara un comercial de productos cosméticos para la televisión, probablemente: 
    A) Tomaría en cuenta la diversidad racial de los habitantes de la capital.
    B) Ofertaría tintes de color castaño claro entre otra variedad de tonos.
    C) Contaría con la participación de una hermosa mujer de tez blanca.
    """)
    if question.lower() == "c":
        grade += 1 
    grade = (grade/3) * 100 
    fecha = time.asctime(time.localtime(time.time()))
    lect_resultados.write(f"""Nombre: {name} 
    Fecha: {fecha}
    Grade: {grade}
    \n""")


def lectura_ejercicios():
    lect_tareas_txt=open('lectura/lectura_tareas.txt','r', encoding="utf8")
    lect_resultados = open("lectura/MartinTanori_resultados.txt", "a", encoding="utf8")  
    name = input("Escribe tu nombre aquí: \n ")
    lect1= lect_tareas_txt.read()

    print(lect1)
    lect_tareas_txt.close() 

    calif = 0 

    print('''1. Señale el título más adecuado para la lectura anterior.
    A) La importancia de la tareas escolares en la mejora del aprendizaje.
    B) El efecto nocivo de las tareas escolares.
    C) Evidencias científicas positivas sobre las tareas escolares.
    ''')

    resp=input()
    print()
    
    if resp.lower() == 'b': 
        print('¡Correcto!\n')
        calif += 50 

    elif resp.lower() == 'a' or resp.lower() == 'c':
        print('''La respuesta está incorrecta.

El texto relata los efectos negativos que pueden tener los niños al
obtener muchas tareas.
''')

    else:
        print('Intente de nuevo.\n')

    print('''2. ¿Cuál de los siguientes enunciados esta en la línea de
pensamiento del autor del texto?
    A) Realizar tareas dosificadoras y cultivadoras de la curiosidad.
    B) Aumentar la presión por las tareas escolares.
    C) Privar a los alumnos del disfrute de su vida juvenil.
    ''')

    resp=input()
    print()
    
    if resp.lower() == 'a': 
        print('¡Correcto!\n')
        calif += 50

    elif resp.lower() == 'b' or resp.lower() == 'c':
        print('''La respuesta está incorrecta.

El texto relata maneras para mejorar las tareas y vida estudiantil a los alumnos.
''')

    else:
        print('Intente de nuevo.\n')
    print("Tu calificacion es:", calif,"\n")