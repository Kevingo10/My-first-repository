# Voy a crear un codigo que le pida al usuario un timepo en segundos
# depende de ese tiempo verificar si es < o > a 10 min 
# Y especificar si es < a 10 min cuanto faltaria para esos 10 min

tiempo_segundos = float(input("Ingrese el tiempo en segundos: "))
if tiempo_segundos > 600:
    print("El tiempo es mayor a 10 minutos")
elif tiempo_segundos < 600:
    tiempo_faltante = 600 - tiempo_segundos
    print("El tiempo es menor a 10 minutos")
    print(f"El faltante del tiempo para los 10 minutos es: {tiempo_faltante}" " segundos")
else:
    print("El tiempo ingresado son exactamente 10 minutos")
    
