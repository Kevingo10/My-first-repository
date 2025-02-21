# Vamos a crear un codigo que me indique cuantas notas aprobadas y desaprobadas tiene

notas = []
notas_obtenidas = int(input("Ingrese la cantidad de notas: "))
for i in range(notas_obtenidas):
    nota = float(input(f"Ingrese la nota numero {i + 1} :"))
    notas.append(nota)
aprobadas = 0
desaprobadas = 0
suma_aprobadas = 0
suma_desaprobadas = 0
suma_total = 0
for nota in notas:
    suma_total += nota
    if nota >= 70:
        aprobadas += 1
        suma_aprobadas += 1
    else:
        desaprobadas += 1
        suma_desaprobadas += 1

# calcular promedios

# Para evitar la división por cero, solo dividimos si hay notas aprobadas o desaprobadas
promedio_aprobadas = suma_aprobadas / aprobadas if aprobadas != 0 else 0
promedio_desaprobadas = suma_desaprobadas / desaprobadas if desaprobadas != 0 else 0

# Imprimir resultados
print(f"\nResultados:")
print(f"Cantidad de notas aprobadas: {aprobadas}")
print(f"Cantidad de notas desaprobadas: {desaprobadas}")
print(f"Promedio de las notas aprobadas: {promedio_aprobadas:}")
print(f"Promedio de las notas desaprobadas: {promedio_desaprobadas:}")







