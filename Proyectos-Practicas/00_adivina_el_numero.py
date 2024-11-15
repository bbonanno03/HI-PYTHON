#https://github.com/cusanotech/proyectos-python-principiantes
#https://github.com/cusanotech/proyectos-python-principiantes/blob/main/Proyectos/%231%20ADIVINA%20EL%20NUMERO/cusanotech.py


import random

print("\t***ADIVINA EL NUMERO***")

print("ESTE JUEGO CONSITE EN ADIVINAR EL NUMERO QUE EL BOT ELIGIO. TEN EN CUENTA QUE ESTARA ENTRE EL 0 Y EL 100. QUE EMPIEZE EL JUEGO!!!")

numero = random.randint(0, 100)
adivinando = False


while not adivinando:  # Mientras la variable adivinando sea falso continua si no break
    try:


        numero_usuario = int(input("Ingresar un numero: "))
        if 0<= numero_usuario <= 100:
            if numero_usuario == numero:
                adivinando = True
            elif numero_usuario > numero:
                print("Más bajo")
            else:
                print("Más arriba")
        else:
            print("Ingresa un numero entre 0 y 100")
    
    except ValueError: #notificamos el error del valor ingresado por el usuario y que continue con los intentos
        print("estas ingresando un valor incorrecto. Por favor, ingresar un valor del 0 al 100.")


print("Has adivinado el numero!!! Felicitaciones!!!!")    



