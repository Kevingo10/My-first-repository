#Cree un algoritmo que le pida 2 números al usuario, 
# los guarde en dos variables distintas (primero y segundo)
#y los ordene de menor a mayor en dichas variables.

numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
if numero1 > numero2:
    print(f"El orden de menor a mayor es: {numero2} , {numero1}")
else:
    print(f"El orden de menor a mayor es {numero1} , {numero2}")
print("Gracias")
