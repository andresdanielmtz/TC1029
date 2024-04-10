import lectura.MartinTanori_fun as lectfun

def submenu_lectura():
    while True: 
        second_choice = int(input(("""Selecciona: 
            1) Teoría de Lectura
            2) Ejercicios de Lectura 
            3) Quiz 
            4) Salir 
            Opción: \n """)))
        if second_choice==1:
            lectfun.lectura_teoria()
        elif second_choice==2:
            lectfun.lectura_ejercicios()
        elif second_choice == 3: 
            lectfun.lectura_quiz() # :) 
        elif second_choice == 4: 
            print("Saliendo... \n")
            break
        else: print("Por favor escoge una opción válida, ¡gracias! \n")
