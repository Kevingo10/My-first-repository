# Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
import math


def es_primo(n):
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def obtener_primos(lista):
    primos = []
    for numero in lista:
        if es_primo(numero):
            primos.append(numero)
    return primos


numeros = [1,4,6,7,13,9,67]
primos = obtener_primos(numeros)
print(primos)
