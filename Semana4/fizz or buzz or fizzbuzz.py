# Voy a crear un codigo, donde se le pida un numero al usuario, 
# si es divisible entre 3 mostrar Fizz
# Mostrar Buzz si es divisible entre 5 y fizzbuzz si es divisibloe entre los 2

numero = int(input("Ingrese un numero: "))
if numero % 15 == 0:
    print("FizzBuzz")
elif numero % 3 == 0:
    print("Fiz")
elif numero % 5 == 0:
    print("Buzz")
else:
    print("El numero no es divisible ni entre 3 ni 5")