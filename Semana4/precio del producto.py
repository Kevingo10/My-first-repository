# Crear un codigo donde muestre el descuento de acuerdo al precio

precio = float(input("Ingrese el precio del producto " ))
precio_mayor = precio >= 100
precio_menor = precio < 100
if precio >= 100:
    descuento = 0.10
    print("el descuento es del 10%")
else:
    descuento = 0.20
    print("El descuento es del 2%")
precio_con_descuento = precio - (precio * descuento)
print(f"de acuerdo al monto seleccionado, el nuevo valor del producto sera:{precio_con_descuento} ")
