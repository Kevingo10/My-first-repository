# crear un codigo para ver el porcentaje de 
# hombres y mujeres, donde 1 es mujer y 2 hombre

lista = []
contador_hombre = 0 
contador_mujer = 0
for i in range(6):
    sexo = input(f"Ingrese el sexo de la persona numero: {i + 1} (1 para mujer o 2 para hombre): ")
    if sexo == "1":
        contador_mujer +=1
    elif sexo == "2":
        contador_hombre += 1
    else:
        print("El valor ingresado esta incorrecto")
        continue
total_personas = contador_hombre + contador_mujer
if total_personas > 0:
    porcentaje_hombres = (contador_hombre / total_personas) * 100
    porcentaje_mujeres = (contador_mujer / total_personas) * 100
    print(f"El porcentaje de hombre es {porcentaje_hombres}")   
    print(f"El porcentaje de mujeres es {porcentaje_mujeres}")
else:
    print("Entrada invalida")
