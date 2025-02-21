# crear programa con numero secreto

numero_secreto = 5

# inicializo el contador de intentos en 0

intentos = 0

print("Vamos a adivinar el numero secreto del 1 al 10 ")

while True:
    numero = int(input("Ingresa un numero "))
    intentos += 1 
    if numero < numero_secreto:
        print("El numero seleccionado es menor al numero secreto, intenta nuevamente")
    elif numero > numero_secreto:
        print("El numero ingresado es muy alto, intenta nuevamente")
    else:
        print("Felicidades, acertaste el numero secreto")
        break
print("Gracias por participar")


