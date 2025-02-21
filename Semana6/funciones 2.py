#Experimente con el concepto de scope:
#1. Intente accesar a una variable definida dentro de una función desde afuera.
#2.  Intente accesar a una variable global desde una función y cambiar su valor.
print("Primer ejercicio")
def funcion1():
    x = 10
    return x


resultado = funcion1()
print(f"Fuera de la funcion, x = {resultado}")


# segundo ejercicio

print(" Segundo ejercicio")
x = 20


def mi_funcion():
    global x
    x = 35
    print(f"Dentro de la funcion, x = {x}")


mi_funcion()
print(f"Fuera de la funcion, x = {x}")


